import pandas as pd
import random

def eval(dataframe, col_sent, col_para):
    sentence = []
    paraphrased = []
    grade = []

    for i in random.sample(range(len(dataframe)), min(100, int(len(dataframe)))):
        print("Oceni besedile", "", dataframe[col_sent], " " ,dataframe[col_para])
        note = int(input())

        grade.append(note)
        paraphrased.append(dataframe[i][col_para])
        sentence.append(dataframe[i][col_sent])
    
    dict = {
        "sentence" : sentence,
        "paraphrased" : paraphrased,
        "grade" : grade
    }

    dict.to_csv("./evaluation.csv")

if __name__ == "__main__":
    df = pd.read_csv("./data/translated_small_parabank2_postproc.tsv", sep=";")
    print(df)
