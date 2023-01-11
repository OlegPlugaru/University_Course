import tweepy

# Authenticate using the keys and tokens
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create an API client
api = tweepy.API(auth)

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1):
        break
    friends = api.friends(acct, count=5)
    for friend in friends:
        print(friend.screen_name)
        print(friend.status.text[:50])