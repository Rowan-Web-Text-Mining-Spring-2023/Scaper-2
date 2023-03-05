import csv
import math

#Grab content from tweets column
data = []
with open('cleaned_tweets_group_2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append((row['content ']))

#Add words to map
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

with open('corpus_group_2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['term', 'occurrences', 'IDF'])
    w.writerows(c)

