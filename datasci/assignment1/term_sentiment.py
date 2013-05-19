import sys
import json

scores = {}
tweets = []

def loadSentiments(_afinnfile):
	afinnfile = open(_afinnfile)
	
	for line in afinnfile:
		term, score  = line.split("\t")
		scores[term] = int(score)
		
	afinnfile.close()

def loadTweets(_tweetFile):
	tweetFile = open(_tweetFile);
	
	for tweetLine in tweetFile:
		tweet = json.loads(tweetLine)
		if "text" in tweet.keys():
			tweetText = tweet["text"].encode('utf-8')
			tweets.append(tweetText)

	tweetFile.close();

def calculateTweetSentiments():
	for tweet in tweets:
		tweetWords = tweet.split()
		tweetScore = 0
		for tweetWord in tweetWords:
			word = tweetWord.lower()
			if word in scores:
				tweetScore += scores[word]
			else:
				tweetScore += 0
		
		for tweetWord in tweetWords:
			wordScore = 0
			if word in scores:
				wordScore = scores[word]
			else:
				wordScore = float(tweetScore) / len(tweetWords)
			
			print tweetWord + " " + str(float(wordScore))

def main():
    loadSentiments(sys.argv[1])
    loadTweets(sys.argv[2])
    calculateTweetSentiments()
	
if __name__ == '__main__':
    main()
