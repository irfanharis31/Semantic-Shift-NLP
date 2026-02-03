# Semantic Shift NLP

A reproducible research framework for detecting **diachronic lexical semantic change** in English news corpora using **contextualized transformer-based language models**.

This project implements an end-to-end pipeline for identifying and ranking words whose meanings shift across temporally separated corpora (2010–2020), combining linguistic filtering, contextual embedding generation, and cosine-based semantic displacement metrics.

---

## Research Motivation

Understanding how word meaning evolves over time is a core problem in **computational linguistics**, with applications in historical semantics, sociolinguistics, and discourse analysis. Traditional static embedding approaches struggle to model **polysemy** and **context-dependent meaning**, motivating the use of transformer-based contextualized representations.

This framework provides a reproducible and extensible pipeline for:
- Modeling semantic drift across time slices
- Identifying high-impact lexical changes
- Supporting qualitative linguistic interpretation of observed shifts

---

## Pipeline Overview

1. **Corpus Acquisition and Normalization**  
   Downloads and preprocesses temporally separated English news corpora (2010 and 2020), including token normalization and sentence filtering.

2. **Target Lexicon Construction**  
   Builds a frequency-filtered vocabulary shared across both corpora, excluding stopwords and low-frequency terms.

3. **Sentence-Level Context Extraction**  
   Extracts sentence contexts for each target word to preserve usage-level semantics.

4. **Contextual Embedding Generation**  
   Generates token-level embeddings using transformer models (BERT / DistilBERT).

5. **Semantic Drift Computation**  
   Computes cosine-based displacement between aggregated contextual representations across time slices.

6. **Qualitative and Quantitative Analysis**  
   Ranks lexical items by semantic shift magnitude and supports linguistic interpretation of meaning change.

---

## Repository Structure

