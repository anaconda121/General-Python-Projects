# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:30:11 2020

@author: tanis
"""

import pandas as pd

read_file = pd.read_excel (r'IDSEXCEL.xlsx')
read_file.to_csv (r'world.csv', index = None, header=True)
