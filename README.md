# Modality Robustness in Multimodal Sentiment Analysis

This repository contains my reproduction and optimization of Multimodal Sentiment Analysis (MSA) benchmarks. 

## Project Scope
* [cite_start]**Reproduction:** Validated the experimental framework of benchmark research on CMU-MOSI datasets[cite: 52].
* [cite_start]**Optimization:** Integrated Low-Rank Adaptation (LoRA) to reduce the trainable parameter count while maintaining modality robustness.
* [cite_start]**Robustness Testing:** Engineered a diagnostic pipeline to evaluate model performance under controlled modality noise (Gaussian/Zero-masking)[cite: 50].

## How to Run
This project utilizes the `peft` and `transformers` libraries to apply LoRA weights to the multimodal backbone.
