from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "text_classification" / "bbc"
OUT = ROOT / "data" / "text_classification" / "News_dataset.csv"
rows=[]
for category_dir in sorted(p for p in DATA_DIR.iterdir() if p.is_dir()):
    for txt in sorted(category_dir.glob("*.txt")):
        rows.append({"file_name":txt.name,"content":txt.read_text(encoding="utf-8",errors="ignore"),"category":category_dir.name})
df=pd.DataFrame(rows)
df.to_csv(OUT,index=False,encoding="utf-8")
print(df["category"].value_counts())
print(f"Saved: {OUT}")
