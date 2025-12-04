# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 17:54:01 2025

@author: d23gr
"""
import pandas as pd

class data_cleanFuncs():
    def convert_MTB_time(df_col):
        new_col = pd.to_timedelta(df_col).dt.total_seconds()
        
        return new_col
    
        