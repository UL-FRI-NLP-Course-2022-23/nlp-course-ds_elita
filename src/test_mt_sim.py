import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from Levenshtein import distance
from datasets import load_dataset

dataset = load_dataset("cjvt/rsdo4_en_sl")

model = SentenceTransformer('bert-base-nli-mean-tokens')
# sentences = base
# sentences.extend(phrases)
# sentence_embeddings = model.encode(sentences)
# sim = cosine_similarity([sentence_embeddings[0]],sentence_embeddings[1:])


def datasetdict_to_numpy(d):
	arr = []
	for i in range(len(d)):
		t = d[i]
		arr.append([t["en_seq"], t["sl_seq"]])
		if i > 10000:
			break
	return np.array(arr)


data = datasetdict_to_numpy(dataset["train"])
emb = model.encode(data[:,0])
sim_mat = cosine_similarity(emb,emb)
np.fill_diagonal(sim_mat,0)
I,J = np.where(sim_mat>0.9)

k=0
for i in range(len(I)):
	s1 = data[I[i],0]
	s2 = data[J[i],0]
	if distance(s1,s2)>1 and len(s1)+len(s2)>8 and not("XX" in s1) and not("XI" in s1):
		k+=1
		print(data[I[i],:], "\n", data[J[i],:])
		print()
