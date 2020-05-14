# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:07:48 2019

@author: Taemin
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re

def FLYDAY_Crawler():
    
    m = 0
    textfile=open('FLYDAY_testdata_10.text','w',encoding='utf-8')
    testcase1="http://www.flyday.co.kr/shop/shopdetail.html?branduid=1115007&xcode=018&mcode=001&scode=&GfDT=bm19W1hB"
    testcase2=""
    testcase3=""
    testcase4=""
    testcase5=""
    testcase6=""
    testcase7=""
    testcase8=""
    testcase9=""
    testcase10=""
    
    
    testcase_list = [testcase1, testcase2, testcase3, testcase4, testcase5, testcase6, testcase7, testcase8, testcase9, testcase10]
    for k in range(1):
        url = testcase_list[k]
    
        #From input url, make the review_widget_url
        product_number = url[url.find("branduid=")+9:url.find("&")]
        widget_url = "http://widgets2.cre.ma/flyday.co.kr/products/reviews?product_code=" + product_number
    
    
        source = urlopen(widget_url)
        obj = soup(source,"html.parser")
        pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
        #star_page = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"})

        #Calculate number of pages
        temp=""
        for l in range(0,len(pages)):
            if(pages[l].isdigit()):
                temp+=pages[l]
        pages=ceil(int(temp)/5)
        
  
        #Crawling and write on text file
        for i in range(1,pages+1):
            urls=urlopen(widget_url + "&page=" + str(i))
            obj=soup(urls,"html.parser")
        
            reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
            #valuation = star_page.findAll('div',{"class":"products_reviews_list_review__score_text_rating"})
            #basket = []
            #grade = 0;
            '''
            for val in valuation:
                comp = str(val.text)
                if(comp == "- 아주 좋아요"):
                    grade = 1 #긍정
                elif(comp == "- 맘에 들어요"):
                    grade = 1 #긍정
                else:
                    grade = 0 #부정
                basket.append(grade)
            '''
            #n = 0
            for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
                comment = comments.text               
                comment = comment.strip()
                EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
                comment_refine = EMOJI.sub(r'',comment)
                textfile.write(comment_refine+"\n")
                #textfile.write(str(m)+"\t"+comment_refine+"\t"+str(basket[n])+"\n")
                #n = n + 1
                m = m + 1
                print("comments ", m, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#URL = input("Enter the URL of product page: ")
FLYDAY_Crawler()
