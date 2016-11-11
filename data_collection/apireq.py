import requests, json
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
from dateutil.parser import *
import datetime
import os
from helpers import article_text, makeurl
import pandas as pd
import numpy as np

before=datetime.datetime(2000,1,1) # start year 2000
after=datetime.datetime(2016,10,31) # end year 2016 (october)

findMondays = rrule.rrule(rrule.WEEKLY,byweekday=relativedelta.MO,dtstart=before) # function to find all the monday dates
findSundays = rrule.rrule(rrule.WEEKLY,byweekday=relativedelta.SU,dtstart=before) # function to find all the sunday dates

startDates =  [date.date() for date in findMondays.between(before,after,inc=True)] # find all the monday dates between the start and end year
endDates =  [date.date() for date in findSundays.between(before,after,inc=True)] # find all the sunday dates between the start and end year

# sections of the api which we want to query
sections = ['business', 'politics', 'world', 'uk-news']

columns=['Year', 'Week Start', 'Week End', 'Section', 'Number', 'Headline', 'Body Text']
article_db = pd.DataFrame(columns=columns)

# iterate through all the weeks
for week in range(807,len(startDates)-1):

    startDate = startDates[week]
    endDate = endDates[week+1]

    print 'Year: ', startDate.year, '   Week Beginning', startDate

    # loop through the sections
    for section in sections:

        # create options object
        options = {}
        options['startDate'] = startDate
        options['endDate'] = endDate
        options['section'] = section
        if section == 'world':
            options['query'] = 'us%20OR%20uk%20OR%20eu'

        # make the request after formatting the url with the correct query parameters
        req = requests.get(makeurl(options))
        # turn response into json
        jtext = json.loads(req.text)
        response = jtext.get('response')

        # extract the array of articles
        articles = response.get('results')

        # print 'Num articles in section: ', section, response['pageSize']*response['pages']

        # iterate through the first 30 articles
        for num, article in enumerate(articles[0:30]):
            # get the body text of the article
            body = article['fields']['body']
            headline = article['fields']['headline']
            # convert the body html to a string
            bodyHTML = str(body.encode("utf-8"))
            # extract text from html
            bodyText = article_text(body).encode("utf-8")
            headlineText = article_text(headline).encode("utf-8")

            # create a row of data to append to DF
            row = np.reshape([startDate.year, startDate, endDate, section, num, headlineText, bodyText], (1,7))

            article_df = pd.DataFrame(row, columns=columns)
            # article_db = article_db.append(article_df)

            with open('./articles/articles_db.csv', 'a') as f:
                article_df.to_csv(f, header=False)
