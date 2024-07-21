def get_readable_url_code(readable_article_url: str)->str:
    return readable_article_url.split("/")[-1]

def check_valid_response(response_code:int):
    if not response_code==200:
        raise ValueError(f"Search result not obtained!, code :{response_code}")
    
def check_valid_date_time_strings(date_time_strings):
    for date_time_string in date_time_strings:
        if not date_time_string:
            raise ValueError("Empty date time string present!")