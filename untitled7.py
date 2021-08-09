# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:34:59 2021

@author: Wayne
"""

import matplotlib.pyplot as plt
import xarray as xr    #读取nc文件
import numpy as np
import cartopy.crs as ccrs   #投影方式
import cartopy.feature as cfeat   #使用shp文件
from cartopy.io.shapereader import Reader  #读取自定的shp文件
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter  #将x，y轴换成经纬度
obj = xr.open_dataset('F://202001.nc')
print(obj)
