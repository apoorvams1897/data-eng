#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def main():
    
# Read excel file i.e., data.xlsx and data_1.xlsx into 2 respective dataframe all_dfs and all_dfs_1
    all_dfs = pd.read_excel('data.xlsx', sheet_name=None) 
    all_dfs_1 = pd.read_excel('data_1.xlsx', sheet_name=None)

# Concatenate all sheets of data.xlsx which have the name "Detail_67_" into a new dataframe final_df
    detail = pd.concat([all_dfs['Detail_67_1_1'], all_dfs['Detail_67_1_1_1'], all_dfs['Detail_67_1_1_2'],
                     all_dfs['Detail_67_1_1_3'],all_dfs['Detail_67_1_1_4'],
                     all_dfs['Detail_67_1_1_5'],all_dfs['Detail_67_1_1_6']],ignore_index=True)

# Concatenate all sheets of data.xlsx which have the name "DetailVol_67_" into a new dataframe final_df_Vol
    Vol = pd.concat([all_dfs['DetailVol_67_1_1'], all_dfs['DetailVol_67_1_1_1'], all_dfs['DetailVol_67_1_1_2'],
                     all_dfs['DetailVol_67_1_1_3'],all_dfs['DetailVol_67_1_1_4'],
                     all_dfs['DetailVol_67_1_1_5'],all_dfs['DetailVol_67_1_1_6']],ignore_index=True)

# Concatenate all the sheets which have the name "DetailTemp_67_" into  a new dataframe final_df_Temp
    Temp = pd.concat([all_dfs['DetailTemp_67_1_1'], all_dfs['DetailTemp_67_1_1_1'], all_dfs['DetailTemp_67_1_1_2'],
                     all_dfs_1['DetailTemp_67_1_1_3'],all_dfs_1['DetailTemp_67_1_1_4'],
                     all_dfs_1['DetailTemp_67_1_1_5'],all_dfs_1['DetailTemp_67_1_1_6']],ignore_index=True)

# store all the data in dataframes into csv files namely "detail.csv", "detailVol.csv" and "detailTemp.csv".
    detail.to_csv("detail.csv", index=False)
    Vol.to_csv("detailVol.csv", index=False)
    Temp.to_csv("detailTemp.csv", index=False)

if __name__=="__main__":
    main()

