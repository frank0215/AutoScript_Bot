import requests
from bs4 import BeautifulSoup
import re


def askArticle(page=1):
    url = 'https://www.jkforum.net/forum-535-{}.html'.format(page)
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    articles = soup.select('form li')

    articlelist = []
    for article in articles:
        for datalist in article('em'):
            #print(datalist)
            for data in datalist('span'):
                #print(data)
                articleInfo = []
                articleTime = data.get('title')
                articleInfo.append(articleTime)


        for datalist in article('h3'):

            articleUrl = 'https://www.jkforum.net/' + datalist.select_one('a').get('href')
            articleInfo.append(articleUrl)
            #print(articleUrl)
            articleTitle = datalist.select_one('a').text
            articleInfo.append(articleTitle)
            #print(articleTitle)

        articlelist.append(articleInfo)        
    
    # length = len(articlelist)
    # for i in range(length):
    #     print(articlelist[i][1])
    #print(articlelist)

    return articlelist


def saveImg(articlelist, stop=1):
    imgList = []
    j=0
    for i in range(len(articlelist)):
        response = requests.get(articlelist[i][1])
        soup = BeautifulSoup(response.text, 'html.parser')
        url = soup.select('ignore_js_op img')
        for imgUrl in url:
            imgFile = imgUrl.get('zoomfile')
            print(imgFile)
            imgList.append(imgFile)

        j+=1
        if j==stop:
            break
    #print(imgList)
    # jlist = {'url_pic': imgList}
    # with open('image.json', 'w', encoding='utf-8') as jfile:
    #     json.dump(jlist, jfile, indent=4)
        
    return imgList

# if __name__ == "__main__":
#     articlelist = askArticle(1)
#     saveImg(articlelist)
    
