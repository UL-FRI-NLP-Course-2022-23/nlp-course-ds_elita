import evaluate
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
"""
df = pd.read_csv("./data/evaluation_old_model.csv")


tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/sloberta")
model = AutoModel.from_pretrained("EMBEDDIA/sloberta")
res = []
for i in range(len(df)):
    #rint(i)
    references = str(df["0"][i])
    tokens_ref = tokenizer(references, return_tensors="pt")

    predictions = str(df["1"][i])
    tokens_pred = tokenizer(predictions, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**tokens_ref)
        embeddings_ref = outputs.last_hidden_state.mean(dim=1).squeeze()
        outputs = model(**tokens_pred)
        embeddings_pred = outputs.last_hidden_state.mean(dim=1).squeeze()
        res.append(cosine_similarity(embeddings_ref.reshape((1, -1)), embeddings_pred.reshape((1, -1)))[0][0])

res = np.array(res)

print(np.mean(res))
print(np.std(res))
df = pd.read_csv("./data/evaluation_new_model.csv")


res = []
for i in range(len(df)):
    references = str(df["0"][i])
    tokens_ref = tokenizer(references, return_tensors="pt")

    predictions = str(df["1"][i])
    tokens_pred = tokenizer(predictions, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**tokens_ref)
        embeddings_ref = outputs.last_hidden_state.mean(dim=1).squeeze()
        outputs = model(**tokens_pred)
        embeddings_pred = outputs.last_hidden_state.mean(dim=1).squeeze()
        res.append(cosine_similarity(embeddings_ref.reshape((1, -1)), embeddings_pred.reshape((1, -1)))[0][0])

res = np.array(res)

print(np.mean(res))
print(np.std(res))
"""
df = pd.read_csv("./data/eval.csv")


tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/sloberta")
model = AutoModel.from_pretrained("EMBEDDIA/sloberta")
res = []
for i in range(len(df)):

    references = str(df["2004 Ocean Cup narodov"][i])

    tokens_ref = tokenizer(references, return_tensors="pt")

    predictions = str(df["Ocean Cup narodov 2004"][i])
    tokens_pred = tokenizer(predictions, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**tokens_ref)
        embeddings_ref = outputs.last_hidden_state.mean(dim=1).squeeze()
        outputs = model(**tokens_pred)
        embeddings_pred = outputs.last_hidden_state.mean(dim=1).squeeze()
        res.append(cosine_similarity(embeddings_ref.reshape((1, -1)), embeddings_pred.reshape((1, -1)))[0][0])

res = np.array(res)

print(np.mean(res))
print(np.std(res))