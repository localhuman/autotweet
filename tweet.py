CONSUMER_KEY='ZY3CXmGniHPKEAlKOh2OZGo7J'
CONSUMER_SECRET='8kKtLys4w8hFyuHJ5264yFQeAg41hsRI8LeoR74dRtK86KNhAt'

ACCESS_TOKEN='262477584-tCdov8hglXcRTMeN4YbrajYM6rb2wkquK45S55MO'
ACCESS_TOKEN_SECRET='p2oSU6Df8Qo3XmKTWIpV34wtLoWpuuy2f6J6BAOEKKINo'

GOOGLE_CIVIC_KEY='AIzaSyBvjN5FXsasaF16qt6yCeh4OFY57h4RXxY'

MARGIN = 2150000


import twitter
import pprint
import random
import time
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)


#statuses = api.GetUserTimeline(screen_name='albertcamoo')


def dotweet(margin):
    #pprint.pprint([s.text for s in statuses])
    margin += random.randint(100,200)
    tweets = [
        "@realDonaldTrump has lost the popular vote to @HillaryClinton by %s votes" % margin,
        "word on the street is @realDonaldTrump actually lost WI and MI, we'll see about PA",
        "@realDonaldTrump is poopy.  trumpispoopy.com",
        "Can this be happiness, this terrifying freedom?",
        "Real generosity toward the future lies in giving all to the present",
        "There is always a philosophy for lack of courage.",
        "@realDonaldTrump if i were you i would hate to be alone",
        "@realDonaldTrump how many million good men and women have died to secure the freedoms you are shitting upon?",
    ]

    tweet = random.choice(tweets)
    result = api.PostUpdate(tweet)
    pprint.pprint( result )

    time.sleep(3600)
    dotweet(margin)


dotweet(MARGIN)