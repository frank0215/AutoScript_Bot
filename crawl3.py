import requests
from bs4 import BeautifulSoup
import datetime

def askArticle(start_date, period=0, pages=1):
    url = 'http://luxutvpremium.blog.fc2.com'
    now_date = datetime.datetime.now()
    current_page = pages
    start_date = datetime.datetime.strptime(start_date, '%Y/%m/%d')
    for round in range(pages):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        articles = soup.select('h2.topentry_title a')
        dates = soup.select('span.date')

        articlelist = [article.get('href') for article in articles]

        datelist = [datetime.datetime.strptime(date.text.strip('\n'), '%Y/%m/%d') for date in dates]

        articlelist = list(map(list,[article for article in zip(datelist, articlelist) if (article[0] <= start_date) and (start_date - article[0] < datetime.timedelta(days=(period+1)))]))

        next_url = soup.select('a.pager_next')[0].get('href')
        url = next_url

    if start_date < now_date and len(articlelist)==0:
        current_page += 1
        return askArticle(datetime.datetime.strftime(start_date, '%Y/%m/%d'), period=0, pages=current_page)
    else:
        return articlelist

def saveImg(articlelist):
    count = 0
    total_img = []
    datelist = []
    for article in articlelist:
        res = requests.get(article[1])
        soup = BeautifulSoup(res.text, 'lxml')
        imglist = soup.select('img')
        saveImg = [img .get('src') for img in imglist if 'https://image.mgstage.com/images/' in img.get('src')]
        count += len(saveImg)     
        total_img.append(saveImg)
        datelist.append(article[0])
        
    return total_img, datelist, count
