# AC209 class project

Using the sentiment of The Guardian business, politics and world news to forecast the UK/US exchange rate.

## Step 1: Data Collection:

We will collect the top 30 articles from The Guardian Api (data_collection/apireq.py) for each week between January 2000 and December 2016. 

News sections
- business and politics news
- world news filtered on articles that include the terms US, UK, or EU
