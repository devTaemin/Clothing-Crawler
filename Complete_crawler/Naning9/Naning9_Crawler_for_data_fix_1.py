# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:45:01 2019

@author: Taemin
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re



#Sequence : URL input => widget => Crawling => text file



def Naning9_Crawler():
    
    m = 0
    textfile=open('Naning9_training_data_3.text','w',encoding='utf-8')
    testcase1=""
    testcase2=""
    testcase3=""
    testcase4=""
    testcase5=""
    testcase6=""
    testcase7=""
    testcase8=""
    testcase9=""
    testcase10=""
    testcase11=""
    testcase12=""
    testcase13=""
    testcase14=""
    testcase15=""
    testcase16=""
    testcase17=""
    testcase18="" 
    testcase19=""
    testcase20=""
    testcase21=""
    testcase22=""
    testcase23=""
    testcase24=""
    testcase25=""
    testcase26=""
    testcase27=""
    testcase28=""
    testcase29=""
    testcase30=""
    testcase31=""
    testcase32=""
    
    testcase_list = [testcase1, testcase2, testcase3, testcase4, testcase5, testcase6, testcase7, testcase8, testcase9, testcase10, testcase11, testcase12, testcase13, testcase14, testcase15, testcase16, testcase17, testcase18, testcase19, testcase20, testcase21, testcase22, testcase23, testcase24, testcase25, testcase26, testcase27, testcase28, testcase29, testcase30, testcase31, testcase32]
    for k in range(20):
        url = testcase_list[k]
    
        #From input url, make the review_widget_url
        product_number = url[url.find("index_no=")+9:]#:url.find("&")]
        widget_url = "https://widgets1.cre.ma/naning9.com/products/reviews?product_code=" + product_number
    
    
        source = urlopen(widget_url)
        obj = soup(source,"html.parser")
        pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
        star_page = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"})

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
                EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
                comment_refine = EMOJI.sub(r'',comment) 
                textfile.write(str(m)+"\t"+comment_refine+"\t"+str(basket[n])+"\n")
                n = n + 1
                m = m + 1
                print("comments ", m, " finished!")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#URL = input("Enter the URL of product page: ")
Naning9_Crawler()


'''
"http://www.naning9.com/shop/view.php?index_no=54567"
"http://www.naning9.com/shop/view.php?index_no=53366"
"http://www.naning9.com/shop/view.php?index_no=42377"
"http://www.naning9.com/shop/view.php?index_no=50366"
"http://www.naning9.com/shop/view.php?index_no=49692"
"http://www.naning9.com/shop/view.php?index_no=54826"
"http://www.naning9.com/shop/view.php?index_no=41057"
"http://www.naning9.com/shop/view.php?index_no=54567"
"http://www.naning9.com/shop/view.php?index_no=42377"
"http://www.naning9.com/shop/view.php?index_no=53910"
"http://www.naning9.com/shop/view.php?index_no=53366"
"http://www.naning9.com/shop/view.php?index_no=49692"
"http://www.naning9.com/shop/view.php?index_no=48014"
"http://www.naning9.com/shop/view.php?index_no=42713"
"http://www.naning9.com/shop/view.php?index_no=53729"
"http://www.naning9.com/shop/view.php?index_no=41057"
"http://www.naning9.com/shop/view.php?index_no=49158"
"http://www.naning9.com/shop/view.php?index_no=49026" 
"http://www.naning9.com/shop/view.php?index_no=54168"
"http://www.naning9.com/shop/view.php?index_no=42369"
"http://www.naning9.com/shop/view.php?index_no=50366"
"http://www.naning9.com/shop/view.php?index_no=50136"
"http://www.naning9.com/shop/view.php?index_no=42249"
"http://www.naning9.com/shop/view.php?index_no=53911"
"http://www.naning9.com/shop/view.php?index_no=53492"
"http://www.naning9.com/shop/view.php?index_no=52430"
"http://www.naning9.com/shop/view.php?index_no=47916"
"http://www.naning9.com/shop/view.php?index_no=46210"
"http://www.naning9.com/shop/view.php?index_no=45463"
"http://www.naning9.com/shop/view.php?index_no=48838"
"http://www.naning9.com/shop/view.php?index_no=48636"
"http://www.naning9.com/shop/view.php?index_no=48113"
"http://www.naning9.com/shop/view.php?index_no=25402"
"http://www.naning9.com/shop/view.php?index_no=36400"
"http://www.naning9.com/shop/view.php?index_no=38968"
"http://www.naning9.com/shop/view.php?index_no=42377"
"http://www.naning9.com/shop/view.php?index_no=39799"
"http://www.naning9.com/shop/view.php?index_no=42713"
"http://www.naning9.com/shop/view.php?index_no=42369"
"http://www.naning9.com/shop/view.php?index_no=42249"
"http://www.naning9.com/shop/view.php?index_no=42077"
"http://www.naning9.com/shop/view.php?index_no=41989"
"http://www.naning9.com/shop/view.php?index_no=50550"
"http://www.naning9.com/shop/view.php?index_no=41989"
"http://www.naning9.com/shop/view.php?index_no=54295"
"http://www.naning9.com/shop/view.php?index_no=43015"
"http://www.naning9.com/shop/view.php?index_no=54277"
"http://www.naning9.com/shop/view.php?index_no=33169"
"http://www.naning9.com/shop/view.php?index_no=40953"
"http://www.naning9.com/shop/view.php?index_no=42577" 
"http://www.naning9.com/shop/view.php?index_no=43119"
"http://www.naning9.com/shop/view.php?index_no=42331"
"http://www.naning9.com/shop/view.php?index_no=41855"
"http://www.naning9.com/shop/view.php?index_no=42742"
"http://www.naning9.com/shop/view.php?index_no=43015"
"http://www.naning9.com/shop/view.php?index_no=48919"
"http://www.naning9.com/shop/view.php?index_no=48555"
"http://www.naning9.com/shop/view.php?index_no=49158"
"http://www.naning9.com/shop/view.php?index_no=53888"
"http://www.naning9.com/shop/view.php?index_no=50092"
"http://www.naning9.com/shop/view.php?index_no=41753"
"http://www.naning9.com/shop/view.php?index_no=41670"
"http://www.naning9.com/shop/view.php?index_no=42221"
"http://www.naning9.com/shop/view.php?index_no=41116"  
"http://www.naning9.com/shop/view.php?index_no=41990"
"http://www.naning9.com/shop/view.php?index_no=42440"
"http://www.naning9.com/shop/view.php?index_no=42793"
"http://www.naning9.com/shop/view.php?index_no=44168"
"http://www.naning9.com/shop/view.php?index_no=36568"
"http://www.naning9.com/shop/view.php?index_no=49047"
"http://www.naning9.com/shop/view.php?index_no=42680"
"http://www.naning9.com/shop/view.php?index_no=50976"
"http://www.naning9.com/shop/view.php?index_no=51662"
"http://www.naning9.com/shop/view.php?index_no=41663"
"http://www.naning9.com/shop/view.php?index_no=18773"
"http://www.naning9.com/shop/view.php?index_no=42680"
"http://www.naning9.com/shop/view.php?index_no=43075"
"http://www.naning9.com/shop/view.php?index_no=41080"
"http://www.naning9.com/shop/view.php?index_no=42574"
"http://www.naning9.com/shop/view.php?index_no=41116"
"http://www.naning9.com/shop/view.php?index_no=42331"
"http://www.naning9.com/shop/view.php?index_no=42440" 
"http://www.naning9.com/shop/view.php?index_no=41620"
"http://www.naning9.com/shop/view.php?index_no=41781"  
'''