import pandas as pd


df = pd.read_csv("./data/paraphrase_evaluation.tsv",delimiter='\t', header=0)
n = int(len(df))
avg_sen_w_r = 0
avg_w_char_p = 0
min_w_char_r = 1e9
min_sen_w_p = 1e9
max_sen_w_r = 0
max_w_char_p = 0
avg_sen_w_p = 0
avg_w_char_r = 0
min_w_char_p = 1e9
min_sen_w_r = 1e9
max_sen_w_p = 0
max_w_char_r = 0
all_word_r = 0
all_word_p = 0
for i in range(n):
    if not isinstance(df["0"][i], str):
        continue
    if not isinstance(df["1"][i], str):
        continue
    k = df["0"][i].split(" ")
    for x in k:
        if len(x) == 0:
            k.remove(x)
    avg_sen_w_r += len(k)
    all_word_r += len(k)
    min_sen_w_r = min(min_sen_w_r, len(k))
    max_sen_w_r = max(max_sen_w_r, len(k))

    for x in k:
        avg_w_char_r += len(x)
        min_w_char_r = min(min_w_char_r, len(x))
        max_w_char_r = max(max_w_char_r, len(x))

    k = df["1"][i].split(" ")
    for x in k:
        if len(x) == 0:
            k.remove(x)
    avg_sen_w_p += len(k)
    all_word_p += len(k)
    min_sen_w_p = min(min_sen_w_p, len(k))
    max_sen_w_p = max(max_sen_w_p, len(k))
    for x in k:
        avg_w_char_p += len(x)
        min_w_char_p = min(min_w_char_p, len(x))
        max_w_char_p = max(max_w_char_p, len(x))

print("Avg word in sentence", avg_sen_w_r/n, avg_sen_w_p/n)
print("Avg chars in word", avg_w_char_r/all_word_r, avg_w_char_p/all_word_p)
print("Min word in sentence", min_sen_w_r, min_sen_w_p)
print("Min chars in word", min_w_char_r, min_w_char_p)
print("Max word in sentence", max_sen_w_r, max_sen_w_p)
print("Max chars in word", max_w_char_r, max_w_char_p)