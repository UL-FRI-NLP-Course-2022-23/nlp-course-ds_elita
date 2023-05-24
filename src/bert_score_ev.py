import evaluate
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel, AutoModelForMaskedLM
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("./data/paraphrase_evaluation.tsv",delimiter='\t', header=0)
df2 = pd.read_csv("./data/translated_small_parabank2_postproc.tsv", delimeter='\t', header=0)


tokenizer = AutoTokenizer.from_pretrained("EMBEDDIA/sloberta")
model = AutoModel.from_pretrained("EMBEDDIA/sloberta")
res = []
for i in range(len(df)):
    if i % 500 == 0:
        print(i)
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

df["BERT_SCORE"] = res
df.to_csv("./new.csv", index=False)