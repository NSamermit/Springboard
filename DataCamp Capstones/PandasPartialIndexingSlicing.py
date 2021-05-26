# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:21:27 2020
Pandas = partial string indexing and slicing
@author: Nsamermit
"""
#assume df was given...
# Extract temperature data for August: august
august = df.Temperature.loc['2010-08'] #loc is slice; use [] not ()

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df.Temperature.loc['2010-02']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()
