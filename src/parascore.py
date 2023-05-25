#
import evaluate
import pandas as pd
import numpy as np
import math
"""
print("Vleze")
df = pd.read_csv("./data/translated_small_parabank2_postproc.tsv", delimiter='\t', header=0)
df = df[:int(0.6*len(df))]
rouge = evaluate.load("rouge")
references = df["2004 Ocean Cup narodov"].to_list()
preds = df["Ocean Cup narodov 2004"].to_list()

res = rouge.compute(references=references, predictions=preds)

print(res)
print("Izleze")
"""
rouge = evaluate.load("transZ/test_parascore")
df = pd.read_csv("./data/evaluation_old_model.csv")
arr = []

references = df["0"].to_list()
preds = df["1"].to_list()

res = rouge.compute(references=references, predictions=preds)

arr = np.array(res["score"])

print(np.mean(arr))
print(np.std(arr))

df = pd.read_csv("./data/evaluation_new_model.csv")

arr = []

references = df["0"].to_list()
preds = df["1"].to_list()

res = rouge.compute(references=references, predictions=preds)

arr = np.array(res["score"])

print(np.mean(arr))
print(np.std(arr))



df = pd.read_csv("./data/eval.csv")
arr = []

references = df["2004 Ocean Cup narodov"].to_list()
preds = df["Ocean Cup narodov 2004"].to_list()

res = rouge.compute(references=references, predictions=preds)

arr = np.array(res["score"])

print(np.mean(arr))
print(np.std(arr))






