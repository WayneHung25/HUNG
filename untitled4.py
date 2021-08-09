# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:26:31 2020

@author: USER
"""

# %%
from netCDF4 import Dataset
from wrf import getvar, to_np, CoordPair, vertcross
from matplotlib.cm import get_cmap
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import matplotlib as mpl
import pandas as pd
import shapefile 

#%%

sf = shapefile.Reader("./mapdata202009150149/TOWN_MOI_1090820.shp")
shapes = sf.shapes()
len(shapes)
len(list(sf.iterShapes()))
shapes[3].shapeType
bbox = shapes[3].bbox
['%.3f' % coord for coord in bbox]
s = sf.shape(7)
fields = sf.fields
fields



#%%
# open ncfile700


ncfile700 = Dataset('./wrfout_d03_2019-07-22_07_00_00')
rain_700 = np.array((ncfile700['RAINC']))
rainc_700 = np.array((ncfile700['RAINNC']))
ra_700 = rainc_700 + rain_700
print('li hoe',ra_700)
hgt800 = np.array((ncfile700['HGT']))
ncfile700.close

# open ncfile730
ncfile730 = Dataset('./wrfout_d03_2019-07-22_07_30_00')

rain_730 = np.array((ncfile730['RAINC']))
rainc_730 = np.array((ncfile730['RAINNC']))
ra_730 = rainc_730 + rain_730
print('li hoe',ra_730)
ncfile730.close

# open ncfile800
ncfile800 = Dataset('./wrfout_d03_2019-07-22_08_00_00')

rain_800 = np.array((ncfile800['RAINC']))
rainc_800 = np.array((ncfile800['RAINNC']))
ra_800 = rainc_800 + rain_800
print('li hoe',ra_800)
ncfile800.close

# open ncfile900
ncfile900 = Dataset('./wrfout_d03_2019-07-22_09_00_00')

rain_900 = np.array((ncfile900['RAINC']))
rainc_900 = np.array((ncfile900['RAINNC']))
ra_900 = rainc_900 + rain_900
print('li hoe',ra_900)
ncfile900.close

# open ncfile
ncfile1000 = Dataset('./wrfout_d03_2019-07-22_10_00_00')

rain_1000 = np.array((ncfile1000['RAINC']))
rainc_1000 = np.array((ncfile1000['RAINNC']))
ra_1000 = rainc_1000 + rain_1000
print('li hoe',ra_1000)
ncfile1000.close



# %
rain_30 = (ra_730 - ra_700).reshape(330,330)
rain_60 = (ra_800 - ra_700).reshape(330,330)
rain_120 = (ra_900 - ra_700).reshape(330,330)
rain_180 = (ra_1000 - ra_700).reshape(330,330)
#print(rain_30,rain_60,rain_120,rain_180)
hgt = hgt800.reshape(330,330)

precip_colors = [
    '#fdfdfd',    # white
    '#ccccb3',    # gray
    '#99ffff',    # blue
    '#66b3ff',
    '#0073e6',
    '#002699',
    '#009900',    # green
    '#1aff1a',
    '#ffff00',    # yellow
    '#ffcc00',
    '#ff9900',
    '#ff0000',    # red
    '#cc0000',
    '#990000',
    '#800040',    # purple
    '#b30047',
    '#ff0066',
    '#ff80b3' ]

precip_colormap = mpl.colors.ListedColormap(precip_colors)
clevel = [0, 0.5, 1, 2, 6, 10, 15, 20, 30, 40, 50, 70, 90, 110, 130, 150, 200, 300, 1000]
dlevel = [200,600,1000,1400,1800,2200,2600,3000,3400]
norm = mpl.colors.BoundaryNorm(clevel, 18)
norm2 = mpl.colors.BoundaryNorm(dlevel, 9)

# %
pair = [0, 330 ,330]
xlat = np.array((ncfile700['XLAT']))[0,:]
xlong = np.array((ncfile700['XLONG']))[0, :]
z = np.array((ncfile700['ZNU']))

#ra_re = ra.reshape(330,330)

#%%
pa=(120.5, 122.1, 24, 25.5)
fig0800 = plt.figure(figsize =(20,15))
ax= plt.axes(projection=ccrs.PlateCarree())
projection=ccrs.PlateCarree()
#ax.coastlines()
ax.gridlines()
plt.axis(pa)
#plt.axis(115.90704, 125.919495, 18.897774, 28.087208)
plt.title('2019_0722_0700UTC~0800UTC_Accumulated precipitation',fontsize=30)
ax.set_xlabel("Longitude", fontsize=20)
ax.set_ylabel("Latitude", fontsize=20)
ax.set_xticks(np.linspace(120.5, 122.1, 9), crs=projection)
ax.set_yticks(np.linspace(24, 25.5, 6), crs=projection)
plt.legend

#coord_pairs = to_np(rain_30[])

hgt_contours = ax.contour(xlong,xlat,hgt,cmap=get_cmap("gray"),alpha=0.5,vmin=10,levels=dlevel,norm=norm2)
rain_700_800_contours = ax.contourf(xlong,xlat,rain_60,cmap=precip_colormap,alpha=0.55,levels=clevel,norm=norm)
#rain_700_730_contours = ax.contour(xlong,xlat,rain_30,cmap=precip_colormap,alpha=0.85,levels=clevel,norm=norm)
plt.colorbar(rain_700_800_contours,label='(mm)')
#plt.colorbar(hgt_contours)

v_700 = np.array((ncfile700['V10']))[0,:]
u_700 = np.array((ncfile700['U10']))[0,:]

#plt.barbs(xlong[::2, ::2],xlat[::2, ::2],u_700[::2, ::2],v_700[::2, ::2],length=5, pivot='middle',sizes=dict(emptybarb=0, spacing=0.2, height=0.3))
#%%
for shape in sf.shapeRecords():
        for e in range(len(shape.shape.parts)):
            i_start = shape.shape.parts[e]
            if e==len(shape.shape.parts)-1:
                i_end = len(shape.shape.points)
            else:
                i_end = shape.shape.parts[e+1]
            x = [e[0] for e in shape.shape.points[i_start:i_end]]
            y = [e[1] for e in shape.shape.points[i_start:i_end]]
            plt.plot(x,y,'k',alpha=0.5)
            plt.xlim((120.5,122.1))
            plt.ylim((24,25.5))

#%%




