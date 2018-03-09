#!/usr/bin/python2.7


from getData import getTraindata, getTestdata
from vocab import SentiWords
from sklearn.mixture import GaussianMixture
from utils import getEmosentiment
import numpy as np
from sklearn import svm
from sklearn import tree
from nltk.classify import PositiveNaiveBayesClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def trainMP(data, labels, n_polarity = 4, n_epochs = 3):
        model = GaussianMixture(n_components=n_polarity, covariance_type="full", n_init=n_epochs)
        model.fit(data, labels)
        return model

def testMP(model, data, labels):
	predictions = model.predict(data)
	print (np.mean(predictions==labels)*100)
	return predictions


def trainSVM(data,labels):
        model=svm.SVC(kernel="rbf")
        model.fit(data, labels)
        return model

def testSVM(model,data,labels):
        predictions=model.predict(data)
        print (np.mean(predictions==labels)*100)
        return predictions

def trainDT(data,labels):
        model=tree.DecisionTreeClassifier()
        model.fit(data,labels)
        return model

def testDT(model,data,labels):
        predictions = model.predict(data)
        print (np.mean(predictions==labels)*100)
        return predictions


def trainNB(data,labels):
        model = GaussianNB()
        model.fit(data, labels)
        return model

def testNB(model,data,labels):
        predictions = model.predict(data)
        print (np.mean(predictions==labels)*100)
        return predictions

def main():
	trainData = []
	trainLabels = []
	testData=[]
	testLabels=[]

	t1Data = []
	t1Label = []
	
	vocab = SentiWords()
	emojis = getEmosentiment()
	Data = getTraindata(mode = "mp", emojis = emojis)
	#print (len(Data))


	TestData = getTestdata(search="sad", count=1,emojis = emojis)
	for i, sample in enumerate(TestData):
		t1Data.append(TestData[i].fvec)
		t1Label.appen(TestData[i].label)
	#print (TestData)

	for i, sample in enumerate(Data):
		trainData.append(Data[i].fvec)
		trainLabels.append(Data[i].label)
		#print (Data[i].fvec)
	print (len(trainData))
	datatrain,datatest,labelstrain,labelstest=train_test_split(trainData,trainLabels,test_size=0.2)
        
	#print (trainData[0])
	print ("Gaussian Mixture Analyzer")
	model = trainMP(datatrain, labelstrain, n_polarity = 4, n_epochs = 10)
	print("Accuracy")
	predictions = testMP(model,datatest, labelstest)


	print("SVM Analyzer")
	model=trainSVM(datatrain,labelstrain)
	print("Accuracy")
	predictions=testSVM(model,datatest,labelstest)


	print ("Decision Tree")
	model=trainDT(datatrain,labelstrain)
	print ("Accuracy")
	predictions = testDT(model,datatest,labelstest)

	
	print ("Naive Bayes")
	model=trainNB(datatrain,labelstrain)
	print ("Accuracy")
	predictions = testNB(model,t1Data,t1Label)


	

	

##	for i, sample in enumerate(TestData):
##		testData.append(TestData[i].fvec)
##		testLabels.append(TestData[i].label)
		#print (Data[i].fvec)	
main()
