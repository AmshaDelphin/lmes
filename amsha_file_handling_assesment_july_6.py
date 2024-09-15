import pandas as pd
import numpy
from sklearn.impute import SimpleImputer

data = pd.read_csv("amsha_coffe_sales.csv")
#print(data)

print(data.tail(6))

#to get no. of rows index range from 0 to lastindex
#print(data.values)

print(data.columns)

print(data.shape)

print(data.index)

print(data.info)

print("Number of Null values in files are ",data.isnull().sum().sum())

#print("\n-----Datas from row 2 to 6------")
#print(data.iloc[2:7])

print("\n-----Datas in col 2 and 3 from row 2 to 6------")
print(data.iloc[1:4,2:4])

print("\n-----Datas from date and money row 2   ------")
print(data.loc[2,["date","money"]])

# print("\n---- fill Null value with 200")
# data.fillna(200,inplace=True)
# print(data.head(6))

print("\n---- fill Null value in money and  with Avg of money value ")
data.fillna({"money":data["money"].mean()},inplace=True)
print(data.head(6))

#data.ffill(inplace=True)
#data.bfill(inplace=True)

data1 = pd.read_csv("amsha_coffe_sales.csv")
print("\n ---- Filling Null with SimpleImputer using constant strategy----")
constant_impute = SimpleImputer(strategy="constant")
data1["money"] = constant_impute.fit_transform(data1[["money"]])
print(data1.head(6))

dataNew = pd.read_csv("amsha_coffe_sales.csv")
print("\n ---- Filling Null with SimpleImputer using median strategy----")
median_impute = SimpleImputer(strategy="median")
dataNew["money"] = median_impute.fit_transform(dataNew[["money"]])
print(dataNew.head(6))


