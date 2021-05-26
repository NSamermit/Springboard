# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:46:06 2020
From Python Basics on YT: https://www.youtube.com/watch?v=3nJkPVrw44k
pandas ffill/bfill methods
@author: NSamermit
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, 2, 5],
                   [np.nan, 3, np.nan, 4]],
                   columns = list('ABCD'))


df.ffill() #row 2 cols A and B are filled going forward. Row 3
#for .ffill() and .bfill(), use the inplace=True arg to commit the change to df
