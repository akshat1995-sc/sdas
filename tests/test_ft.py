from sdas.base import ArticleData
from sdas.ft import get_ft_article_readable_url, get_ft_articles, get_text_from_readable_url
from sdas.url_utils import get_readable_url_code

import pytest

KEYWORD = "gold"

@pytest.fixture
def articles()->list[ArticleData]:
    return get_ft_articles(KEYWORD)

@pytest.fixture
def readable_article_url(articles)->str:
    return get_ft_article_readable_url(articles[0])

def test_search_contents():
    article_links = get_ft_articles(KEYWORD)
    assert len(article_links) > 0
    
def test_get_ft_article_contents(articles):
    article_content = get_ft_article_readable_url(articles[0])
    assert get_readable_url_code(article_content).isalnum()
    
def test_get_article_text(readable_article_url):
    article_text = get_text_from_readable_url(readable_article_url)
    assert len(article_text)>0
    