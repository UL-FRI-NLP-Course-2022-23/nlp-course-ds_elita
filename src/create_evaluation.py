import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    data = pd.read_csv("./data/translated_small_parabank2_postproc.tsv", delimiter='\t', header=0)
    train_data, temp_data = train_test_split(data, test_size=0.4, random_state=42)
    
    eval_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)
    eval_start = test_data[:1000]
    print("Vleze")
    eval_start.to_csv("./data/eval.csv")