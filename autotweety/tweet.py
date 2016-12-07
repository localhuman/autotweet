
from env import *
import twitter
import pprint
import random
import time
from multiprocessing import Process

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)



def dotweet():
    epoch = int(time.time())
    margin_add = int(( epoch -1480344915 ) / 60.0 )
    margin = 2700000 + margin_add

    tweets = [
        ".@realDonaldTrump has lost the popular vote to @HillaryClinton by %s votes" % margin,
        "word on the street is @realDonaldTrump actually lost WI and MI, we'll see about PA.  lost by %s" % margin,
        ".@realDonaldTrump is poopy. trumpispoopy.com. lost by %s" % margin,
        "Can this be happiness, this terrifying freedom? @realDonaldTrump lost by %s votes" % margin,
        "Real generosity toward the future lies in giving all to the present.  @realDonaldTrump lost by %s votes" % margin,
        "There is always a philosophy for lack of courage. @realDonaldTrump lost by %s votes" % margin,
        ".@realDonaldTrump if i were you i would hate to be alone. Lost by %s votes" % margin,
        ".@realDonaldTrump how many million good men and women have died to secure the freedoms you are shitting upon? Lost by %s votes" % margin,
	".@realDonaldTrump delete yur account. lost by %s votes" % margin,
	".@realDonaldTrump lost by %s votes. sad!" % margin,
	"In the depth of winter, I finally learned that within me there lay %s votes that @realDonaldTrump lost by" % margin,
	"I shall tell you a great secret, @realDonaldTrump. Do not wait for the last judgment, you have already lost by %s votes" % margin,
	".@readDonaldTrump, Nobody realizes that some people expend tremendous energy merely to lose by %s votes." % margin
    ]

    tweet = random.choice(tweets)
    result = api.PostUpdate(tweet)
    pprint.pprint( result )
    time.sleep(3600)
    dotweet()


tweeting = Process(target=dotweet, args=())
tweeting.start()
