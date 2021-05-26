# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 01:10:15 2020
Austin Temp EDA Capstone
@author: Aim
"""

# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc['August 2010', 'Temperature'].max()
print(august_max)

# Resample August 2011 temps in df_clean by day & aggregate the max value: august_2011
august_2011 = df_clean.loc['August 2011', 'dry_bulb_faren'].resample('D').max()
#print(august_2011)
#print(len(august_2011))
#print(type(august_2011), august_2011.describe)

# Filter for days in august_2011 where the value exceeds august_max: august_2011_high
#print(len(august_2011.values),  len(august_max))
august_2011_high = august_2011.loc[august_2011.values > august_max]
#print(august_2011_high)

# Construct a CDF of august_2011_high
#plt.plot(a, kind='hist', normed='True', cumulative='True', bins=25)
august_2011_high.plot(kind='hist', normed='True', cumulative='True', bins=25)
# Display the plot
plt.show()
