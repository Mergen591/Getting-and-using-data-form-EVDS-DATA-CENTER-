import matplotlib.pyplot as plt                        # firtly, please install and import all of library..(include evds)
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import seaborn as sns

from evds import evdsAPI

evds = evdsAPI('Use your API key, and get from EVDS DATA Center ')    # 1st step
                                                                    # 2nd step, find your series code, and use'evds.main_categories - evds.get_sub_categories-evds.get_series' for example(TP.KREDI.L001)


df = evds.get_data(['TP.KREDI.L001'], 
                   startdate="01-01-2019", enddate="24-10-2022", 
                   
                   )

#x = df['Tarih']                                                          # Another codes are optional, its up to you, and determine your codes and use color and label or tittle name.
#y = df["TP_KREDI_L001"]
#fig = plt.figure()
#ax = fig.add_subplot(111)

#ax.grid(axis='y', linestyle='--')

#plt.plot(x,y, label = "Total Loan")
#plt.legend()

df['TP_KREDI_L001'] = df['TP_KREDI_L001'].ffill()
df['Tarih'] = pd.to_datetime(df['Tarih'],dayfirst=True)

x = df['Tarih']
y = (df["TP_KREDI_L001"]/1000)

fig, ax = plt.subplots()
                                 
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
plt.xticks(rotation=40, fontsize=8)

plt.plot(x,y, label='Toplam Kredi')
plt.title("weekly loan")
plt.xlabel("Date")
plt.ylabel("Volume")

ax.legend(loc="upper right",prop={'size': 3.5})

ax.xaxis.set_major_locator(ticker.MultipleLocator(120))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y/%m"))


plt.setp( ax.xaxis.get_majorticklabels(), rotation=45, fontsize='6' )
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#C0C0C0')

plt.legend()