import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_excel('Uber Request Datas.xlsx')
print(df.head())
print(df.shape)
print(df.describe())


sns.heatmap(df.isnull(),cbar= False,cmap = 'viridis')
plt.title('Missing Values Heatmap')
plt.show()

print(df['Drop timestamp'].isnull().sum())

df['Request timestamp']=pd.to_datetime(df['Request timestamp'],errors='coerce')
df['Drop timestamp']=pd.to_datetime(df['Drop timestamp'],errors='coerce')
print(df.isnull().sum())

df['hour']=df['Request timestamp'].dt.hour
df['hour'].value_counts().sort_index().plot(kind='bar')
plt.title('hour distribution')
plt.xlabel('hours')
plt.ylabel('count')
plt.show()

print(pd.crosstab(df['hour'],df['Status']))

def time_slot(hour):
    if hour>=0 and hour<4:
        return 'Late Night'
    elif hour>=4 and hour<8:
        return 'Early Morning'
    elif hour>=8 and hour<12:
        return 'Morning'
    elif hour>=12 and hour<16:
        return 'Afternoon'
    elif hour>=16 and hour<20:
        return 'Evening'
    else:
        return 'Night'
df['time slot']=df['hour'].apply(time_slot)
print(df['time slot'])
pd.crosstab(df['time slot'],df['Status']).plot(kind = 'bar')
plt.title ('status by time slot')
plt.xlabel('time slot')
plt.ylabel('status')
plt.show()