sub_data = pd.DataFrame({
    "language": language,
    "frequency": ["frequent","infrequent","unique"],
    "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
    "num_words": data.groupby(by = "frequency").size()
})

sub_data
	language	frequency	mean_word_length	num_words
frequency				
frequent	English	frequent	4.371517	323
infrequent	English	infrequent	5.825243	1442
unique		English	unique	7.005675	3348
