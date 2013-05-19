import sys
import json

stateScores = {}

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
		
		if tweet['lang'] is None:
			continue
		tweetLanguage = tweet['lang'].encode('utf-8')
		if tweetLanguage.lower() != 'en':
			continue

		if tweet['place'] is None:
			continue
		_tweetState = tweet['place']['full_name'].encode('utf-8').split()
		print _tweetState

		if tweet['text'] is None:
			continue;
		tweetText = tweet["text"].encode('utf-8')
		
		stateScore[tweetState] += calculateTweetSentiment(tweetText)

	tweetFile.close();

def calculateTweetSentiment(tweet):
	tweetScore = 0
	for tweetWord in tweet.split():
		word = tweetWord.lower()
		if word in scores:
			tweetScore += scores[word]
		else:
			tweetScore += 0
	
	return float(tweetScore)

def printHappiestState():
	return 0

def main():
    loadSentiments(sys.argv[1])
    loadTweets(sys.argv[2])
    
    printHappiestState()
	
if __name__ == '__main__':
    main()
