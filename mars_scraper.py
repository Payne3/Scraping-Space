
import pymongo
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_scrape
collection = db.stats

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def headlines():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain book information
    articles = soup.find_all('div', class_='content_title')


    for article in articles:
#  Use Beautiful Soup's find() method to navigate and retrieve attributes
         
        link = article.find('a')
        href = link['href']
    
    browser.quit()

    # Return results
    return href

def images():
    browser = init_browser()
    url_1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_1)

    # HTML object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    image_finder = soup.find("footer" )   

    browser.quit()

    return image_finder


def tweet():
    browser = init_browser()
    url_3 ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    timeline = soup.find_all('ol', class_= "stream-items")
    tweets = soup.find('p', class_='tweet-text').text
    

    browser.quit()
    return tweets

def tables():
    browser = init_browser()
    url_4 = "https://space-facts.com/mars/"
    browser.visit(url_4)

    tables = pd.read_html(url_4)

    df = tables[0]

    html_table = df.to_html()

    browser.quit()

    return html_table

    