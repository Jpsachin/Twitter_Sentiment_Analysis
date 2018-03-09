import csv
import nltk
from utils import acrDict,getEmosentiment
from collections import defaultdict
#from tweet import Tweet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

sid = SentimentIntensityAnalyzer()

filename = "tweets.csv"

allTweets = [];

def fExtract(tokens, sentence, hashtags, emojis):
	
	fvec = []
	emojiDict = getEmosentiment()
	#print (emojiDict)
	emojiscore = 0.0
	for emo in emojis:
		try:
			emojiscore += emojiDict[emo]
		except ValueError:
			pass

	#print ("lol", emojiscore) 


	#f0: percentage of capitalized text
	#f1: COMPLETELY CAPITAL text
	#f2: Capital + exclamation presence in a tweet
	#f3: nouns, adj etc
	#f4: no. of hashtags
	#f5: no. of positive [nouns, adj, verbs, adv]
	#f6: no. of negative [nouns, adj, verbs, adv]
	#f7: summation Prior pol. scores of words of that POS 
	#f8: sentence polarity
	#f9: no. of [poshashtags, neghashtags]
	#f10: no. of hashtags
	num_features = 21;
	for j in range(num_features):
		fvec.append(-1.0);

	# with open(filename, 'r') as csvfile:
	# 	csvreader = csv.reader(csvfile)
	# 	fields = csvreader.next()

	# 	for row in csvreader:
	# 		str1 = ''.join(row)
	# 		allTweets.append(str1);


	Cap = 0
	CAP = 0
	exc = 0
	nouns = 0.
	adjectives = 0.
	verbs = 0.
	adverbs = 0.
	line_size = len(tokens)
	posn, posadj, posv, posadv = 0.,0.,0.,0.
	negn, negadj, negv, negadv = 0.,0.,0.,0.
	polarity_sum = 0.0
	for word in tokens:
		# print type(line)
		## for capitalised, f0 and f1
		ss = sid.polarity_scores(word)
		pol = ss["compound"]
		polarity_sum += pol
		# print word, pol, ss
		uppers = [l for l in word if l.isupper()]
		# print "1st:", word[0]
		if word[0].isupper():
			Cap+=1
		s1 = len(uppers)
		s2 = len(word);
		if s1==s2:
			# print "CAP word: ", word
			CAP += 1

		## for exclamations and capitalised check
		last_char = word.strip()[-1]
		if last_char=='!':
			exc += 1
		## for JJ, NN, VB and RB counts
		if word[0].isalpha():
			sent = tuple(nltk.word_tokenize(word))
			tagged = nltk.pos_tag(sent)
			for w,t in tagged:
				p, n = 0,0
				sent_pos_type = None
				if t.startswith("NN"):
					sent_pos_type = "n"
					nouns += 1
					if pol > 0.0:
						posn += 1
					elif pol < 0.0:
						negn += 1
				elif t.startswith("JJ"):
					sent_pos_type = "a"
					adjectives += 1
					if pol > 0.0:
						posadj += 1
					elif pol < 0.0:
						negadj += 1
				elif t.startswith("VB"):
					sent_pos_type = "v"
					verbs += 1
					if pol > 0.0:
						posv += 1
					elif pol < 0.0:
						negv += 1
				elif t.startswith("RB"):
					sent_pos_type = "r"
					adverbs += 1
					if pol > 0.0:
						posadv += 1
					elif pol < 0.0:
						negadv += 1

	# nltk.sentiment.util.demo_liu_hu_lexicon(sentence, plot=False)
	# blob = TextBlob(sentence)
	# print "lol", blob.sentiment.polarity

	poshash, neghash = 0.0, 0.0
	for hashtag in hashtags:
		sentence = ""
		for word in hashtag:
			sentence += word + " "
		# print sentence
		ss = sid.polarity_scores(sentence)
		hashtag_pol = ss["compound"]
		if hashtag_pol > 0.0:
			poshash += 1
		elif hashtag_pol < 0.0:
			neghash += 1


	ss = sid.polarity_scores(sentence)
	sentence_pol = ss["compound"]
	fvec[0] = ((Cap*1.0)/line_size)
	fvec[1] = ((CAP*1.0)/line_size)
	fvec[3] = nouns
	fvec[4] = adjectives
	fvec[5] = verbs
	fvec[6] = adverbs
	fvec[7] = posn
	fvec[8] = posadj
	fvec[9] = posv
	fvec[10] = posadv
	fvec[11] = negn
	fvec[12] = negadj
	fvec[13] = negv
	fvec[14] = negadv
	fvec[15] = polarity_sum
	fvec[16] = sentence_pol
	fvec[17] = poshash
	fvec[18] = neghash
	fvec[19] = len(hashtags)
	fvec[20] = emojiscore
	
	# print "sfd", fvec[9]

	# print fvec[5]
	# print fvec[6]


	if Cap==0 or exc==0:
		fvec[2] = 0
	else:
		fvec[2] = 1
	return fvec	
# print "new:", tweet, fvec[i][0], fvec[i][1], fvec[i][2], fvec[i][3]



##y = "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!"
##
##x = y.split()
##z = [['me', 'too'],['love','you']]
##w = [u'\u270b']
###print (x,y,z)
##fExtract(x,y,z,w)

