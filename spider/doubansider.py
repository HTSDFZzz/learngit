#-*- coding:UTF-8 -*-
import urllib
from bs4 import BeautifulSoup


def getpage(url):
    html = urllib.request.urlopen(url).read().decode('utf-8')
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    return soup
def get_info(soup):
    for content in soup.select('.info'):
        title= content.select('.title')[0].text
        if content.select('.author-item') == []:
            author = None
        else:
            author= content.select('.author-item')[0].text
            category= content.select('.category')[0].text
            price = content.select('.price-tag')[0].text
        if content.select('.rating-average') == []:
            rating = None
        else:
            rating= content.select('.rating-average')[0].text
        if content.select('.ratings-link') == []:
            rate_num = None
        else:
            rate_num = content.select('.ratings-link')[0].text[:-3]
        if content.select('.article-desc-brief') == []:
            desc = None
        else:
            desc= content.select('.article-desc-brief')[0].text
        print(title,author)

#def get_cover(soup):
    #for content in soup.select('.cover shadow-cover'):
        #cover = content.findall('img', class='pic')

def main():
    page = int(input("输入查询页数："))
    key_word = input("输入关键词：")
    for i in range(page):
        i = (i- 1) * 15
        base_url = "https://read.douban.com/search?q="+key_word+"&start="+str(i)
        print(base_url)
        soup = getpage(base_url)
        get_info(soup)

if __name__ == '__main__':
    main()