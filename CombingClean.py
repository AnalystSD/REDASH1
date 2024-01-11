import pandas as pd
import csv
import panel as pn
# This needs to be able to compare two tables and only pull from the auction table properties to buy
# Meaning, pulling data of 3 props from realsetateinv to compare to 1 prop from Auction.
prosp = pd.read_csv('ProspectList.csv')
comp = pd.read_csv('complist.csv')
df1 = pd.DataFrame(prosp) #Prospects
df2 = pd.DataFrame(comp) #Comps to compare with the property in question to buy
df10 = df1.filter(items=['Address2'])
df20 = df2.filter(items=['Address2'])
df1.sort_index(inplace=True)
df2.sort_index(inplace=True)
cmps = df2.loc[0:3,'Address2']
#We only need the ones that match and are more available. Just delete the #'s to test the print.
#print(cmps)
#print(df1['Address2'])

#Getting the best property from prospectlist
#headers Address	Address2	Price	Bed	Bath	Sqft	Date	Time
df11 = df1.loc[1]
df21 = df2[df2["Address2"].isin(["Sunrise, FL 33351"])]
df22 = df21[df21.Bed.isin([2])]
print(df22) #if you test this you'll see we now got a list of comps we can use.
print(df11)
#Now we just gotta add a few things, its market value(after repairs), prerepair offer, and avg repair costs
sumcomp = df22['Price'].sum()
avgcomp = sumcomp / 2
d = {}
df00 = pd.DataFrame(index=[1])
df00['MarketV'] = avgcomp.astype(int) #assuming repairs and profit added
repairc = 40000 #assuming tons of repairs are needed (example) IN reality, an in-person inspection is needed.
df00['repairC'] = repairc
#df00 = df00.assign(repairC = repairc) #Another method that applies to each column too
profit =(avgcomp * 0.3) #assuming 30% profit
offer = avgcomp - profit - repairc
df00['offer'] = offer
df00['profit'] = profit
print(df00)

#Launch it using jupyter labs AND any help at: https://panel.holoviz.org/getting_started/index.html
