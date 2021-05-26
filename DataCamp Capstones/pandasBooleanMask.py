# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:19:52 2020
Creating a boolean mask for pandas
@author: Aim
"""

# Build a Boolean mask to filter for the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'
# df[index] == value is the mask. It will either eval to TRUE or FALSE

# Use the mask to subset the data: la
la = df[mask]
#the subset la contains all rows where the column 'Destination Airport' eval TRUE for 'LAX'

# Combine two columns of data to create a datetime series: times_tz_none 
times_tz_none = pd.to_datetime( la['Date (MM/DD/YYYY)'] + ' ' + la['Wheels-off Time'] ) #creates datetime array/series

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')