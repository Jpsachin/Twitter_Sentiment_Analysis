#!/usr/bin/python2.7

acrDict = {
	"brb":"be right back",
	"lol":"laughing out loud",
	"btw":"by the way",
	"bcnu":"be seeing you",
	"bff":"best friends forever",
	"cya":"see you later",
	"dbeyr":"don't believe everything you read",
	"dilligas":"do i look like I give a shit",
	"fud":"fear, uncertainity and disinformation",
	"ily":"i love you",
	"imho":"in my humble opinion",
	"irl":"in real life",
	"iso":"in search of",
	"lmao":"laughing my ass off",
	"lylas":"Love You Like A Sister",
	"mhoty":"My Hat's Off To You",
	"oic":"Ohh, I see",
	"jk":"just joking",
	"rt":"retweet",
	"omg":"oh my god",
	"thx":"thanks",
	"xoxo":"hugs and kisses",
	"wtf":"what the hell",
	"wywh":"wish you were here",
	"tyvm":"thank you very much",
	"ty":"thank you",
	"sol":"sooner or later",
	"ttyl":"talk to you later",
	"pov":"point of view",
	"np":"no problem",
	"ot":"off topic",
	"rbtl":"read between the lines",
	"rotflmao":"Rolling On The Floor Laughing My Ass Off",
	"stby":"sucks to be you",
	"tmi":"too much information",
	"swak":"sealed with a kiss",
	"sitd":"still in the dark",
	"pls":"please",
	"plz":"please"
}

Emotions = {"sad":0, "happy":1, "angry":2, "surprise":3}

Polarity = {0:"negative", 1:"positive"}

def getEmosentiment(file = "./EmojiData/EmojiSentimentData.csv"):

	fp = open(file,encoding="utf-8")

	emoDict = {}

	for i, emoline in enumerate(fp):
		if i > 0:
			tokens = emoline.split(',')
			emocode = tokens[0]#.decode('utf-8')

			numNeg = float(tokens[4])
			numPos = float(tokens[6])
			total = float(tokens[2])

			score = (-numNeg + numPos)/total

			emoDict[emocode] = score

	return emoDict
