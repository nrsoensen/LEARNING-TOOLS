import json
from textblob import TextBlob
import matplotlib.pyplot as plt

twitterPolarityList = []
subjectivityList = []

def avgPolarity(tweetData, tb):
    sum = []
    for i in range(len(tweetData)):
        sum.append(tb.polarity)
    final = 0
    for i in range(len(sum)):
        final = final + sum[i]
    final = final / (len(sum))
    print("\n", final, "\n")

def avgSubjectivity(tweetData, tb):
    sum = []
    for i in range(len(tweetData)):
        sum.append(tb.subjectivity)
    final = 0
    for i in range(len(sum)):
        final = final + sum[i]
    final = final / (len(sum))
    print("\n", final, "\n")

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

for i in range(len(tweetData)):
    print("\n" + tweetData[i]['text'] + "\n")
    tb = TextBlob(tweetData[i]['text'])
    print(tb.polarity)
    print(tb.subjectivity)
    twitterPolarityList.append(tb.polarity)
    subjectivityList.append(tb.subjectivity)

avgPolarity(tweetData, tb)
avgSubjectivity(tweetData, tb)

# Continue your program below!
plt.title("Twitter Histogram")
plt.hist(twitterPolarityList, bins=[-1,-.6,-.2,.2,.6,1])
plt.xlabel("Polarity")
plt.ylabel("Frequency")
plt.axis([-1.1,1.1,0,65])
plt.grid(True)
#plt.show()

plt.title("Twitter Scattergram")
plt.plot(twitterPolarityList, subjectivityList, 'ro')
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.axis([-1.1,1.1,-.1,1.1])
plt.grid(True)
plt.show()
# Textblob sample:
