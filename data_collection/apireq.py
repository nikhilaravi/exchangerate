import requests, json
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
from dateutil.parser import *
import datetime
import os

before=datetime.datetime(2000,1,1) # start year 2000
after=datetime.datetime(2010,12,31) # end year 2010

findMondays = rrule.rrule(rrule.WEEKLY,byweekday=relativedelta.MO,dtstart=before) # function to find all the monday dates
findSundays = rrule.rrule(rrule.WEEKLY,byweekday=relativedelta.SU,dtstart=before) # function to find all the sunday dates

startDates =  [date.date() for date in findMondays.between(before,after,inc=True)] # find all the monday dates between the start and end year
endDates =  [date.date() for date in findSundays.between(before,after,inc=True)] # find all the sunday dates between the start and end year

# sections of the api which we want to query
sections = ['business', 'politics', 'world', 'uk-news']

apiKey = '74b9c625-6033-46be-b0e6-7b020a1f4d15'

# format the url for the request
def makeurl(options):
    base = 'http://content.guardianapis.com/search?&api-key=' + apiKey + '&show-most-viewed=True&show-fields=body&page-size=50';

    if options['startDate']:
        base = base + '&from-date=' + str(options['startDate'])
    if options['endDate']:
        base = base + '&to-date=' + str(options['endDate'])
    if options['section']:
        base = base + '&section=' + options['section']
    if options.get('query'):
        base = base + '&q=' + options['query']

    print 'requesting url: ', base

    return base;

# iterate through all the weeks
for week in range(len(startDate)):

    # loop through the sections
    for section in sections:

        # create options object
        options = {}
        options['startDate'] = startDates[week]
        options['endDate'] = endDates[week+1]
        options['section'] = section
        if section == 'world':
            options['query'] = 'us%20OR%20uk%20OR%20eu'

        # make the request after formatting the url with the correct query parameters
        r = requests.get(makeurl(options))

        # turn response into json
        jtext = json.loads(r.text)
        response = jtext['response']

        # extract the array of articles
        articles = response['results']

        print 'Num articles in section: ', section, response['pageSize']*response['pages']

        # iterate through the first 30 articles
        for num, article in enumerate(articles[0:30]):
            # get the body text of the article
            body = articles[0]['fields']['body']
            # format the file name of the format: article/weekbeg/section/number.html

            filename = 'articles/' + str(startDates[week]) + '/' + str(section) + '/' + str(num) + '.html'

            # check if the folder and file exist or create it if not
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

            # open the file
            f = open(filename, 'w')
            # convert the body html to a string
            bodyText = str(body.encode("utf-8"))
            # write the html to the file
            f.write(bodyText)
