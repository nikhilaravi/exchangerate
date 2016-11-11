from bs4 import BeautifulSoup

def article_text(article):
    soup = BeautifulSoup(article, "lxml")
    return soup.get_text()


apiKey = 'becada9b-4794-4a99-a249-5c47d9c9d36a'

# format the url for the request
def makeurl(options):
    base = 'http://content.guardianapis.com/search?&api-key=' + apiKey + '&show-most-viewed=True&show-fields=headline%2Cbody&page-size=50';

    if options['startDate']:
        base = base + '&from-date=' + str(options['startDate'])
    if options['endDate']:
        base = base + '&to-date=' + str(options['endDate'])
    if options['section']:
        base = base + '&section=' + options['section']
    if options.get('query'):
        base = base + '&q=' + options['query']

    return base;
