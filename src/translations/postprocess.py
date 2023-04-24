import csv
from itertools import combinations
from tqdm import tqdm

INPUT_PATH = "../../data/translated_small_parabank2.tsv"
OUTPUT_PATH = "../../data/translated_small_parabank2_postproc.tsv"



def postprocess(input_file, output_file):
    num_rows = sum(1 for _ in open(INPUT_PATH))
    with open(input_file, 'r') as in_f:
        with open(output_file, 'w') as out_f:
            reader = csv.reader(in_f, delimiter='\t')
            writer = csv.writer(out_f, delimiter='\t')
            for row in tqdm(reader, total=num_rows):
                # Remove leading and trailing spaces and remove duplicates
                row = {p.strip() for p in row} 
                # If there are at least two paraphrases for a given sentence, generate all possible pairs and save
                if len(row) > 1: 
                    writer.writerows(combinations(row, 2))


if __name__ == '__main__':
    postprocess(INPUT_PATH, OUTPUT_PATH)