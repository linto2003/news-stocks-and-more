import requests
from  bs4 import BeautifulSoup
from newspaper import Article

url = 'https://economictimes.indiatimes.com/markets/markets/ipos/fpos/news'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
resp = requests.get(url,headers,timeout=90)
soup = BeautifulSoup(resp.content,'html.parser')
raw = soup.findAll('div',class_='eachStory')
headlines = []
for data in raw:
    time = data.find('time').get_text(strip=True)
    
    news_url = 'https://economictimes.indiatimes.com'+data.find('a')['href']
    article = Article(news_url)
    article.download()
    article.parse()
    article.nlp()
    headlines.append({
        'headline': article.title,
        'summary':article.summary,
        'time': time})

