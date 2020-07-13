This code will give the mean altitude for Eric:

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

mean_altitudes_perday.head()
