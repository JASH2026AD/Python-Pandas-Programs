import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("./data.csv")
print("Before",a)
a_split=a['address'].str.split(',',n=1,expand=True)
a['district']=a_split[0]
a['state']=a_split[1]
del(a['address'])
print("After=",a)
a.plot(kind='scatter',x='marks',y='rollno',c='red')
plt.show()