import contractions
import csv
import re
import demoji

def remove_new_lines(value):
    return ''.join(value.splitlines())

many = []    #List to store all tweets after cleaning
#Loop through all tweets in csv file
with open('tweets.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    #Checking line by line
    for row in reader:
        new_row = []

        #Checking each element of line
        for item in row:
            item = remove_new_lines(item)    #removes new lines in text
            item = item.lower()    #lowercases text
            item = contractions.fix(item)    #removes contractions
            item = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'xxhyperlink', item)     #removes hyperlinks
            item = demoji.replace(item, "")      #removes emojis
            item = re.sub(r'@[A-Za-z0-9_]+', 'xxhandle', item)     #removes @handles
            new_row.append(item)
        print(new_row)
        many.append(new_row)

#Writes clean data to separate csv file
with open('cleaned.csv', 'w', newline='', encoding='utf-8') as clean:
    writer = csv.writer(clean)
    writer.writerows(many)


