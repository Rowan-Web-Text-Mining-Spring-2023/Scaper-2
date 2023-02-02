import snscrape.modules.twitter as sntwitter
import csv
from datetime import date

#Scrape data from following handles
twitter_handles = ['Cristiano', 'alexmorgan13', 'CHARLESBARKLEY', 'terrellowens', 'thecooleyzone', 'RyanWhitney6', 'CaroWozniacki', 'ShawnJohnson', 'paulpierce34', 'AaronRodgers12', 'KimKardashian']

#Define dates to look for tweets through
start = '2010-12-25'
end = date.today()

#Adding the heading to csv file
file = open('tweets.csv', 'a+', encoding='utf-8',newline='')
header = 'url,date,content,id,user,replyCount,retweetCount,likeCount,quoteCount,conversationId,lang,source,coordinates,\n'
file.write(header)
file.close()

#Go through each twitter user
for twitter_handle in twitter_handles:
    tweets = []
    print(twitter_handle)   #Print current handle gathering tweets for
    query = "(from:{}) until:{} since:{}".format(twitter_handle, end, start)
    limit = 200            #Max 200 tweets to grab

    #Check to see if limit of tweets is reached, otherwise takes required data from tweet
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.url, tweet.date, tweet.content, tweet.id, tweet.user,  tweet.replyCount, tweet.retweetCount, tweet.likeCount,   tweet.quoteCount, tweet.conversationId, tweet.lang, tweet.source, tweet.coordinates])
    
    #Adding all the tweet data to the csv file
    file = open('tweets.csv', 'a+', encoding='utf-8',newline='')
    with file:
        write = csv.writer(file)
        write.writerows(tweets)

print('Finished')