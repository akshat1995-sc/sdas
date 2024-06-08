import pytest

from sdas.base import ArticleData
from sdas.ft import ft_article_urls, get_ft_articles
from sdas.url_utils import get_readable_url_code

KEYWORD = "gold"

    
@pytest.fixture
def article()->ArticleData:
    article_urls = ft_article_urls(KEYWORD)
    return get_ft_articles([article_urls[0]])[0]

def test_get_ft_article_contents(article):
    assert article.readable_url.split("/")[-1].isalnum()
    
def test_get_article_text(article):
    assert len(article.text_data)>0

def test_search_contents():
    article_urls = ft_article_urls(KEYWORD)
    assert len(article_urls) > 0
    
    

    