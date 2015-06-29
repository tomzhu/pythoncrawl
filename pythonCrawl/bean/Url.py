#!/usr/bin/python 

"""describe a url with a url string and visitedTime"""

class Url:
    
    """A url class to describe a url"""
    
    def __init__(self , url , visitedTime = 1):
        self.url = url
        self.visitedTime = visitedTime
        
    def __str__(self):
        return "[Url:url=" + self.url + ",visitedTime=" + self.visitedTime + "]"
    
    __repr__ = __str__
    
    
    def __setUrl__(self , url):
        self.url = url
        
    def __getUrl__(self):
        return self.url
    
    def __setVisitedTime__(self , visitedTime):
        self.visitedTime = 1
    
    def __getVisitedTime(self):
        return self.visitedTime