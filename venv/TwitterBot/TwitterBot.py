import tweepy
import time

auth = tweepy.OAuthHandler('v4onB22K53ax6BPMHzKNdDo9d', 'JZNwOuIy2WHpryh2IJAbAQiMTSkW9Gp8etm8KIieDYv0p1JyEp')
auth.set_access_token('1169128027080601603-se51n7Zs0zkMCfyNsqFlf1ViAZr86Z', 'rDkPXIVAFOtViBa80OcfzRhOmf91t1uQfv1aMNUbUm8LH')

api = tweepy.API(auth)

usersData = api.me()

def limit_handle(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

#Genrous Bot
#this bot is used to follow back the person who follows you
# for follower in limit_handle(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'AMAN SINGHAL':
#         follower.follow()
#         break
#     print(follower.name)

print(api.me().name)
searchString = 'I see you'
numbersOfTweets = 1

for tweet in tweepy.Cursor(api.search,searchString).items(numbersOfTweets):
    try:
        tweet.retweet()
        print("I like the tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
