import csv
import pandas as pd

data = {}
with open('corpus_group_2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data[row['term']] = row['IDF']


file = open('tf_vectors_group_2.csv')
df = pd.read_csv(file)
for i in df.columns:
    df.update(df.filter(regex=i).mul(float(data.get(i))))
df.to_csv('tfidf_vectors_group_2.csv', index=False)