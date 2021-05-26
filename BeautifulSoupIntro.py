# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:17:29 2021
BeautifulSoup tryout on Scotch.io
@author: Aim
"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.scotch.io'

#use requests so we don't have to close connection
r = requests.get(url)

#here's what we can do with a requests object

#we call call and bind attributes 
html_doc = r.text

#we can pass that requests object to BeautifulSoup
soup = BeautifulSoup(html_doc, features='lxml')
#added features arg after console output a suggestions

#BeautifulSoup parses the text, and we can call attributes
print(soup.title)

#soup also has its own methods
scotch_text = soup.get_text()

#print(scotch_text)



