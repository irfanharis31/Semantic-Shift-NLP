import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from tqdm import tqdm

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_NAME = "distilbert-base-uncased"
BATCH_SIZE = 16

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME).to(DEVICE)
model.eval()

def load_contexts(path):
    data = defaultdict(list)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t", 1)
            if len(parts) == 2:
                word, sentence = parts
                data[word].append(sentence)
    return data

def embed_batch(sentences):
    inputs = tokenizer(
        sentences,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=128
    )
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state.mean(dim=1).cpu().numpy()

def mean_embedding(sentences):
    vecs = []
    for i in range(0, len(sentences), BATCH_SIZE):
        batch = sentences[i:i + BATCH_SIZE]
        vecs.append(embed_batch(batch))
    return np.mean(np.vstack(vecs), axis=0).reshape(1, -1)

def main():
    print("Loading contexts...")
    old_data = load_contexts("data/contexts/old_contexts.tsv")
    new_data = load_contexts("data/contexts/new_contexts.tsv")

    results = []

    print("Computing semantic shifts...")
    for word in tqdm(old_data):
        if word not in new_data:
            continue

        old_vec = mean_embedding(old_data[word])
        new_vec = mean_embedding(new_data[word])

        score = 1 - cosine_similarity(old_vec, new_vec)[0][0]
        results.append((word, score))

    results.sort(key=lambda x: x[1], reverse=True)

    with open("results/semantic_shift.txt", "w") as f:
        for w, s in results[:100]:
            f.write(f"{w}\t{s:.4f}\n")

    print("Top 100 semantic shifts saved to results/semantic_shift.txt")

if __name__ == "__main__":
    main()
