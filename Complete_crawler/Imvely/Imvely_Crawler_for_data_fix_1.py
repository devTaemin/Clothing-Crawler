# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:34:08 2019

@author: Taemin
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re



#Sequence : URL input => widget => Crawling => text file



def Imvely_crawler():
    
    m = 0
    textfile=open('Imvely_training_data_5.text','w',encoding='utf-8')
    testcase1="http://www.imvely.com/product/detail.html?product_no=5727&cate_no=57&display_group=1"
    testcase2="http://www.imvely.com/product/detail.html?product_no=14210&cate_no=57&display_group=1"
    testcase3="http://www.imvely.com/product/detail.html?product_no=15996&cate_no=57&display_group=1"
    testcase4="http://www.imvely.com/product/detail.html?product_no=13412&cate_no=57&display_group=1"
    testcase5="http://www.imvely.com/product/detail.html?product_no=8892&cate_no=57&display_group=1"
    testcase6="http://www.imvely.com/product/detail.html?product_no=13986&cate_no=57&display_group=1"
    testcase7="http://www.imvely.com/product/detail.html?product_no=15012&cate_no=57&display_group=1"
    testcase8="http://www.imvely.com/product/detail.html?product_no=14944&cate_no=57&display_group=1"
    testcase9="http://www.imvely.com/product/detail.html?product_no=14584&cate_no=57&display_group=1"
    testcase10="http://www.imvely.com/product/detail.html?product_no=11730&cate_no=57&display_group=1"
    testcase11="http://www.imvely.com/product/detail.html?product_no=13272&cate_no=57&display_group=1"
    testcase12="http://www.imvely.com/product/detail.html?product_no=11727&cate_no=57&display_group=1"
    testcase13="http://www.imvely.com/product/detail.html?product_no=7147&cate_no=57&display_group=1"
    testcase14="http://www.imvely.com/product/detail.html?product_no=16332&cate_no=57&display_group=1"
    testcase15="http://www.imvely.com/product/detail.html?product_no=10938&cate_no=57&display_group=1"
    testcase16="http://www.imvely.com/product/detail.html?product_no=16331&cate_no=57&display_group=1"
    testcase17="http://www.imvely.com/product/detail.html?product_no=16194&cate_no=57&display_group=1"
    testcase18="http://www.imvely.com/product/detail.html?product_no=11707&cate_no=57&display_group=1" 
    testcase19="http://www.imvely.com/product/detail.html?product_no=14302&cate_no=57&display_group=1"
    testcase20="http://www.imvely.com/product/detail.html?product_no=14511&cate_no=57&display_group=1"
    testcase21="http://www.imvely.com/product/detail.html?product_no=13138&cate_no=57&display_group=1"
    testcase22="http://www.imvely.com/product/detail.html?product_no=14729&cate_no=57&display_group=1"
    testcase23="http://www.imvely.com/product/detail.html?product_no=10935&cate_no=57&display_group=1"
    testcase24="http://www.imvely.com/product/detail.html?product_no=15579&cate_no=57&display_group=1"
    testcase25="http://www.imvely.com/product/detail.html?product_no=14512&cate_no=57&display_group=1"
    testcase26="http://www.imvely.com/product/detail.html?product_no=12785&cate_no=57&display_group=1"
    testcase27="http://www.imvely.com/product/detail.html?product_no=13828&cate_no=57&display_group=1"
    testcase28="http://www.imvely.com/product/detail.html?product_no=8857&cate_no=57&display_group=1"
    testcase29="http://www.imvely.com/product/detail.html?product_no=15308&cate_no=57&display_group=1"
    testcase30="http://www.imvely.com/product/detail.html?product_no=16403&cate_no=57&display_group=1"
    testcase31="http://www.imvely.com/product/detail.html?product_no=14183&cate_no=57&display_group=1"
    testcase32="http://www.imvely.com/product/detail.html?product_no=16445&cate_no=57&display_group=1"
    
    testcase_list = [testcase1, testcase2, testcase3, testcase4, testcase5, testcase6, testcase7, testcase8, testcase9, testcase10, testcase11, testcase12, testcase13, testcase14, testcase15, testcase16, testcase17, testcase18, testcase19, testcase20, testcase21, testcase22, testcase23, testcase24, testcase25, testcase26, testcase27, testcase28, testcase29, testcase30, testcase31, testcase32]
    for k in range(32):
        url = testcase_list[k]
    
        #From input url, make the review_widget_url
        product_number = url[url.find("product_no=")+11:url.find("&")]
        widget_url = "http://widgets6.cre.ma/imvely.com/products/reviews?product_code=" + product_number + "&iframe_id=crema-product-reviews-2&widget_id=82&app=0"
    
    
        source = urlopen(widget_url)
        obj = soup(source,"html.parser")
        pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
        star_page = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"widget_reviews__body products_reviews_list__body"}).find('div',{"class":"page"}).find('ul',{"class":"reviews reviews-product"})

        #Calculate number of pages
        temp=""
        for l in range(0,len(pages)):
            if(pages[l].isdigit()):
                temp+=pages[l]
        pages=ceil(int(temp)/10)
        
  
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
Imvely_crawler()


'''
"http://imvely.com/product/detail.html?product_no=12540&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16477&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=14980&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16641&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16470&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16573&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16556&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16599&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16445&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=15552&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=14891&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16623&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16454&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16527&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16537&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16568&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=13064&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=13838&cate_no=41&display_group=1" 
"http://imvely.com/product/detail.html?product_no=16492&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16384&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16507&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16526&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=16460&cate_no=41&display_group=1"
"http://imvely.com/product/detail.html?product_no=12325&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=13990&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16656&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16506&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14267&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=12973&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=13599&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14074&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=15394&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16587&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=13949&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=12001&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16124&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=15893&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=15204&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14275&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16546&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16629&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16528&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=15512&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14170&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16014&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16508&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16671&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16615&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14925&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16346&cate_no=52&display_group=1" 
"http://imvely.com/product/detail.html?product_no=14607&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14639&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16560&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=14918&cate_no=52&display_group=1"
"http://imvely.com/product/detail.html?product_no=16595&cate_no=52&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=12165&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15762&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15111&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16550&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16273&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16597&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=10973&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15043&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16516&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13961&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15882&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16373&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14502&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14154&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16152&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16616&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14470&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16556&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16542&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=11566&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13188&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16161&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15654&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14308&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14134&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14787&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13388&cate_no=46&display_group=1" 
"http://www.imvely.com/product/detail.html?product_no=14074&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16485&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16532&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14759&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15085&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15776&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13773&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15747&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15661&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14399&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13136&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16682&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15409&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15517&cate_no=46&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14991&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=10923&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14221&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15060&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16457&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16726&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14878&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16608&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16006&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14763&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16611&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15195&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16545&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14139&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16672&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14231&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16538&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16394&cate_no=126&display_group=1" 
"http://www.imvely.com/product/detail.html?product_no=16717&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16596&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16490&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15543&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=14799&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16651&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15608&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16468&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16689&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=13814&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15007&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15335&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=15218&cate_no=126&display_group=1"
"http://www.imvely.com/product/detail.html?product_no=16433&cate_no=126&display_group=1"
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
'''