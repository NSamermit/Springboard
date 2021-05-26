# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:14:48 2020
Pandas .loc[] cheat sheet
@author: Aim
"""
DataFrame.loc[datetime:datetime, 'column']


# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['June 20, 2011 8AM':'June 20, 2011 8AM', 'dry_bulb_faren']) 
#pd interprets 8AM as 8:00 to 8:59:59
#if use 9AM, it will include values from 9:00 to 9:59:59


# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample("D").mean()

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011.dry_bulb_faren.values

# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample("D").mean()

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()['Temperature'].values
#.reset_index() completely resets the index
#can slice immediately after .reset_index()[slice arg]
#probably do not need .values but wanted to be consistent with line 5

#debug
#print('daily_temp_2011 info: ', type(daily_temp_2011), len(daily_temp_2011), daily_temp_2011.shape)
#print('daily_temp_climate info: ', type(daily_temp_climate), len(daily_temp_climate), daily_temp_climate.shape)

# Compute the difference between the two arrays and print the mean difference
#Note - both have to be numpy arrays of the same shape to perform the calcs. 
#confirmed with print shape of both ndarrays are (365, )
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())