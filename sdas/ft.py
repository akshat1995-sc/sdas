import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet

from sdas.base import ArticleData
from sdas.url_utils import check_valid_response

SEARCH_EXT = "/search?q="
BASE_URL = "https://www.ft.com"
DATE_SORTING = "&sort=date&isFirstView=true"
CONTENT_EXTRACTION_BASE_URL = "https://archive.is"

def get_articles(contents:ResultSet, time_stamps:ResultSet)->list[ArticleData]:
    article_list = []
    for content, time_stamp in zip(contents, time_stamps):
        extension_url = content.a['href']
        date_time_stamp = time_stamp.time['datetime']
        date_stamp = date_time_stamp.split("T")[0]
        time_stamp = date_time_stamp.split("T")[1]
        article_list.append(ArticleData(ft_url=BASE_URL+extension_url,
                                         date=date_stamp,
                                         time=time_stamp))
    return article_list

def get_ft_articles(keyword:str)->list[ArticleData]:
    page = requests.get(BASE_URL+SEARCH_EXT+keyword+DATE_SORTING)
    
    check_valid_response(page.status_code)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    contents = soup.find_all("div", {"class": "o-teaser__heading"})
    time_stamps = soup.find_all("div", {"class":"o-teaser__timestamp"})
    return get_articles(contents=contents, time_stamps=time_stamps)

def get_ft_article_readable_url(article_url: ArticleData)->str:
    session = requests.Session()
    page = session.get(CONTENT_EXTRACTION_BASE_URL+"/"+article_url.ft_url, headers={
            "User-Agent": "your bot 0.1"
        })
    check_valid_response(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    main_html_content = soup.find_all("div", {"class":"TEXT-BLOCK"})
    readable_article_url = main_html_content[0].a['href']
    return readable_article_url

def get_text_from_readable_url(readable_article_url:str)->str:
    session = requests.Session()
    page = session.get(readable_article_url, headers={
            "User-Agent": "your bot 0.1"
        })
    soup = BeautifulSoup(page.text, "html.parser")
    article_body = soup.find(id="article-body")
    text = "".join([div_element.text for div_element in article_body.find_all("div")])
    return text
