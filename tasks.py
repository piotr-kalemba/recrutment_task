import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

data_source = "2017-fordgobike-tripdata.csv"


# column_names = ["duration_sec","start_time", "end_time", "start_station_id", "start_station_name",
#                 "start_station_latitude", "start_station_longitude","end_station_id","end_station_name",
#                 "end_station_latitude","end_station_longitude","bike_id","user_type"]

df = pd.read_csv(data_source, sep=",", header=0, usecols=[0, 1, 2, 3, 4, 7, 8, 11, 12])
df.sort_values(by=["start_time"], inplace=True)


# task_1
unique_station_ids = df["start_station_id"].unique().tolist()
print(len(unique_station_ids))
# answer=272

# task_2
min_d = df["duration_sec"].min()
max_d = df["duration_sec"].max()
minimal_duration_rows = df.loc[df["duration_sec"] == min_d]
minimal_duration_bike_ids = minimal_duration_rows["bike_id"].tolist()
print(minimal_duration_bike_ids)
maximal_duration_rows = df.loc[df["duration_sec"] == max_d]
maximal_duration_bike_ids = maximal_duration_rows["bike_id"].tolist()
print(maximal_duration_bike_ids)

# task_5

df1 = df.groupby(["start_station_id", "start_station_name", "end_station_id", "end_station_name"]).size()\
    .reset_index(name="count")
df2 = df1.loc[df1["count"] == df1["count"].max()]
print(df2[["start_station_name", "end_station_name"]])

# task_6

start_times = df["start_time"].tolist()
hours = []
dic = {}
for date in start_times:
    day, hour = date.split()
    day = day[-5:]
    hour = int(hour[:2])
    hours.append(hour)
    if day not in dic:
        dic[day] = [hour]
    else:
        dic[day].append(hour)


def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]


days = list(dic.keys())
most_freq_hour = [most_frequent(dic[day]) for day in days]


x_values = range(len(days))
y_values = most_freq_hour
plt.plot(x_values, y_values, "ob")
plt.xlabel("Days from 06-28 to 12-31")
plt.ylabel("Pick hour of the day")
plt.savefig("pick_hour.png")
