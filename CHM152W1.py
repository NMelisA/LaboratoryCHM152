import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading values from excel
path="C://Users//Melis//Desktop//CHM152//WEEK1//CHM152W1.xlsx"
df=pd.read_excel(path)
Voltage=df["Voltage"].to_numpy()
Current=df["Current"].to_numpy()


slope=np.gradient(Current, Voltage)
second_derivative = np.gradient(slope, Voltage)
threshold_slope=np.percentile(slope, 50) 

#finding estimated resudial current value
resudial_current=np.round(np.mean(np.sort(Current[:3])),2)
#decomposition voltage
decV=np.round(Voltage[np.where(np.abs(slope)>threshold_slope)[0][0]],2)
#turning point
turning_point=np.round(Voltage[np.argmax(second_derivative)],2)

#plotting
plt.plot(Voltage, Current, color="b")
plt.scatter(Voltage, Current, color="firebrick")
plt.xlabel("Voltage(V)")
plt.ylabel("Current(mA)")
plt.title("Current Vs Voltage")
plt.show()

plt.scatter(Voltage, Current, color="firebrick")
plt.plot([turning_point, turning_point], [0,max(Current)], linestyle="--", color="r" )
plt.plot([0,max(Voltage)], [resudial_current,resudial_current], linestyle="--", color="g"  )
plt.plot([decV,decV], [0,max(Current)], linestyle="--", color="b" )
plt.xlabel("Voltage(V)")
plt.ylabel("Current(mA)")
plt.legend(["Experimental Data",f"Estimated Turning Point {turning_point}V",
        f"Estimated Resudial Current {resudial_current}mA", f"Estimated Decomposition Voltage {decV}V"],
          title="Current vs Voltage", loc="best", facecolor="white")
plt.show()