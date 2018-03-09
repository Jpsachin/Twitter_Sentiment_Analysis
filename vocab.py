#!/usr/bin/python2.7

class SentiWords:

	def __init__(self, file = open("./Datasets/SentiWordNet_3.0.0_20130122.txt", "r")):
		self.__posScore = []
		self.__negScore = []
		self.__words = []
		self.__getWords(file)

	def __getWords(self, file): 
		for i, line in enumerate(file):
			if line[0]=="a":
				tokens = line.split("\t")

				for j, token in enumerate(tokens):
					if "#" in token and j>3:
						imWords = token.split(" ")
						for imWord in imWords:
							word = imWord.split("#")[0]
							self.__words.append(word)
							self.__posScore.append(tokens[2])
							self.__negScore.append(tokens[3])

	def search(self, word):
		try:
			indx = self.__words.index(word)
			print (indx)
		except ValueError:
			return [False, 0, 0]

		return [True, self.__posScore[indx], self.__negScore[indx]]
