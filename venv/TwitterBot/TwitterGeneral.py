import tweepy

auth = tweepy.OAuthHandler('v4onB22K53ax6BPMHzKNdDo9d', 'JZNwOuIy2WHpryh2IJAbAQiMTSkW9Gp8etm8KIieDYv0p1JyEp')
auth.set_access_token('1169128027080601603-se51n7Zs0zkMCfyNsqFlf1ViAZr86Z', 'rDkPXIVAFOtViBa80OcfzRhOmf91t1uQfv1aMNUbUm8LH')

api = tweepy.API(auth)

usersData = api.me()

print(usersData.name) #print Name
print(usersData.screen_name) #print account name
print(usersData.followers_count) #get followers Count
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)