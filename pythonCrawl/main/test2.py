import re 
import urllib2
import urllib

pa = re.compile("^abc*", flags = 0)

result = pa.match("abch")

if result:
    t = True
else:
    t = False

print t

url = "http://www.baidu.com"
req = urllib2.Request(url)
resp = urllib2.urlopen(req)
print resp.read().decode("utf-8")
