import pandas as pd
import matplotlib.pyplot as plt 
data =  pd.read_csv("temps_de_consommationD.csv")
x = data.x
y = data.temps_cpu
plt.plot(x,y) 
plt.show()
