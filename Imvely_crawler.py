# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:50:31 2019

@author: devTaemin
@github: github.com/devTaemin
@github_blog: devTaemin.github.io
@mail: devTaemin@gmail.com

"""
#Sequence : URL input => widget => Crawling => text file
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re



def Imvely_crawler(url):
    
    
    #From input url, make the review_widget_url
    product_number = url[url.find("product_no=")+11:url.find("&")]
    widget_url = "http://widgets6.cre.ma/imvely.com/products/reviews?product_code=" + product_number + "&iframe_id=crema-product-reviews-2&widget_id=82&app=0"
    
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
    
    #Product name
    name = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_product_info"}).find('div',{"class":"products_reviews_product_info__name"}).text
    #Product Photo (Use image_src)
    image = obj.find("img")
    image_src = image.get("src")
    
    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/10)
    m = 0
  
    #Crawling and write on text file
    textfile=open('Imvely.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
            comment_refine = EMOJI.sub(r'',comment) 
            textfile.write(comment_refine+"\n")
            m = m + 1
        print("page ", i, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
URL = input("Enter the URL of product page: ")
Imvely_crawler(URL)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#