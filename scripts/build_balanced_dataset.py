"""
Build the final balanced fine-tuning dataset by sampling per-label from the
two annotated megathreads, then make a stratified train/test split.

Sources (different schemas, same human-reviewed labels in `label`):
  - data/megathread_jun26.csv : columns [text, pre_label, label]
  - data/megathread_jun24.csv : columns [body, pre_label, label, notes]

Target distribution (200 total): Question 60, Analysis 60, Opinion 50, Information 30.
Information is the minority class (32 available combined), so 30 uses nearly all of it.

`[deleted]`/`[removed]` rows have a blank label and are dropped automatically.
"""

import csv
import random
from collections import Counter, defaultdict

# ---- knobs ------------------------------------------------------------------
SEED = 42                     # reproducible "random" sampling
LABEL_COL = "label"           # human-reviewed labels
TARGETS = {                   # per-class counts in the final dataset
    "Question": 60,
    "Analysis": 60,
    "Opinion": 50,
    "Information": 30,
}
TEST_FRAC = 0.20              # stratified holdout fraction

SOURCES = [
    ("data/megathread_jun26.csv", "text"),
    ("data/megathread_jun24.csv", "body"),
]
OUT_ALL   = "data/balanced_dataset.csv"
OUT_TRAIN = "data/train.csv"
OUT_TEST  = "data/test.csv"
# -----------------------------------------------------------------------------


def load(path, text_field):
    """Return list of (text, label) for rows with a non-blank label."""
    with open(path, encoding="utf-8", newline="") as f:
        out = []
        for row in csv.DictReader(f):
            label = (row.get(LABEL_COL) or "").strip()
            text = (row.get(text_field) or "").strip()
            if label in TARGETS and text:
                out.append((text, label))
        return out


def main():
    rng = random.Random(SEED)

    # 1) combine both threads, dedupe identical texts (keep first seen)
    pool, seen = [], set()
    for path, field in SOURCES:
        for text, label in load(path, field):
            if text not in seen:
                seen.add(text)
                pool.append((text, label))

    by_label = defaultdict(list)
    for text, label in pool:
        by_label[label].append(text)

    print("combined pool:", {k: len(by_label[k]) for k in TARGETS})

    # 2) random sample the target count per label
    sampled = []
    for label, want in TARGETS.items():
        texts = by_label[label][:]
        rng.shuffle(texts)
        if len(texts) < want:
            raise SystemExit(
                f"ERROR: {label} has only {len(texts)} examples but {want} requested. "
                f"Collect more {label} or lower its target."
            )
        sampled += [(t, label) for t in texts[:want]]

    # 3) stratified train/test split (split each label independently)
    train, test = [], []
    for label in TARGETS:
        rows = [r for r in sampled if r[1] == label]
        rng.shuffle(rows)
        n_test = round(len(rows) * TEST_FRAC)
        test += rows[:n_test]
        train += rows[n_test:]
    rng.shuffle(train)
    rng.shuffle(test)

    # 4) write
    for path, data in [(OUT_ALL, sampled), (OUT_TRAIN, train), (OUT_TEST, test)]:
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["text", "label"])
            w.writerows(data)

    print("balanced total:", len(sampled), dict(Counter(l for _, l in sampled)))
    print("train:", len(train), dict(Counter(l for _, l in train)))
    print("test :", len(test),  dict(Counter(l for _, l in test)))


if __name__ == "__main__":
    main()
