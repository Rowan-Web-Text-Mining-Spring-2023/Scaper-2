import csv
import pandas as pd
import datetime
import os

dir = 'all_tweets'
names = []
for file in os.listdir(dir):
    names.append(file)
    df = pd.read_csv('all_tweets/'+file)
    df2 = df.rename(columns = {'language': 'lang', 'replies': 'replycount', 'retweets': 'retweetcount', 'likes': 'likecount', 'quotes': 'quotecount', 'tweets': 'content', 'tweet': 'content'})
    df2.columns = df2.columns.str.lower()
    df2.columns = df2.columns.str.replace(' ', '')
    df2.to_csv('all_tweets/'+file, index = False)



li = []

for filename in names:
    df = pd.read_csv('all_tweets/'+filename, index_col=None, header=0, parse_dates=True, infer_datetime_format=True)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
frame.drop(frame.columns[frame.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
frame.to_csv('all_tweets_group_2.csv', index=False)