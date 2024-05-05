from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import tqdm

model = SentenceTransformer("moka-ai/m3e-base")
d = 768  # dimension
index = faiss.IndexFlatL2(d)  # build the index
database_list = []
with open("./data/honglou-book.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        database_list.append(json.loads(line)["content"])
for i in tqdm.tqdm(range(0, len(lines), 200)):
    cur_list = database_list[i : i + 200]
    index.add(model.encode(cur_list).reshape(-1, 768))

print(index.ntotal)
faiss.write_index(index, "./database/honglou-index")
