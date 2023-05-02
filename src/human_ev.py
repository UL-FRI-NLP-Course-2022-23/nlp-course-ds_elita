import pandas as pd
import random

def eval(dataframe):
    sentence = []
    paraphrased = []
    grade = []

    for i in random.Random(0).sample(range(len(dataframe)), min(100, int(len(dataframe)))):
        print("Oceni besedili", "\n  ", dataframe.iloc[i, 1], "\n  " ,dataframe.iloc[i, 2])
        note = int(input())

        grade.append(note)
        paraphrased.append(dataframe.iloc[i, 2])
        sentence.append(dataframe.iloc[i, 1])
    
    dict = {
        "sentence" : sentence,
        "paraphrased" : paraphrased,
        "grade" : grade
    }

    df = pd.DataFrame(dict, columns=["sentence", "paraphrased", "grade"])
    return df
    

if __name__ == "__main__":
    df = pd.read_csv("./data/paraphrase_evaluation.tsv", delimiter='\t', header=0)
    df = eval(df)
    df.to_csv("./evaluation.csv", index=False)
    print(df["grade"].mean())
    
