import pandas as pd
import numpy as np
import csv
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime as dt
import time

# Generating datetime
from datetime import datetime, timedelta
now = datetime.now()
now = now.strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(days = 400)
yesterday = yesterday.strftime('%Y-%m-%d')

keyword = input('Enter a topic or keyword, please:')




#Open/create a file to save data
csvFile = open(keyword +'-scrape-' + now + '.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet',])


for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:id since:' +  yesterday + ' -filter:links -filter:replies').get_items()):
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()
