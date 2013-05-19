import sys
import json
import operator

sent_dict = {}

def parse_sentiment_file(sent_file):
    for line in sent_file:
        sentiments = line.split("\t")
        sent_dict[sentiments[0]] = int(sentiments[1].replace("\n", ""))

def get_country_code(tweet):
    country_code = ""
    
    place = tweet.get('place')
    if not place is None:
        country_code = place.get('country_code')
        if country_code is None:
            country_code = ""
        
    return country_code

def get_state_code(tweet):
    state_code = ""
    
    place = tweet.get('place')
    if not place is None:
        full_name = place.get('full_name')
        if not full_name is None:
            full_name_list = full_name.split(", ")
            
            if len(full_name_list) > 1:
                state = full_name_list[1]
                state_list = state.split(" ")
                if len(state_list) > 1:
                    for i in state_list:
                        state_code += i[0]
                else:
                    state_code = state_list[0]
                
    return state_code 

def get_tweet_text(tweet): 
    text = tweet.get('text') 
    if text  is None:
        text = ""
        
    return text

def calc_tweet_sentiment(tweet_text):
    tweet_terms = tweet_text.split()
    
    sentiment = 0
    
    for term in tweet_terms:
        if sent_dict.has_key(term):
            sentiment = sentiment + sent_dict[term]
            
    return sentiment
    
def parse_tweet_file(tweet_file):
    
    state_dict = {}
    
    for line in tweet_file:
        tweet = json.loads(line)
        
        country_code = get_country_code(tweet)        
        
        if country_code == "US":
            state_code = get_state_code(tweet)
            if len(state_code) > 0:
                text = get_tweet_text(tweet)        
                sentiment = calc_tweet_sentiment(text)
                
                if state_dict.has_key(state_code):
                    state_dict[state_code] += sentiment
                else: 
                    state_dict[state_code] = sentiment
        
    sorted_dict = sorted(state_dict.iteritems(), key=operator.itemgetter(1))
        
    print sorted_dict[len(sorted_dict) - 1][0].encode('utf-8')

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    parse_sentiment_file(sent_file)
    parse_tweet_file(tweet_file)

if __name__ == '__main__':
    main()
