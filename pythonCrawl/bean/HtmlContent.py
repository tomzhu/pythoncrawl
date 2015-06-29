#!/usr/bin/python
#-*- coding=utf-8 -*-

import codecs 
import webbrowser

class HtmlContent:
    
    """used to show the html from html content
       一个简单的辅助类，用于将产生的html的data
       存储为文件，然后用浏览器打开查看
    """
    
    def __init__(self , filePath = None, fileNameFeature = None):
        webbrowser.open("http://www.baidu.com")
        if filePath == None:
            self.filePath = "/home/tomzhu/program/python/python-file-temp/"
        else:
            self.filePath = filePath
        if fileNameFeature == None:
            self.fileNameFeature = "temp-web"
        else:
            self.fileNameFeature = fileNameFeature
        self.count = 0    
            
    def open(self , content , encoding = "utf-8"):
        fileName = self.filePath + self.fileNameFeature + str(self.count) + ".html"
        f = codecs.open(fileName , "w" , encoding)
        f.write(content.decode(encoding))
        f.close()
        webbrowser.open("file:///" + fileName)
        self.count = self.count + 1
        