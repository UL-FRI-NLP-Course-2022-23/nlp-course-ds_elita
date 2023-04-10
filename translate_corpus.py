import translators as ts
from tqdm import tqdm
import csv
import os

# Script that translates a tab-separated file from the parabank2 dataset (tsv, first column is the score and all further columns are paraphrases, one row contains all paraphrases)
# from English to Slovene. The script saves the translations immediately and can be stopped (or can crash due to rate limits) and continued later (it automatically continues where it left off).

DATASET_PATH = "small_parabank2.tsv"
OUTPUT_PATH = "translated_small_parabank2.tsv"

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
    translated_paraphrases = []
    for paraphrases in tqdm(corpus[start_index:]):
        for paraphrase in paraphrases:
            translated_paraphrases.append(ts.translate_text(paraphrase, to_language="sl", from_language="en", translator="bing")) # bing as it is the fastest
        save_translation(out_path, translated_paraphrases)                
        translated_paraphrases = []

if __name__ == "__main__":
    ts.preaccelerate()
    start_index = 0
    if os.path.exists(OUTPUT_PATH): # Continue where you left off
        start_index = len(read_paraphrase_data(OUTPUT_PATH))
        print(f"Starting where previously left off (index {start_index})...")
    else:
        print("Starting from the beginning...")
    corpus = read_paraphrase_data(DATASET_PATH)
    translate_paraphrase_data(corpus, start_index, OUTPUT_PATH)