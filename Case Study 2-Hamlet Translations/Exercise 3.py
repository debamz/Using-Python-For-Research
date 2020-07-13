The number of unique words can be found using the following code:

data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

data.groupby('frequency').count()
		word	count	length
frequency			
frequent	323	323	323
infrequent	1442	1442	1442
unique		3348	3348	3348
