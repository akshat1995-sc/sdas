import requests
from bs4 import BeautifulSoup

from sdas.abstract import ArticleExtractor, soup
from sdas.base import ArticleData
from sdas.url_utils import check_valid_date_time_strings, check_valid_response

SEARCH_EXT = "/search?q="
BASE_URL = "https://www.ft.com"
DATE_SORTING = "&sort=date&isFirstView=true"
CONTENT_EXTRACTION_BASE_URL = "https://archive.is"


class FTArticleExtractor(ArticleExtractor):
    def __init__(self, article_url: str="", date_time_string: str=""):
        super().__init__(article_url)
        self.date_time_string = date_time_string
        
    def _get_article_date(self) -> str:
        date_stamp = self.date_time_string.split("T")[0]
        return date_stamp
    
    def _get_article_time(self)->str:
        time_stamp = self.date_time_string.split("T")[1]
        return time_stamp
    
    def _get_article_readable_url(self) -> str:
        archive_is_soup = soup(CONTENT_EXTRACTION_BASE_URL+"/"+self.article_url)
        main_html_content = archive_is_soup.find_all("div", {"class":"TEXT-BLOCK"})
        if not main_html_content: raise ValueError("No div class \"TEXT-BLOCK\" in archive is url!")
        readable_article_url = main_html_content[0].a['href']
        return readable_article_url
    
    def _get_article_text(self) -> str:
        readable_article_soup = soup(self._get_article_readable_url())
        article_body = readable_article_soup.find(id="article-body")
        if not article_body: raise ValueError("No article body in archive url!")
        text = "".join([div_element.text for div_element in article_body.find_all("div")])
        return text
    

def ft_article_urls(keyword: str)->list[tuple[str,str]]:
    page = requests.get(BASE_URL+SEARCH_EXT+keyword+DATE_SORTING)
    check_valid_response(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    return get_contents_date_time(soup)

def get_ft_articles(ft_article_contents:list[tuple[str,str]])->list[ArticleData]:
    article_generator = FTArticleExtractor()
    articles = []
    for ft_article_content in ft_article_contents:
        content, date_time_string = ft_article_content
        article_generator.article_url = content
        article_generator.date_time_string = date_time_string
        articles.append(article_generator.article_data)
    return articles

def get_contents_date_time(soup: BeautifulSoup)->list[tuple[str,str]]:
    contents = soup.find_all("div", {"class": "o-teaser__heading"})
    date_time_contents = soup.find_all("div", {"class":"o-teaser__timestamp"})
    check_valid_date_time_strings(date_time_contents)
    if not contents: raise ValueError("No ft article url in the soup!")
    date_time_strings = [date_time_content.time["datetime"] for date_time_content in date_time_contents]
    return [(BASE_URL+content.a["href"], date_time_string) for content, date_time_string in zip(contents, date_time_strings)]
