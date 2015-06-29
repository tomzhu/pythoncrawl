#1/usr/bin/python 

import urllib
import urllib2
import re 
from distlib.locators import Page

class QUBAICrawl:
    
    def __init__(self):
        self.page = 1
        self.content = []
        self.imgUrl = []
        self.items = 0
        
    def crawl(self , pageCount = 10):
        while self.page < pageCount:
            url = "http://www.qiushibaike.com/8hr/page/" + self.page + "?s=4785182"
            
           
     
    
    