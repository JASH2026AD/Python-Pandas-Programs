import pandas as pd
a=pd.read_csv("./data.csv")
print("Before:")
print(a)
a_split=a['address'].str.split(',',n=1,expand=True)
a['district']=a_split[0]
a['state']=a_split[1]
del(a['address'])
print("After:")
print(a)