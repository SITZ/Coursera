import json,sys,collections
from collections import OrderedDict

tweet_file = open(sys.argv[1])

scores = {}

def main():
   wordsCount = 0.0

   for tweetText in tweet_file:
      tweet = json.loads(tweetText)
      
      if tweet.has_key("entities"):
         entities = tweet["entities"]
         hashtags = entities['hashtags']
         for hashtag in hashtags:
            token = hashtag['text']
            if token in scores:
               scores[token] = scores[token] + 1.0
            else:
               scores[token] = 1.0
      
   orderedScores = OrderedDict (collections.Counter(scores).most_common(10) )
   for token in orderedScores:
      print token + ' ' + str(orderedScores[token])

if __name__ == '__main__':
    main()
