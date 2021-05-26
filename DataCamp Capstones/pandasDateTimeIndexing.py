# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:47:25 2020
How to set the index of a DataFrame 
using an already converted column
@author: Aim
"""
# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df['Date'])


# Set the index to be the converted 'Date' column
df.set_index('Date', inplace=True)
#.set_index('column', args, args, args) 
#key takeaway is in set_index you cannot use index slicing df['column']
#because while the index is replaced by the datetime objects, the Date column
#is not eliminated. There will be 2 columns in df because the 'Date' column persists
#if use the proper 'column' arg within .set_index(), the stated column will no
#longer show as a non-index column.