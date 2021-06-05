#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

class Task_2:
    
    def __init__(self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3
    
    def downsample(self):
        dt = pd.DataFrame()
        # Read the file
        df = pd.read_csv(self.file1)
        # Convert to datetime 
        dt['time'] = pd.to_datetime(df['Absolute Time'])
        # Resampling down to 60 seconds i.e., 1 min
        dt = dt.resample('60s', on='time').first()
        
        #To append the resampled time into dataframe that contains detail.csv
        df = df.reset_index()
        dm = [df, dt]
        dm_final = pd.concat(dm, axis=1)
        # Store the modified dtaframe inot new/intermediate "detail_1.csv"
        dm_final.to_csv(self.file2, index=False)

        #Read the modified csv into a new dataframe
        dp = pd.read_csv(self.file2, parse_dates=['time'], index_col=['time'])
        # Downsample all samples of details.csv from 1 sample/sec to 1 sample/min
        dm = dp.resample('60s').mean()

        #Store the entries of 1sample/minute into detailDownsampled.csv
        dm.to_csv(self.file3)
        del dm, dm_final, dp
    
p1 = Task_2("detail.csv","detail_1.csv","detailDownsampled.csv")
p1.downsample()

#Change Realtime to Absolute Time in detailVol.csv and detailTemp.csv
p2= Task_2("detailVol.csv","detail_2.csv","detailVolDownsampled.csv")
p2.downsample()

# remember to save all csv files as CSV UTF-8 (Comma Delimited)
p3 = Task_2("detailTemp.csv","detail_3.csv","detailTempDownsampled.csv")
p3.downsample()

