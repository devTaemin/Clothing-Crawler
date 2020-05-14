# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:05:58 2019

@author: Taemin
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil


#Sequence : URL input => widget => Crawling => text file



def Imvely_crawler(url):
    
    
    #From input url, make the review_widget_url
    product_number = url[url.find("product_no=")+11:url.find("&")]
    widget_url = "http://widgets6.cre.ma/imvely.com/products/reviews?product_code=" + product_number + "&iframe_id=crema-product-reviews-2&widget_id=82&app=0"
    
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
    star_page = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"})

    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/10)
    m = 0
  
    #Crawling and write on text file
    textfile=open('Imvely_Crawler_fix_1.text','w',encoding='utf-8')
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
           elif(comp == "- 맘에 들어요"):
               grade = 1 #긍정
           else:
               grade = 0 #부정
           basket.append(grade)
        n = 0
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            textfile.write(str(m)+"\t"+comment+"\t"+str(basket[n])+"\n")
            n = n + 1
            m = m + 1
        print("page ", i, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
URL = input("Enter the URL of product page: ")
Imvely_crawler(URL)

#testcase1="http://www.imvely.com/product/detail.html?product_no=16550&cate_no=71&display_group=1"
#testcase2="http://www.imvely.com/product/detail.html?product_no=14668&cate_no=71&display_group=1"
#testcase3="http://www.imvely.com/product/detail.html?product_no=15996&cate_no=71&display_group=1"
#testcase4="http://www.imvely.com/product/detail.html?product_no=16597&cate_no=71&display_group=1"
#testcase5="http://www.imvely.com/product/detail.html?product_no=15762&cate_no=71&display_group=1"
#testcase6="http://www.imvely.com/product/detail.html?product_no=14584&cate_no=71&display_group=1"
#testcase7="http://www.imvely.com/product/detail.html?product_no=14916&cate_no=71&display_group=1"
#testcase8="http://www.imvely.com/product/detail.html?product_no=16332&cate_no=71&display_group=1"
#testcase9="http://www.imvely.com/product/detail.html?product_no=15012&cate_no=71&display_group=1"
#testcase10="http://www.imvely.com/product/detail.html?product_no=5727&cate_no=113&display_group=1"
#testcase11="http://www.imvely.com/product/detail.html?product_no=12165&cate_no=113&display_group=1"