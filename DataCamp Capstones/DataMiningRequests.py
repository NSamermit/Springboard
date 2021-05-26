# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:11:02 2020
Data Mining with requests
@author: Aim
"""

import requests


print('Beginning file download with requests')

url = 'http://www.sidc.be/silso/INFO/sndtotcsv.php' #has to be a string
r = requests.get(url)

with open('/Users/Aim/Downloads/DailySunspot.csv', 'wb') as f:
    f.write(r.content)
    