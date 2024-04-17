# Sentiment data collector
Online financial websites offer enoumous amount of financial data to play around with. Yet some data for e.g. the sentiment data regarding a particular stock is not easily avaiable. In order to begin the process of collecting sentiment data from different ticker, I aim to design the stated tool.

## Components
The tool has several components including -
- Web scrapper
- Sentiment scoring algorithm
- Post-gres database recording
- Data visualization from database

The following components will each have their own. They are discussed in as much detail as possible in the following subsections.

### Web scrapper
The webscrapper is supposed to collect information about a stock market ticker from websites like google, X and others. This might require an external library to be invoked or an amalgation of an existing code along with a customized part as well.

### Sentiment scoring algorithm
The sentiment scoring algorithm is straight forward thrid party software by the name of nltk. It takes the string text as in input and gives out a float number for positive, neutral and negative sentiment present in the provided text. This will be used in the database registry step of the algorithm.

### Database 
The information will be stored in the dataclass with the name ```TickerInfo``` which would store 
- name
- dictionary which would contain the website name from the data is extracted and the respective score is recorded as well
- date and time of extraction entiity
The sentiment is evaluated using the sentiment scoring algorithm which is done using a third party library. 
- The stock price at the time and date the data is extracted.

### Data visualization
This component is used to visualize the information from the dataclass which is stored in the database. This could include time-series representation of data from different websites for a given ticker. 

We could also perform correlation and auto-correlation visualization to check for relation between different tickers and also within the ticker (for e.g. between the sentimental data and the stock price).