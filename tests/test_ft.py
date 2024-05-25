from sdas.ft import get_article_links

KEYWORD = "gold"

def test_search_contents():
    contents = get_article_links(KEYWORD)
    assert len(contents) > 0