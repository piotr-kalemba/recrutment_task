import pandas as pd
data_source = "2017-fordgobike-tripdata.csv"


# column_names = ["duration_sec","start_time", "end_time", "start_station_id", "start_station_name",
#                 "start_station_latitude", "start_station_longitude","end_station_id","end_station_name",
#                 "end_station_latitude","end_station_longitude","bike_id","user_type"]

df = pd.read_csv(data_source, sep=",", header=0, usecols=[0, 1, 2, 3, 4, 7, 8, 11, 12])

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

