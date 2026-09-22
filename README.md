# Natural Language Processing (NLP) - S2 Informatics

Repository final untuk pembelajaran **Natural Language Processing** jenjang S2.

Course ini menggunakan pendekatan **learning-by-doing + project-based learning**. Tidak ada kuis, UTS, atau UAS terpisah. Kompetensi dibangun melalui laboratory, mini-project, eksperimen, error analysis, dan satu final project yang berkembang dari minggu ke minggu.

## Learning loop

**Understand → Inspect → Implement → Experiment → Evaluate → Explain → Improve**

## Roadmap 16 Pertemuan

| Minggu | Fokus | Produk |
|---|---|---|
| 01 | NLP, pipeline, tokenization | Tokenization Lab |
| 02 | Normalization & preprocessing | Reproducible preprocessing |
| 03 | Syntax, POS, parsing | Syntax Lab |
| 04 | Semantics & similarity | Similarity Lab |
| 05 | Vector space & embeddings | Retrieval/embedding mini-project |
| 06 | Statistical language modeling | n-gram LM |
| 07 | Text classification | Classification baseline |
| 08 | NER & sequence labeling | NER baseline |
| 09 | Machine learning/deep learning for NLP | Model comparison |
| 10 | Evaluation & error analysis | Model audit |
| 11 | Final project: problem & data | Proposal + data card |
| 12 | Final project: baseline | First working system |
| 13 | Final project: experiments | Multi-model comparison |
| 14 | Final project: analysis | Error analysis + improvement |
| 15 | Final project: presentation | Scientific presentation |
| 16 | Final project: release | Reproducible GitHub release |

## Repository structure

Setiap minggu idealnya memiliki:
- `materi.md` - bahan bacaan,
- `README.md` - petunjuk aktivitas,
- `.ipynb` - guided laboratory,
- `reflection.md` - refleksi mahasiswa.

## Dataset

Dataset BBC News dan dataset NER dari repository praktikum sebelumnya dipertahankan sebagai dataset pembelajaran. Untuk final project mahasiswa memilih dataset sendiri dengan dokumentasi sumber, lisensi, distribusi, dan ethical considerations.

## Instalasi

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

Untuk Transformer:
```bash
pip install -r requirements-transformers.txt
```

## Referensi inti

- Jurafsky & Martin, *Speech and Language Processing*, 3rd ed.
- Manning & Schütze, *Foundations of Statistical Natural Language Processing*.
