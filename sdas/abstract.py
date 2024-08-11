from abc import ABC, abstractmethod

import requests
from time import sleep
from bs4 import BeautifulSoup

from sdas.base import ArticleData
from sdas.url_utils import check_valid_response


class ArticleExtractor(ABC):
    
    def __init__(self, article_url: str):
        self.article_url = article_url
        
    def _get_article(self)->ArticleData:
        return ArticleData(original_url=self.article_url,
                           date=self._get_article_date(),
                           time=self._get_article_time(),
                           readable_url=self._get_article_readable_url(),
                           text_data=self._get_article_text())
    
    @abstractmethod
    def _get_article_date(self)->str:
        pass
    
    @abstractmethod
    def _get_article_time(self)->str:
        pass
    
    @abstractmethod
    def _get_article_text(self)->str:
        pass
    
    @abstractmethod
    def _get_article_readable_url(self)->str:
        pass
    
    @property
    def article_soup(self)->BeautifulSoup:
        return soup(self.article_url)
        
    @property
    def article_data(self)->ArticleData:
        if not self.article_url:
            raise ValueError("No article url provided. Please set the article url!")
        return self._get_article()

def soup(url):
    session = requests.session()
    sleep(2)
    page = session.get(url, headers={"User-Agent":"your bot 0.1"})
    check_valid_response(page.status_code)
    return BeautifulSoup(page.text, "html.parser")
        
    