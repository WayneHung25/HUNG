# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:44:30 2021

@author: Wayne
"""

from netCDF4 import Dataset
# open nc file
a = Dataset("F:/msl/data (1).nc")
print(a)
print(a.variables.keys()) # chekc all key in this file

#print (a.variables['longitude'][:]) # specific key to check value