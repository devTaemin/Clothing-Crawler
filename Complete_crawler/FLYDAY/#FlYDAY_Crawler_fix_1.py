# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:12:33 2019

@author: Taemin
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil


#Sequence : URL input => widget => Crawling => text file


def FLYDAY_crawler(url):
    
    
    #From input url, make the review_widget_url
    product_number = url[url.find("branduid=")+9:url.find("&")]
    widget_url = "http://widgets2.cre.ma/flyday.co.kr/products/reviews?product_code=" + product_number
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
    star_page = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"})

    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/5)
    m = 0
  
    #Crawling and write on text file
    textfile=open('FLYDAY_comment_fix_1.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
        valuation = star_page.findAll('div',{"class":"products_reviews_list_review__score_text_rating"})
        basket = []
        grade = 0;
        
        for val in valuation:
           comp = str(val.text)
           if(comp == "- 아주 좋아요"):
               grade = 1 #긍정
           else:
               grade = 0 #부정
           basket.append(grade)
        n = 0
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            textfile.write(str(m)+"\t"+str(basket[n])+"\t"+comment+"\n")
            n = n + 1
            m = m + 1
        print("page ", i, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
URL = input("Enter the URL of product page: ")
FLYDAY_crawler(URL)
#testcase1 = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1116605&xcode=018&mcode=003&scode=&special=3&GfDT=Z293UA%3D%3D"
#testcase2 = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1114245&xcode=005&mcode=001&scode=&special=3&GfDT=amp3Ug%3D%3D"
#testcase3 = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1113577&xcode=019&mcode=004&scode=&special=3&GfDT=bm9%2FW14%3D"
#testcase4 = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1113994&xcode=005&mcode=001&scode=&special=3&GfDT=bml0W1k%3D"
#testcase5 = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1113790&xcode=019&mcode=004&scode=&special=3&GfDT=a2l3Vw%3D%3D"
