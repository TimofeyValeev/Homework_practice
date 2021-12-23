from pandas import *
from numpy import *

data = read_csv("https://raw.githubusercontent.com/nicepeopleproject/ml_linear_regression/master/data/data.csv")

make = data.Make.unique()
brand = []
for i in data.Make.unique():
    brand.append(i)
    
summary = []
carAmount = []
for i in range(data.Make.nunique()):
    summary.append(0)
    carAmount.append(0)

for i in range(len(data)):
    summary[brand.index(data.Make[i])] += data.MSRP[i]
    carAmount[brand.index(data.Make[i])] += 1

for i in range(data.Make.nunique()):
    summary[i] = summary[i] / carAmount[i]

print("Самые дорогие автомобили выпускает ", brand[summary.index(max(summary))])

carAmount.clear()
for i in range(data.Make.nunique()):
    carAmount.append(0)

for i in range(len(data)):
    if data.MSRP[i] >= 2000 and data.MSRP[i] <= 3000:
        carAmount[brand.index(data.Make[i])] += 1

print("Больше всего автомобилей с ценой от 2 до 3 тыс.$ выпускает ", brand[carAmount.index(max(carAmount))])

for i in data.columns:
    data[i] = data[i].fillna("No info")