import csv
import math
import pandas as pd
import numpy as np
import collections
from sklearn.feature_extraction.text import CountVectorizer

#Grab content from tweets column
data = []
with open('cleaned_tweets_group_2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append((row['content ']))

#Add words to map
#If word not in map, adds to map and the doc number that it occurs in to a list
#If word is in map, adds the doc number it occured in to list with other occurrences
DF = {}
for i in range(len(data)):
    tokens = data[i].split()
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}

#Number of words in corpus
corpus_len = len(DF)

#Convert occurrence positions into len of occurrences
for i in DF:
    DF[i] = len(DF[i])
only_words = [x for x in DF]

#Put each word, occurence, and idf in one element together
c = []
for i in range(corpus_len):
    tmp = []
    tmp.append(only_words[i])
    matches = DF.get(only_words[i])
    tmp.append(matches)
    num = pow((math.log(corpus_len/matches)), 2)
    tmp.append(num)
    c.append(tmp)

#Save corpus
with open('corpus_group_2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['term', 'occurrences', 'IDF'])
    w.writerows(c)


#Selecting docs for tf-idf vectors, semi random, selected to have some commonality, but not much
to_tfidf = []
to_tfidf.extend((data[1813], data[2271], data[1358], data[114], data[2956], data[4838], data[5000], data[1325], data[5451], data[5732]))

#Perform a 'bag of words' on the selected docs
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(to_tfidf)
vector = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

#Save tfidf vectors
vector.to_csv('tf_vectors_group_2.csv', index=False)