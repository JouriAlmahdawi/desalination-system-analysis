# تحميل المكتبات 
import pandas as pd
import matplotlib.pyplot as plt

# بيانات نظام التحلية
data = {
    "Salinity_ppm": [5000, 8000, 12000, 15000, 18000, 22000, 26000, 30000, 33000, 35000],
    "Osmotic_Pressure_bar": [4, 6, 9, 11, 13, 16, 19, 22, 24, 26],
    "Operating_Pressure_bar": [12, 15, 20, 24, 28, 34, 40, 48, 55, 60],
    "Energy_kWh": [1.8, 2.1, 2.8, 3.2, 3.8, 4.5, 5.3, 6.4, 7.1, 7.8],
    "Production_m3_day": [52, 55, 59, 63, 66, 70, 73, 75, 76, 77]
}
#تحويل البيانات الى جدول
df=pd.DataFrame(data)
#عرض البيانات
print(data)
# حساب كفاءة المياه
df['Efficiency']=df["Production_m3_day"]/df["Energy_kWh"]
print(df)

print(df.corr())

plt.scatter(df[ "Salinity_ppm"],df["Osmotic_Pressure_bar"])
plt.xlabel("Salinity_ppm")
plt.ylabel("Osmotic_Pressure_bar")
plt.title('Effect of Salinity on Osmotic Pressure')
plt.figure()

plt.scatter(df["Operating_Pressure_bar"],df["Production_m3_day"])
plt.xlabel("Operating_Pressure_bar")
plt.ylabel("Production_m3_day")
plt.title('Operating Pressure vs Water Production')
plt.figure()

plt.scatter(df[ "Energy_kWh"],df["Production_m3_day"])
plt.xlabel( "Energy_kWh")
plt.ylabel("Production_m3_day")
plt.title('Energy Consumption vs Water Production')
plt.figure()

plt.plot(df[ "Operating_Pressure_bar"],df['Efficiency'])
plt.xlabel("Operating_Pressure_bar")
plt.ylabel('Efficiency')
plt.title('RO System Efficiency vs Operating Pressure')
plt.show()

