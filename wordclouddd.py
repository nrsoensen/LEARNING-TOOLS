import json
from textblob import TextBlob
import matplotlib.pyplot as plt
#from os import path
#from PIL import Image
#import numpy as np
#import os
from wordcloud import WordCloud

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#book = np.array(Image.open(path.join(d, "book.png")))

#combine all the tweet texts
combinedTweets = ""
for tweet in tweetData:
    combinedTweets += tweet['text']

#print(combinedTweets)
tweetblob = TextBlob(combinedTweets)

wordsToFilter = ["https","automation","the","will","could","about","thing",
    "randazzoj","potential","media","million"]

filterList = []
for word in tweetblob.words:
    if len(word) < 3:
        continue
    if not word.isalpha():
        continue
    if len(word) <5 and word.upper() != word:
        continue
    if word.lower() in wordsToFilter:
        continue
    if word.lower() in filterList:
        continue
    filterList.append((word.lower(), tweetblob.word_counts[word.lower()]))

wordcloud = WordCloud().generate_from_frequencies(filterList)
#wordcloud.to_file(path.join(d, "book.png"))
plt.imshow(wordcloud, interpolation='bilinear')
#plt.imshow(book, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
