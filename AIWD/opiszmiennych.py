#OPIS ZMIENNYCH

import pandas as pd

dane=pd.read_csv("c://Users/Michal i Julia//Desktop//analiza//ATUS.csv")

#Socializing & Relaxing
relaks=dane["Socializing & Relaxing"]
r=relaks.fillna(0)
print(r.describe())

#Housework
pracedom=dane["Housework"]
p=pracedom.fillna(0)
print(p.describe())

#Food & Drink Prep
gotowanie=dane["Food & Drink Prep"]
g=gotowanie.fillna(0)
print(g.describe())

#Weekly Earnings
zarobki=dane["Weekly Earnings"]
z=zarobki.fillna(0)
print(z.describe())

#Weekly Hours Worked
godziny=dane["Weekly Hours Worked"]
godz=godziny.fillna(0)
print(godz.describe())

#Gender -----> SPRAWDZIĆ CZY JEST DOBRZE!!!!!
plec=dane["Gender"]
sex=plec.fillna(0)
print(sex.describe())

#Employment Status -----> SPRAWDZIĆ CZY JEST DOBRZE!!!!!
zatrudnienie=dane["Employment Status"]
sz=zatrudnienie.fillna(0)
print(sz.describe())
