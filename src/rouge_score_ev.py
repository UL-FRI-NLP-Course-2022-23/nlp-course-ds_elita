import evaluate
import pandas as pd

df = pd.read_csv("./data/paraphrase_evaluation.tsv",delimiter='\t', header=0)

rouge = evaluate.load("rouge")
references = df["0"].to_list()
preds = df["1"].to_list()

res = rouge.compute(references=references, predictions=preds)

print(res)
#{'rouge1': 0.7283420257160238, 'rouge2': 0.5799825126255123, 'rougeL': 0.702052156245857, 'rougeLsum': 0.7018812556579996}