import urllib2
import urllib
import sys
import requests
from lxml import html
import json
from requests import Session

url = sys.argv[1]
token_name = '__RequestVerificationToken'

a = urllib2.urlopen(url)
content = a.read()

tree = html.fromstring(content)
b = tree.xpath('//script')
js =  b[-1].text

ind = js.find(token_name)
subJS = js[ind:]
ind2 = subJS.find('value')

subJS = subJS[ind2:]
ind2 = subJS.find('"')

subJS = subJS[ind2:]
ind3 = subJS.find('"', 1)

token = subJS[1:ind3]
print token

id = tree.xpath('//input')

uid = id[0].value


rdata = {token_name: token, 'userId': uid, 'text': 'You are the best !'}

url2 = url + '/Messages/SendMessage' 
print url2

rheads = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': url2}

print rdata

session = Session()
session.head(url2)
r = session.post(url=url2, data=(rdata), headers=rheads)
print r
