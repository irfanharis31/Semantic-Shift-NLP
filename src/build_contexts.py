import os

def load_targets():
    with open("data/processed/targets.txt") as f:
        return set(w.strip() for w in f)

def extract_contexts(input_path, output_path, targets, max_per_word=50):
    os.makedirs("data/contexts", exist_ok=True)

    counts = {w: 0 for w in targets}

    with open(input_path, "r", encoding="utf-8") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:

        for line in fin:
            words = line.lower().split()
            for w in words:
                if w in targets and counts[w] < max_per_word:
                    fout.write(f"{w}\t{line.strip()}\n")
                    counts[w] += 1

    print(f"Saved contexts to {output_path}")

def main():
    targets = load_targets()

    extract_contexts(
        "data/processed/old_clean.txt",
        "data/contexts/old_contexts.tsv",
        targets
    )

    extract_contexts(
        "data/processed/new_clean.txt",
        "data/contexts/new_contexts.tsv",
        targets
    )

if __name__ == "__main__":
    main()
