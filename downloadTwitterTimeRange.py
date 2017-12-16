# This Python file uses the following encoding: utf-8
#!/usr/bin/python

from twitter import *
from datetime import datetime, timedelta, date
import re


def isInsideTimeRange(timestamp, startTimestamp, endTimestamp):
  actual = datetime.strptime(timestamp,'%a %b %d %H:%M:%S +0000 %Y')
  start = datetime.strptime(startTimestamp,'%Y-%m-%d')
  end = datetime.strptime(endTimestamp,'%Y-%m-%d')
  
  return (start <= actual and actual < end)

# === main ===
USER='yruewbnwkjewjk'
START='2017-07-01'
END='2018-12-01'

MAX_ITERATIONS=50
consumer_key='mAkPqcrlGxNwgeXN7S3A1F86K'
consumer_secret='SKfiwQdmGPwZaSW4rcurlL617SjuChzs2O8eRQWHYTeq3cFICC'
access_token_key='16560104-iljkmaSiy28ZTUr41DoJqpNWVZQhNfYMES7t3d0XF'
access_token_secret='2NCObRK52TLmlgDg5uSaX8YAeW2RXsUbnbTnI0NFqHOfa'
twitter = Twitter(auth = OAuth(access_token_key, access_token_secret, consumer_key, consumer_secret))

lastId = None
matchingTweets = []
for i in range(0,MAX_ITERATIONS):
  if lastId:
    statuses = twitter.statuses.user_timeline(screen_name = USER, count = 200, max_id=lastId, tweet_mode="extended")
  else:
    statuses = twitter.statuses.user_timeline(screen_name = USER, count = 200, tweet_mode="extended")
  if len(statuses) == 1:
    break

  for status in statuses:
      lastId = status["id"]
      timestamp = datetime.strptime(status["created_at"],'%a %b %d %H:%M:%S +0000 %Y')
      if isInsideTimeRange(status["created_at"], START, END):
        matchingTweets.append("{} {}".format(timestamp.strftime('%Y-%m-%d %H:%M'), status["full_text"].strip()))  

matchingTweets.reverse()
message = ""
for line in matchingTweets:
    message = message + line + "\n\r"
print(message)
print(len(matchingTweets))
