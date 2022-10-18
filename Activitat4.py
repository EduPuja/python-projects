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