import requests
from  bs4 import BeautifulSoup
from newspaper import Article

url = 'https://www.livemint.com/market/stock-market-news/page-1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url, headers, timeout=90)
soup = BeautifulSoup(response.content,'html.parser')
headlines_raw = soup.findAll('h2',class_='headline')
time = soup.findAll('span', {'data-expandedtime': True})
headlines = []
for i , headline in enumerate(headlines_raw):
    start_index = headline.find('a')['onclick'].find('target_url:')+len("target_url: '")
    end_index = headline.find('a')['onclick'].find('}')-1
    article = Article(headline.find('a')['onclick'][start_index:end_index].strip())
    article.download()
    article.parse()
    article.nlp()
    headlines.append({
        'headline': headline.get_text(strip=True),
        'summary':article.summary,
        'time': time[i]['data-updatedtime']})

