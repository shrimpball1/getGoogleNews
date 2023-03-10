import ssl
import urllib.request

from bs4 import BeautifulSoup

def get_google_news(xml_news_url, counter):

# Set up SSL context to handle https requests
    context = ssl._create_unverified_context()

# Open connection and read in response from xml_news_url
    with urllib.request.urlopen(xml_news_url, context=context) as response:
        xml_page = response.read()

# Parse xml_page using lxml tree builder
    soup_page = BeautifulSoup(xml_page, "lxml")

# Find all news items on the page
    news_list = soup_page.find_all("item")

# Print the details of the news items
    for i, news in enumerate(news_list):
        print(f"News Title: {news.title.text}")
        print(f"News Link: {news.link.text}")
# Ignore the news without data
        if not news.pubDate:
            continue

        print(f"Published Date: {news.pubDate.text}")
        print("+-" * 20, "\n")

        if i == counter:
            break


if __name__ == '__main__':
    news_url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
    sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"
    get_google_news(news_url, 10)
    get_google_news(sports_url, 5)
