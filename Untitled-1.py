#%%
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
import seaborn as sns


registry_data = pd.read_csv("https://raw.githubusercontent.com/huizhangky/CSE590/main/hw/hw2/subject_registry.csv")
timezone_data = pd.read_csv("https://raw.githubusercontent.com/huizhangky/CSE590/main/hw/hw2/subject_timezone_log.csv")

registry_data = registry_data[registry_data["ISA"] == "BP03"]
registry_data = registry_data[registry_data["Actual_Visit"] != "SF"]
registry_data = registry_data[registry_data["Actual_Visit"] != "ED"]

combined_data = registry_data.merge(timezone_data, left_on="SubjectID", right_on="subject")

idx = []
cols = []

for subj in registry_data.SubjectID:
    idx.append(subj)
    
for i in range(1,67):
    cols.append(i)

df = pd.DataFrame(combined_data)

df = df.reset_index()

#df.to_csv("C:\\School\\CS551\\df.csv")

data = []

for index, row in df.iterrows():
    start_date = row['Data_collection_started']
    time_diff = timedelta(days=67)
    for i in range(start_date, start_date+time_diff):
        print(row['timestamp_iso'])
    #for i in range(1,67):
        #tz_values = row['time_offset']
        #data.append({"subject":row['SubjectID'], "day":i, "timezone":(tz_values/3600)})

df1 = pd.DataFrame(data)

df2 = df1[["subject","day","timezone"]]
x = pd.DataFrame(df1['day'].unique())
heatmap_pt = pd.pivot_table(df2,values ='timezone', index=['subject'], columns='day')
heatmap_pt

sns.set()
plt.figure(figsize=(10,6))
sns.heatmap(df2.pivot_table(index='subject', columns='day', values='timezone', aggfunc='first'), cmap='tab20')

plt.show()
# %%
