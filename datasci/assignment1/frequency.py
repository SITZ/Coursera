import sys
import json

globalFrequency = {}
tweets = []

def loadTweets(_tweetFile):
	tweetFile = open(_tweetFile);
	
	for tweetLine in tweetFile:
		tweet = json.loads(tweetLine)
		if "text" in tweet.keys():
			tweetText = tweet["text"].encode('utf-8')
			tweets.append(tweetText)

	tweetFile.close();

def computeTermFrequencies():
	for tweet in tweets:
		tweetWords = tweet.split()
		for tweetWord in tweetWords:
			word = tweetWord.lower()
			if word in globalFrequency.keys():
				++globalFrequency[word]
			else:
				globalFrequency[word] = 1
	
	for tweet in tweets:
		tweetWords = tweet.split()	
		localFrequency = {}
		for tweetWord in tweetWords:
			word = tweetWord.lower()
			if word in localFrequency.keys():
				++localFrequency[word]
			else:
				localFrequency[word] = 1
		
		for word in localFrequency.keys():
			print word + " " + str(float(localFrequency[word]) / float(globalFrequency[word]))

def main():
    loadTweets(sys.argv[1])
    computeTermFrequencies()
	
if __name__ == '__main__':
    main()
