from tqdm import tqdm
import csv
import os
import requests
from requests.sessions import Session
# Script that translates a tab-separated file from the parabank2 dataset (tsv, first column is the score and all further columns are paraphrases, one row contains all paraphrases)
# from English to Slovene. The script saves the translations immediately and can be stopped (or can crash due to rate limits) and continued later (it automatically continues where it left off).
# Uses Slovene NMT model (NeMO trained on en-sl pairs) locally for translation

DATASET_PATH = "../../data/parabank2.tsv"
OUTPUT_PATH = "../../data/translated_parabank2.tsv"

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
    with Session() as session:
        for paraphrases in tqdm(corpus[start_index:]):
            req = {
                "src_language": "en",
                "tgt_language": "sl",
                "text": paraphrases
            }
            res = session.post("http://localhost:4000/api/translate", json=req).json()
            translated_paraphrases = res["result"]
            save_translation(out_path, translated_paraphrases)                

if __name__ == "__main__":
    start_index = 0
    if os.path.exists(OUTPUT_PATH): # Continue where you left off
        start_index = len(read_paraphrase_data(OUTPUT_PATH))
        print(f"Starting where previously left off (index {start_index})...")
    else:
        print("Starting from the beginning...")
    corpus = read_paraphrase_data(DATASET_PATH)
    translate_paraphrase_data(corpus, start_index, OUTPUT_PATH)