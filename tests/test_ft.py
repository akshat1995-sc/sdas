from sdas.ft import get_ft_article_readable_url, get_ft_articles
from sdas.url_utils import get_readable_url_code

KEYWORD = "gold"

def test_search_contents():
    article_links = get_ft_articles(KEYWORD)
    assert len(article_links) > 0
    
def test_get_ft_article_contents():
    articles = get_ft_articles(KEYWORD)
    article_content = get_ft_article_readable_url(articles[0])
    assert get_readable_url_code(article_content).isalnum()