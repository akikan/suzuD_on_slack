import tweepy
import libs.GenerateText as gt

CK = ""
CS = ""
AT = ""
AS = ""

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)
oneTime=""

def getTweet():
    tweets=api.user_timeline(screen_name = "",count =1)
    for tweet in tweets:
        text=tweet.text.replace('\n','')
    return text

def gene():
    generator = gt.GenerateText()
    generator.n = 1
    gen_txt = generator.generate()
    return gen_txt.encode('utf-8')

        
