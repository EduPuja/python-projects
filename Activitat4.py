# -*- coding: utf-8 -*-
"""Activitat4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SW8ff4C6jU_Uf8xJTmthUyZDN3_J1iTP
"""

from google.colab import files

uploaded = files.upload()

#punt 1
from pathlib import PureWindowsPath
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("cars_data.csv")
anys = data["car_year"].values
anys.sort() # ordneao els anys

nCotxes2005=0
nCotxes2006=0
nCotxes2007=0
nCotxes2008=0
nCotxes2009=0
nCotxes2010=0
nCotxes2011=0
nCotxes2012=0

for row in anys:
  if row>=2005 and row<=2012:
    if row == 2005:
      nCotxes2005= nCotxes2005+1
    elif row == 2006:
      nCotxes2006 = nCotxes2006 +1
    elif row == 2007:
      nCotxes2007 = nCotxes2007 +1
    elif row == 2008:
      nCotxes2008 = nCotxes2008 +1
    elif row == 2009:
      nCotxes2009 = nCotxes2009 +1
    elif row == 2010:
      nCotxes2010 = nCotxes2010 +1
    elif row == 2011:
      nCotxes2011 = nCotxes2011 +1
    elif row == 2012:
      nCotxes2012 = nCotxes2012 +1

x = ["2005","2006","2007","2008","2009","2010","2011","2012"]
y = [nCotxes2005,nCotxes2006,nCotxes2007,nCotxes2008,nCotxes2009,nCotxes2010,nCotxes2011,nCotxes2012]

plt.bar(x,y)
plt.show()

# DIAGRAMA DE SECTORS





c2005 = 0
c2006 = 0
c2007 = 0
c2008 = 0
c2009 = 0
c2010 = 0
c2011 = 0
c2012 = 0
for i in range(len(data["car_year"])):
  if data["car_year"][i] == 2005:
    c2005 = c2005 +1 
  elif data["car_year"][i] == 2006:
    c2006 = c2006 +1
  elif data["car_year"][i] == 2007:
    c2007 = c2007 +1 
  elif data["car_year"][i] == 2008:
    c2008 = c2008 +1 
  elif data["car_year"][i] == 2009:
    c2009 = c2009 +1 
  elif data["car_year"][i] == 2010:
    c2010 = c2010 +1 
  elif data["car_year"][i] == 2011:
    c2011 = c2011 +1 
  elif data["car_year"][i] == 2012:
    c2012 = c2012 +1 

x = ["2005","2006","2007","2008","2009","2010","2011","2012"]
y = [c2005,c2006,c2007,c2008,c2009,c2010,c2011,c2012]
plt.pie(y, labels=x, autopct="%0.1f %%")
plt.axis("equal")
plt.show()

#Punt 3
brands = data["car_brand"].values
models = data["car_model"].values
years = data["car_year"].values

# ordeno els arrays
brands.sort()
models.sort()
years.sort()
#imprimeixo per saber quants models i tot
#print(brands)
#print(models)
#print(years)



for i in brands:
  if "Volkswagen" in i:
    print(i)

#punt 5 -- cert i fals  

hybrid = data["hybrid_car"].values
for a in hybrid:
  if True in hybrid:
      print("Cotxe SI")