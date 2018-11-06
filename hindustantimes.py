import requests  
import csv
import pandas as pd
from bs4 import BeautifulSoup 

def htnews(): 
    url1='https://www.hindustantimes.com/latest-news'
    url2='https://www.hindustantimes.com/top-news'
    
    web_response = requests.get(url1, url2) 
    
    if web_response.status_code==200:     
        soup = BeautifulSoup(web_response.text, 'html.parser')	 
        newslist = soup.find("ul", {"class":"latest-news-bx"}) 
        with open("Latest_News.csv", 'w') as f:
            writer = csv.writer(f, dialect='excel')
            writer.writerow(['News', 'Link'])
            for news in newslist.findAll("a"):
                if news.text.startswith(" read more") or news.text.startswith("read more") :
                    pass
                else:
                    writer.writerow(news)
                    
        f.close()
        df = pd.read_csv('Latest_News.csv')
        df.drop('Link', axis = 1, inplace = True)
        df.to_csv('Latest_News.csv', index = False)
        print("News Extracted from Hindustan Times has been Succcessfully imported to \n Latest_News.csv")
    else: 
        print("Webpage Error: Please try again...") 
  
htnews()
