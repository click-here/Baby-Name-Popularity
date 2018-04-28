import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

file_loc = './data'
files = [x for x in os.listdir(file_loc)]

frames = []
for file in files:
    df = pd.read_csv(os.path.join(file_loc,file),header=None,dtype={2:np.int32})
    df = df.rename(columns={0:'name',1:'gender',2:'count'})
    df['year'] = np.int32(file[3:7])
    frames.append(df)
df = pd.concat(frames)

df2 = df.groupby(['year','gender']).agg({'count':['max','sum']}).reset_index()
df2.columns = ['year','gender','count','sum']
df2 = df2.merge(df,on=['gender','year','count'],how='inner')

df2['variance'] = df2['count']/df2['sum']

df3 = df2[['year','gender','variance']].set_index('year')
chart_group = df3.groupby('gender')['variance'].plot()

plt.legend()
plt.title('Most Popular Name as a Percent of Total Population')
plt.xlabel('Year')
plt.ylabel('Percent of Population')
plt.show()
