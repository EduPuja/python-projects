from turtle import pd
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("cars_data.csv")

car_brand = data["car_brand"].values

print(car_brand)
