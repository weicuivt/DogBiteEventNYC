import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from decimal import *
import datetime

getcontext().prec = 10

# Import CVS.file
data_csv0 = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv').fillna(0)
#data_csv1 = pd.read_csv('NYC_Dog_Licensing_Dataset.csv').fillna(0)
data_csv2 = pd.read_csv('DOHMH_Dog_Bite_Data.csv').fillna(0)
data_csv3 = pd.read_csv('DogRuns_20190417.csv').fillna(0)
#print data_csv1.shape, data_csv2.shape,data_csv3.shape
# print data_csv1.head()
# print data_csv2.head()
# print data_csv3.head()
# print data_csv0.head()
# print data_csv0.shape
# lencsv0=len(data_csv0)
# lencsv1=len(data_csv1)
lencsv2=len(data_csv2)
lencsv3=len(data_csv3)


# DogBites_Data:
date2=np.array(data_csv2["DateOfBite"])
zipcode2 = np.array(data_csv2["ZipCode"])
borough2 = np.array(data_csv2["Borough"])
gender2 = np.array(data_csv2["Gender"]).tolist()
spay2 = np.array(data_csv2["SpayNeuter"])
age2 = np.array(data_csv2["Age"])
breed2 = np.array(data_csv2["Breed"])

#other analysis
num1=np.count_nonzero(spay2)
print float(num1)/lencsv2, float(lencsv2-num1)/lencsv2
print float(gender2.count("M"))/lencsv2,float(gender2.count("F"))/lencsv2

# time analysis:
# year={"2015":0,"2016":0,"2017":0}
# month = {'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,
# 		'August':0,'September':0,'October':0,'November':0,'December':0}
# month2 = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,
# 		'August':8,'September':9,'October':10,'November':11,'December':12}
# week=[0]*7
#
# for i in range(lencsv2-1):
#     t=date2[i].split(" ")
#     year[t[2]]+=1
#     month[t[0]]+=1
#     week[datetime.date(int(t[2]),month2[t[0]], int(t[1])).weekday()]+=1
# print year
# print month
# print week
#
# import calendar
# monthN=list(calendar.month_name)
# Smonth=sorted(month.items(), key=lambda t: monthN.index(t[0]))
# print Smonth
#
# j=[]
# for i in range(12):
#     j.append(Smonth[i][1])
# print j
#
# plt.subplot(2, 1, 1)
# plt.bar(np.arange(7),week)
# plt.xticks(np.arange(7), ('Mon', 'Thu', 'Wed', 'Thr', 'Fre','Sat','Sun'))
# plt.title('The Number of Biting Event')
# plt.ylabel('Week')
#
# plt.subplot(2, 1, 2)
# plt.bar(np.arange(12),j)
# plt.xticks(np.arange(12), ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'))
# #plt.xlabel('Time Analysis')
# plt.ylabel('Month')
# plt.show()


#
# #location analysis
t1 =np.unique(borough2)
t2=np.array([0]*len(t1))
dict_borough2 = dict(zip(t1, t2))

t1 =np.unique(zipcode2)
t2=np.array([0]*len(t1))
dict_zipcode2 = dict(zip(t1, t2))

for i in range(lencsv2-1):
    dict_borough2[borough2[i]]+=1
    dict_zipcode2[zipcode2[i]]+=1
print dict_borough2
area=[58.69,69.5,1.0,42.47,22.82,108.1]
{'Staten Island': 930, 'Brooklyn': 2281, 'Other': 437, 'Bronx': 1757, 'Manhattan': 2354, 'Queens': 2520}
print 930/58.69, 2281/69.5, 1757/42.47, 2354/22.82,2520/108.1

sum1=float(930+2281+1757+2354+2520)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Staten Island', 'Brooklyn', 'Bronx', 'Manhattan','Queens'
sizes = [930/sum1,2281/sum1,1757/sum1,2354/sum1,2520/sum1]
#explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# #print dict_zipcode2
#
# Sdict_zipcode2=sorted(dict_zipcode2.items(), key=lambda item: item[1],reverse=True)
# print Sdict_zipcode2
#
# zipcode3 = np.array(data_csv3["ZIPCODE"])
# t1 =np.unique(zipcode3)
# t2=np.array([0]*len(t1))
# dict_zipcode3 = dict(zip(t1, t2))
# print lencsv3
# for i in range(lencsv3-1):
#     dict_zipcode3[zipcode3[i]]+=1
# #print dict_zipcode3
#
# Sdict_zipcode3=sorted(dict_zipcode3.items(), key=lambda item: item[1],reverse=True)
#print Sdict_zipcode3


#breed data:
t1 =np.unique(breed2)
t2=np.array([0]*len(t1))
dict_breed2 = dict(zip(t1, t2))

for i in range(lencsv2-1):
    dict_breed2[breed2[i]]+=1
#print dict_breed2
#print dict_zipcode2

Sdict_breed2=sorted(dict_breed2.items(), key=lambda item: item[1],reverse=True)
print type(Sdict_breed2)
print Sdict_breed2[1:100]

# plt.subplot(2, 1, 1)
# plt.bar(np.arange(7),week)
# plt.xticks(np.arange(7), ('Mon', 'Thu', 'Wed', 'Thr', 'Fre','Sat','Sun'))
# plt.title('The Number of Biting Event')
# plt.ylabel('Week')
#
# plt.subplot(2, 1, 2)
# plt.bar(np.arange(12),j)
# plt.xticks(np.arange(12), ('JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'))
# #plt.xlabel('Time Analysis')
# plt.ylabel('Month')
# plt.show()
