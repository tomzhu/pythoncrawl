#!/usr/bin/python 

import urllib2
import urllib
from bean.HtmlContent import HtmlContent

url = "http://www.qiushibaike.com/8hr/page/1?s=4785182"

headers = {"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"}

req = urllib2.Request(url , headers = headers)

resp = urllib2.urlopen(req)

htmlContent = HtmlContent(fileNameFeature = "qsbk")

htmlContent.open(resp.read(), "utf-8")