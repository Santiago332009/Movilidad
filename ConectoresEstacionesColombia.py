import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("EstacionesDeCargaColombia.csv")

keys=df.keys()

TypeConnector=keys[2]
Qty=keys[3]

Connector=list(df[TypeConnector])
Qtys=list(df[Qty])

Conectores=[]

for i in Connector:
    if i not in Conectores:
        Conectores.append(i)

NumConectores=[]
for i in Conectores:
    mascara=df[TypeConnector]==i
    NumConectores.append(sum(df[Qty]*mascara))
'''
sns.barplot(Conectores,NumConectores)
plt.ylabel("Qty Conectores Colombia")
plt.xlabel("Tipo de conector")
plt.title("Tipo de conectores EV en Colombia")
plt.grid()
plt.show()'''

Total=sum(NumConectores)

Num=pd.Series(NumConectores)
NumPorcen=Num/Total*100

sns.barplot(Conectores,NumPorcen)
plt.title(r"$Tipo\ de\ conectores\ EV\ en\ Colombia$")
plt.show()
