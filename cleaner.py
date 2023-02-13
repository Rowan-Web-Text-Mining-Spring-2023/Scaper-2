import contractions
import csv
import re
import demoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from unicodedata import normalize

#Remove new lines from text
def remove_new_lines(value):
    return ''.join(value.splitlines())

nltk.download('stopwords')
nltk.download('punkt')
stops_en = set(stopwords.words('english'))   #list of stopwords

#Adding extra stopwords
with open('new_stops.txt') as file:
    for line in file:
        stops_en.add(line.strip())

#Remove stopworsd from sentence
def remove_stopwords(value):
    remove_stops = ''
    words = word_tokenize(value)
    for word in words:
        if(word not in stops_en): 
            remove_stops = remove_stops + word + ' '
    return remove_stops

many = []    #List to store all tweets after cleaning
#Loop through all tweets in csv file
with open('tweets.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    #Checking line by line
    for row in reader:
        new_row = []

        #Checking each element of line
        i = 0
        for item in row:
            item = remove_new_lines(item)    #removes new lines in text
            item = item.lower()    #lowercases text
            item = contractions.fix(item)    #removes contractions
            item = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'xxhyperlink', item)     #removes hyperlinks
            item = demoji.replace(item, "")      #removes emojis
            item = re.sub(r'@[A-Za-z0-9_]+', 'xxhandle', item)     #removes @handles
            if(i == 2):   #Only removes stopwords in content
                item = remove_stopwords(item)
                t = normalize('NFKD', item).encode('ascii', 'ignore')
                item = t.decode()
            new_row.append(item)
            i = i + 1
        many.append(new_row)

#Writes clean data to separate csv file
with open('cleaned.csv', 'w', newline='', encoding='utf-8') as clean:
    writer = csv.writer(clean)
    writer.writerows(many)


