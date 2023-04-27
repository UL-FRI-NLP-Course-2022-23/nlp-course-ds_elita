import pandas as pd
import random

def eval(dataframe):
    sentence = []
    paraphrased = []
    grade = []

    for i in random.Random(0).sample(range(len(dataframe)), min(100, int(len(dataframe)))):
        print("Oceni besedile", "", dataframe.iloc[i, 0], " " ,dataframe.iloc[i, 1])
        note = int(input())

        grade.append(note)
        paraphrased.append(dataframe.iloc[i, 1])
        sentence.append(dataframe.iloc[i, 0])
    
    dict = {
        "sentence" : sentence,
        "paraphrased" : paraphrased,
        "grade" : grade
    }

    df = pd.DataFrame(dict, columns=["sentence", "paraphrased", "grade"])
    return df
    

if __name__ == "__main__":
    df = pd.read_csv("./data/translated_small_parabank2_postproc.tsv", delimiter='\t', header=0)
    df = eval(df)
    df.to_csv("./evaluation.csv", index=False)
