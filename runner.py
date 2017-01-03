from importlib import reload
import tweepy
import strings_fns
reload(strings_fns)


# twitter API credentials
consumer_key = "2ftokUvglAwe4fO3kZfw5VaNM"
consumer_secret = "1OQSPZEZkcYM0UDdXItpv3buN4VCnAXx4DjeLl6JAiWcH6Gf6e"
access_key = "3142721558-1Km65GNsIwAEMFRUkxM7VneJovczwBjZNu3JcQk"
access_secret = "M1m9vcxU2K1T1CPIwX3tlrFLgq8LrtUzDaGebOZOMiJHR"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
screen_name = '361Capital'
new_tweets = api.user_timeline(screen_name=screen_name, count=20)

s = 'Summit Global Invest @SummitLowVol 2 Dec 2015\nWe understand the hard work and long hours it takes \
to build your savings and investments. Find out how we can help: http://summitglobalinvestments.com/individual_\
investors.html …\nReply\nRetweet\nLike\nMore'

s1 = 'Summit Global Invest @SummitLowVol 1 Dec 2015\nDave Harden, managing partner and CIO at SGI, examines \
the risk factors primed to impact the markets in 2016\nReply\nRetweet\n1\nLike\n3\nMore'

retweeets = strings_fns.strToInt(strings_fns.find_between(s1, 'Retweet\n', 'Like'))
likes = strings_fns.strToInt(strings_fns.find_between(s1, 'Like\n', 'More'))

temp1 = isinstance(retweeets, int)
temp2 = isinstance(likes, int)
print("retweets: " + retweeets + "likes: " + likes)