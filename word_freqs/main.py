import csv

articles = [open("article_1.txt", "r"), open("article_2.txt", "r")]

def dict_to_csv(dict_, file_):
	with open(file_, "w") as f:
		w = csv.DictWriter(f, dict_.keys())
		w.writeheader()
		w.writerow(dict_)

for article in range(2):
	print("Article", article+1)
	article_num = article
	article = articles[article].read()
	words = article.split()
	word_len_freq = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
        16: 0
	}
	for word in words:
		if len(word) < 16:
			word_len_freq[len(word)] += 1
		else:
			word_len_freq[16] += 1

	print("Word lenghts and their respective frequencies", "\n", word_len_freq)
	print("Putting it in a file...")
	dict_to_csv(word_len_freq, "a"+str(article_num+1)+".csv")

