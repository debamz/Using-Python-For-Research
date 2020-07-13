language, text = hamlets.iloc[0]

counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values())
})

data.head(10)
word	count
0	the	935
1	tragedie	3
2	of	576
3	hamlet	97
4		45513
5	actus	2
6	primus	1
7	scoena	1
8	prima	1
9	enter	80
