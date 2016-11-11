# AC209 class project

Using the sentiment of The Guardian business, politics and world news to forecast the UK/US exchange rate.

## Step 1: Data Collection:

We will collect the top 30 articles from The Guardian Api (data_collection/apireq.py) for each week between January 2000 and December 2016.

News sections
- business and politics news
- world news filtered on articles that include the terms US, UK, or EU

Other things to consider:
- look at the uk vs us edition of the guardian
- extract the tags for each article and see if they can be used as labels
- data from tables/figures in the articles
- sentiment of specific authors
-  keywords

## Step 2: Filter relevant articles

#### To DO

* [ ] List of relevant words
* [ ] Relevant economic phrases for classifying as positive/negative
* [ ] Senti-word net model

First filter on relevance to us/uk exchange rate

#### Naive approach
- Vectorise articles
- Filter articles for relevance - if n of the relevant words are present in the article - mark as relevant
- Out of relevant articles get sentiment scores by scoring using sentiword net
- average sentiment score for each week
- plot sentiment score vs time

- consider each section separately

#### Improvements:

- Look at co-occurence of words

## Step 3: Sentiment Analysis of relevant articles

Senti word net score - positive/negative + plot
  - break down by business, politics and world
  - list of common positive and common negative words in each section
  - focus on times of crisis and see if score becomes more variable
  - difference in scores from taking 10 articles per week to 30 articles
  - error measurements - standard error measurements

## Step 4: Clustering

- remove stop words
- stem algorithm


- relevant words? - determine this

- bag of words model 


- partial least squares
- synsets based on context
- phrases/tokens

- classify words as noun/adjectives - use unsupervised split between adjectives to classify as positive/negative
