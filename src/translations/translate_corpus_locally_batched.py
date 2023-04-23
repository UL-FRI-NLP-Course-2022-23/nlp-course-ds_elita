from tqdm import tqdm
import csv
import os
from requests.sessions import Session

from itertools import chain

# Script that translates a tab-separated file from the parabank2 dataset (tsv, first column is the score and all further columns are paraphrases, one row contains all paraphrases)
# from English to Slovene. The script saves the translations immediately and can be stopped (or can crash due to rate limits) and continued later (it automatically continues where it left off).
# Uses Slovene BMT API locally (NeMO finetuned on english-slovenian pair)

DATASET_PATH = "../../data/parabank2.tsv"
OUTPUT_PATH = "../../data/translated_parabank2.tsv"
BASE_API_URL = "http://localhost:4000"


def translate_paraphrases_batch(batch, session):
    flat_batch = list(chain.from_iterable(batch))
    req = {
        "src_language": "en",
        "tgt_language": "sl",
        "text": flat_batch
    }
    with session.post(f"{BASE_API_URL}/api/translate", json=req) as res:
        return res.json()["result"]

# Given a flat batch (array of strings), and split_ixs (how many strings belong into a single row), return rows.
# I.e. for flat_batch=["a", "b", "c", "d"] and split_ixs=[1,2,1]. The result is [["a"], ["b", "c"], ["d"]]
def rowify(flat_batch, split_ixs):
    result = []
    for ix in split_ixs:
        row = flat_batch[:ix]
        if len(row) > 0:
            result.append(row)
        flat_batch = flat_batch[ix:]
    return result

def save_translated_rows(path, rows):
    with open(path, "a") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(rows)

def process_dataset(ix, in_path, out_path, batch_char_limit=4800):
    with open(in_path) as f:
        batch = []
        split_ixs = []
        batch_size = 0
        with Session() as session:
            for row_ix, line in enumerate(tqdm(f)):
                # Skip to where we left off
                if row_ix < ix:
                    continue

                if (row_ix + 1) % 1000 == 0:
                    print(row_ix + 1, "rows translated")

                # Read a single line and turn it into an array of paraphrases
                line = line.strip()
                split_data = line.split("\t")[1:]  # Ignore the first column as that's just the score
                
                # If this line would make the batch too long for the API, translate the current batch, save it, and put the line into the next batch
                line_len = len("".join(split_data))
                if (batch_size + line_len) > batch_char_limit:
                    translated = translate_paraphrases_batch(batch, session)
                    save_translated_rows(out_path, rowify(translated, split_ixs))
                    split_ixs = []
                    batch = []
                    batch_size = 0
                    
                split_ixs.append(len(split_data))
                batch.append(split_data)
                batch_size += line_len
                if (row_ix) > 1000:
                    break
if __name__ == "__main__":
    start_index = 0
    if os.path.exists(OUTPUT_PATH): # Continue where you left off
        start_index = sum(1 for _ in open(OUTPUT_PATH))
        print(f"Starting where previously left off (index {start_index})...")
    else:
        print("Starting from the beginning...")
    process_dataset(start_index, DATASET_PATH, OUTPUT_PATH)