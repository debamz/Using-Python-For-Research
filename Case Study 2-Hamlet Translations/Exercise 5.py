The solution code is given here:

grouped_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])

for i in range(hamlets.shape[0]):
    language, text = hamlets.iloc[i]
    sub_data = summarize_text(language, text)
    grouped_data = grouped_data.append(sub_data)
    
grouped_data
	language	frequency	mean_word_length	num_words
frequent	English	frequent	4.371517	323
infrequent	English	infrequent	5.825243	1442
unique		English	unique	7.005675	3348
frequent	German	frequent	4.528053	303
infrequent	German	infrequent	6.481830	1596
unique		German	unique	9.006987	5582
frequent	Portuguese	frequent	4.417625	261
infrequent	Portuguese	infrequent	6.497870	1643
unique		Portuguese	unique	8.669778	5357
