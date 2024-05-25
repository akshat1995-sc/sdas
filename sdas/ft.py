import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag

from sdas.base import ArticleLinks

SEARCH_EXT = "/search?q="
BASE_URL = "https://www.ft.com"

def get_articles(contents:ResultSet, time_stamps:ResultSet)->list[ArticleLinks]:
    article_list = []
    for content, time_stamp in zip(contents, time_stamps):
        extension_link = content.a['href']
        date_time_stamp = time_stamp.time['datetime']
        date_stamp = date_time_stamp.split("T")[0]
        time_stamp = date_time_stamp.split("T")[1]
        article_list.append(ArticleLinks(link=BASE_URL+extension_link,
                                         date=date_stamp,
                                         time=time_stamp))
    return article_list

def get_ft_article_links(keyword:str)->list[ArticleLinks]:
    page = requests.get(BASE_URL+SEARCH_EXT+keyword)
    
    if not page.status_code==200:
        raise ValueError("Search result not obtained!")
    
    soup = BeautifulSoup(page.text, 'html.parser')
    contents = soup.find_all("div", {"class": "o-teaser__heading"})
    time_stamps = soup.find_all("div", {"class":"o-teaser__timestamp"})
    return get_articles(contents=contents, time_stamps=time_stamps)