import pandas as pd
file=pd.read_csv("./data.csv")
print('shape :',file.shape)
#no of columns
cols=len(file.axes[1])
print('no of columns:',cols)
#mean of data
m=file["marks"].mean()
print('mean of marks:',m)
