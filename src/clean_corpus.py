import os

def clean_line(line):
    line = line.strip()
    if len(line) < 20:
        return None
    return line

def process(input_path, output_path, max_lines=200000):
    os.makedirs("data/processed", exist_ok=True)

    count = 0
    with open(input_path, "r", encoding="utf-8", errors="ignore") as fin, \
         open(output_path, "w", encoding="utf-8") as fout:

        for line in fin:
            clean = clean_line(line)
            if clean:
                fout.write(clean + "\n")
                count += 1

            if count >= max_lines:
                break

    print(f"Saved {count} cleaned sentences to {output_path}")

if __name__ == "__main__":
    process("data/raw/old.txt", "data/processed/old_clean.txt")
    process("data/raw/new.txt", "data/processed/new_clean.txt")
