import pandas as pd
ds=pd.read_csv('Game_medal.csv',encoding="ISO-8859-1")
ds.head()
ds.tail()
ds.describe()
ds.shape
ds.shift
ds.info()
ds.NOC
ds.plot()
import matplotlib.pyplot as plt
plt.plot(ds.Edition)
plt.plot(ds.Edition,label="YEAR OF EVENTS")
plt.plot(ds.Edition,color="RED",label="YEAR OF EVENTS")
