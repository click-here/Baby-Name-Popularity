import pandas as pd
import os
import matplotlib.pyplot as plt

file_loc = './data'
files = [x for x in os.listdir(file_loc)]

frames = []
for file in files:
    df = pd.read_csv(os.path.join(file_loc,file),header=None)
    df = df.rename(columns={0:'name',1:'gender',2:'count'})
    df['year'] = file[3:7]
    frames.append(df)
df = pd.concat(frames)


df['year']= df['year'].astype(float)
df['count']= df['count'].astype(float)

df2 = df.groupby(['year','gender']).agg({'count':['max','sum']}).reset_index()
df2.columns = ['year','gender','count','sum']
df2 = df2.merge(df,left_on=['gender','year','count'],right_on=['gender','year','count'],how='inner')
df2['var'] = df2['count']/df2['sum']

##df2.plot(x='year', y='count')
##plt.show()
