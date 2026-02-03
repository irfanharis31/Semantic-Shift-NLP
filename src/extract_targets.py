from collections import Counter
import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def tokenize(line):
    return re.findall(r"[a-z]+", line.lower())

def build_vocab(path, max_lines=100000):
    vocab = Counter()
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            vocab.update(tokenize(line))
    return vocab

def main():
    old_vocab = build_vocab("data/processed/old_clean.txt")
    new_vocab = build_vocab("data/processed/new_clean.txt")

    common = []
    for word in old_vocab:
        if word in new_vocab:
            if (
                old_vocab[word] > 50 and
                new_vocab[word] > 50 and
                word not in STOPWORDS and
                len(word) > 3
            ):
                common.append(word)

    common.sort()

    with open("data/processed/targets.txt", "w") as f:
        for w in common:
            f.write(w + "\n")

    print(f"Saved {len(common)} target words")

if __name__ == "__main__":
    main()
