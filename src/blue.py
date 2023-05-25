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
rouge = evaluate.load("bleu")
df = pd.read_csv("./data/evaluation_old_model.csv")
arr = []
for i in range(len(df)):
   
    references = [df["0"][i]]
    preds = [df["1"][i]]
    if not isinstance(df["1"][i], str):
        continue
    res = rouge.compute(references=references, predictions=preds)
    arr.append(res["bleu"])
arr = np.array([arr])

print(np.mean(arr))
print(np.std(arr))

df = pd.read_csv("./data/evaluation_new_model.csv")

arr = []
for i in range(len(df)):
    
    references = [df["0"][i]]
    preds = [df["1"][i]]
    if not isinstance(df["1"][i], str):
        continue
    res = rouge.compute(references=references, predictions=preds)
    arr.append(res["bleu"])
arr = np.array([arr])

print(np.mean(arr))
print(np.std(arr))

df = pd.read_csv("./data/eval.csv")
arr = []
for i in range(len(df)):
   
    references = [df["2004 Ocean Cup narodov"][i]]
    preds = [df["Ocean Cup narodov 2004"][i]]
    if not isinstance(df["Ocean Cup narodov 2004"][i], str):
        continue
    res = rouge.compute(references=references, predictions=preds)
    arr.append(res["bleu"])
arr = np.array([arr])

print(np.mean(arr))
print(np.std(arr))






#{'rouge1': 0.7283420257160238, 'rouge2': 0.5799825126255123, 'rougeL': 0.702052156245857, 'rougeLsum': 0.7018812556579996}