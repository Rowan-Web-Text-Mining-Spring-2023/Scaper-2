import snscrape.modules.twitter as sntwitter
import csv
from datetime import date
twitter_handles = ['Cristiano', 'alexmorgan13', 'CHARLESBARKLEY', 'terrellowens', 'thecooleyzone', 'RyanWhitney6', 'CaroWozniacki', 'ShawnJohnson', 'paulpierce34', 'AaronRodgers12', 'KimKardashian']
start = '2010-12-25'
end = date.today()
file = open('tweets.csv', 'a+', encoding='utf-8',newline='')
header = 'url,date,content,id,user,replyCount,retweetCount,likeCount,quoteCount,conversationId,lang,source,coordinates,\n'
file.write(header)
file.close()
for twitter_handle in twitter_handles:
    tweets = []
    print(twitter_handle)
    query = "(from:{}) until:{} since:{}".format(twitter_handle, end, start)
    limit = 200

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.url, tweet.date, tweet.content, tweet.id, tweet.user,  tweet.replyCount, tweet.retweetCount, tweet.likeCount,   tweet.quoteCount, tweet.conversationId, tweet.lang, tweet.source, tweet.coordinates])
        
    file = open('tweets.csv', 'a+', encoding='utf-8',newline='')
    with file:
        write = csv.writer(file)
        write.writerows(tweets)

print('Finished')