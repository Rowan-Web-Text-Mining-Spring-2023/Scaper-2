import contractions
import csv
import re

#Removes any emoji, takes arg(str)
def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)

many = []    #List to store all tweets after cleaning
#Loop through all tweets in csv file
with open('tweets.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    #Checking line by line
    for row in reader:
        new_row = []

        #Checking each element of line
        for item in row:
            item = item.lower()    #lowercases text
            item = contractions.fix(item)    #removes contractions
            item = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'xxhyperlink', item)     #removes hyperlinks
            item = remove_emojis(item)      #removes emojis
            item = re.sub(r'@[A-Za-z0-9]+', 'xxhandle', item)     #removes @handles
            new_row.append(item)
        print(new_row)
        many.append(new_row)

#Writes clean data to separate csv file
with open('cleaned.csv', 'w', newline='', encoding='utf-8') as clean:
    writer = csv.writer(clean)
    writer.writerows(many)


