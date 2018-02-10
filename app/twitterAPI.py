import tweepy, json

consumer_key = "RlyqnXdvGyRPI65bFFbRAFW6F"
consumer_secret = "cwF5FzqikYDVoddjNnwaaLwIvFLqFvjFboGcYK0gO4IR9CUumZ"
access_token = "4806032416-ywmR2ri9kjvB6q9tH0UeCDMD7fehmlyCOHynSOe"
access_token_secret = "CRufuaJOZUEpkAWpILkhDMuMM1WQybVC1bnwe24bflSYH"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(lat, long, radius):
    geo = str(lat) + "," + str(long) + "," + str(radius) + "mi"
    results = tweepy.Cursor(api.search, q="#NowPlaying",geocode=geo).items(100000)
    count = 0
    retVal = []
    for result in results:
        retVal.append(result.text)
    return retVal
'''
def trends(id=2473224):
    result = api.trends_place(id)
    strform = ''.join(result)
    output = (json.loads(strform))['name']
    print (output)
'''
def by_hashtag(lat, long, radius, hashtag):
    tag = tweepy.Cursor(api.search, q='')

if __name__ == '__main__':
    get_tweets(lat=40.4415719, long=-80.0100425)
