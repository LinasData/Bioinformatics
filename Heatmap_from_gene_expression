import pandas as pd
import math
import numpy as np
from matplotlib import pyplot as plt
from pandas import DataFrame


#Open gene expression data
data = pd.read_csv("normalized_counts.csv", index_col=0)
df = pd.DataFrame(data)

#Convert data to lists
M11 = data["11M_KontrMot"].tolist()
M1 = data["1M_KontrMot"].tolist()
V2 = data["2M_KontrVyr"].tolist()
V12 = data["12M_KontrVyr"].tolist()

# Create function to covert data to logarithmic scale
def data2Log(control):
    Log = []
    for i in control:
        i = float(i)
        if i > 0:
            l = math.log2(i)
            if l >= 0:
                Log.append(l)
            else:
                l = 0
                Log.append(l)
        else:
            l = 0
            Log.append(l)
    return Log

# Covert data to logarithmic scale
M11LOG = data2Log(M11)
M1LOG = data2Log(M1)
V2LOG = data2Log(V2)
V12LOG = data2Log(V12)


# insert data to dataframe
df.insert(loc=(int(df.shape[1])), column="M11LOG", value=M11LOG)
df.insert(loc=(int(df.shape[1])), column="M1LOG", value=M1LOG)
df.insert(loc=(int(df.shape[1])), column="V2LOG", value=V2LOG)
df.insert(loc=(int(df.shape[1])), column="V12LOG", value=V12LOG)

# data frame of logaritmic values
dflog = df.filter(["M11LOG", "M1LOG","V2LOG","V12LOG"])
print(dflog)




#Heatmap creation
plt.rcParams["figure.figsize"] = (100,200)
plt.subplots(figsize=(100,100))
plt.pcolor(dflog, cmap ="inferno")
plt.colorbar()

plt.yticks(np.arange(0.5, len(dflog.index), 1), dflog.index, fontsize = 5, rotation = 45)
plt.xticks(np.arange(0.5, len(dflog.columns), 1), dflog.columns, fontsize = 10, rotation = 0)
plt.savefig("/home/linas/Documents/figure.png")
plt.show()
