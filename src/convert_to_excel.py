import pandas as pd
import json

col = ['query','ptime','pcontent','nb_retweet','nb_favorite','nb_reply']
f = 'tweet_by_query_table'
data = []
for d in open(f,'r').readlines():
     l = json.loads(d)
     s = []
     for c in col:
         s.append(l[c])
     data.append(s)

df = pd.DataFrame(data)  
df.columns = col
df.to_excel(f+'.xls',encoding='utf-8',index=False) 


f = 'tweet_by_user_table'
data = []
for d in open(f,'r').readlines():
     l = json.loads(d)
     s = []
     for c in col:
         s.append(l[c])
     data.append(s)

df = pd.DataFrame(data)  
df.columns = col
df.to_excel(f+'.xls',encoding='utf-8',index=False) 

col = ['intro','name','query']
f = 'user_table'
data = []
for d in open(f,'r').readlines():
    l = json.loads(d)
    if l['query'] == '':
        continue
    s = []
    for c in col:
        s.append(l[c])
    data.append(s)

df = pd.DataFrame(data)  
df.columns = col
df.to_excel(f+'.xls',encoding='utf-8',index=False) 

