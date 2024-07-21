from dataclasses import dataclass


@dataclass
class ArticleData:
    original_url: str
    date: str
    time:str
    readable_url: str
    text_data: str
    
