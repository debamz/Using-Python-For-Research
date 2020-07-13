The following code will create the new column and allow you to figure out the number of red wines:

data["is_red"] = (data["color"] == "red").astype(int)
numeric_data = data.drop(["color", "high_quality", "quality"], axis=1)

numeric_data.groupby('is_red').count()
