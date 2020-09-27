import twitter
import json

consumer_key = 'lS9Sm8soUl23ArCmiXTB1B2vL'
consumer_secret = 'XIHU8Fb0T5WnP9iIhPMFeHcjsUIwqA0RY7zvAl0kgpbEfEwWcU'
access_token = '1306399984300949504-lEklM8nKguntBus1rJi7KgmXAa0pR1'
access_token_secret = 'DQFepnRMm0pCU52UJzm0eozC3Iknty9ePDrncoUDVP19C'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

tweet_filter = ['#ps5']
languages = ['en']


def main(FILTER, LANGUAGES):
    with open('output.txt', 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        print('ITS RUNNNING HELLO!!')
        count = 0
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            print('line')
            f.write(json.dumps(line))
            f.write('\n')
            
            #otherwise it goes on forever
            if count == 5:
                break
            count +=1
            