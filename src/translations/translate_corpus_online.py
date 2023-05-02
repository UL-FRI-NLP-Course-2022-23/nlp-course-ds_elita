import translators as ts
from tqdm import tqdm
import csv
import os
from fp.fp import FreeProxy
import random

# Script that translates a tab-separated file from the parabank2 dataset (tsv, first column is the score and all further columns are paraphrases, one row contains all paraphrases)
# from English to Slovene. The script saves the translations immediately and can be stopped (or can crash due to rate limits) and continued later (it automatically continues where it left off).

DATASET_PATH = "../../data/small_parabank2.tsv"
OUTPUT_PATH = "../../translated_small_parabank2.tsv"

def read_paraphrase_data(path):
    paraphrases = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            paraphrases.append(line.split("\t")[1:])
    return paraphrases

def save_translation(path, row):
    with open(path, "a") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(row)


def translate_paraphrase_data(corpus, start_index, out_path):
    proxy_list = FreeProxy(rand=True, timeout=0.5, elite=True).get_proxy_list(repeat=False)
    proxy_pool = [{"http": p} for p in proxy_list]
    print(proxy_pool)
    for paraphrases in tqdm(corpus[start_index:]):
        translated_paraphrases = [ts.translate_text(paraphrase, to_language="sl", from_language="en", translator="bing", proxies=random.choice(proxy_pool)) for paraphrase in paraphrases] # bing as it is the fastest
        save_translation(out_path, translated_paraphrases)                

if __name__ == "__main__":
    #ts.preaccelerate()
    start_index = 0
    if os.path.exists(OUTPUT_PATH): # Continue where you left off
        start_index = len(read_paraphrase_data(OUTPUT_PATH))
        print(f"Starting where previously left off (index {start_index})...")
    else:
        print("Starting from the beginning...")
    corpus = read_paraphrase_data(DATASET_PATH)
    translate_paraphrase_data(corpus, start_index, OUTPUT_PATH)