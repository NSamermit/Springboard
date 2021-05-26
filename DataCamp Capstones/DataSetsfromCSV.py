# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:29:19 2020

@author: Aim
"""
'''This file does not match DataCamp's video as the csv only has 1 column instead of 6'''
import pandas as pd
filepath = 'DailySunspot.csv'
col_names = ['year', 'month', 'day', 'dec_date', 'sunspots', 'definite']
sunspots = pd.read_csv(filepath, header=None, names=col_names)
sunspots.info()
sunspots.iloc[10:20, :]