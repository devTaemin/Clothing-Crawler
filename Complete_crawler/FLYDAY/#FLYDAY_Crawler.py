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


    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/5)

  
    #Crawling and write on text file
    textfile=open('Flyday_comment_list.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            textfile.write(comment+"\n")
        print("page ", i, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
URL = input("Enter the URL of product page: ")
FLYDAY_crawler(URL)
#testcase = "http://www.flyday.co.kr/shop/shopdetail.html?branduid=1116605&xcode=018&mcode=003&scode=&special=3&GfDT=Z293UA%3D%3D"