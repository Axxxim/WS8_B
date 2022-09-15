import matplotlib.pyplot as plt
import pandas as pd

#seting the max coumns and width for initial
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
climate = pd.read_csv("climate.csv")

years = climate['Year'].to_numpy()
co2 = climate['CO2'].to_numpy()
temp = climate['Temperature'].to_numpy()


plt.subplot(2, 1, 1)
plot(years, co2, temp) 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp.png") 

