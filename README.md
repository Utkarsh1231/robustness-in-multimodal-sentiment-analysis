# Modality Robustness in Multimodal Sentiment Analysis (MSA)

This repository contains the experimental framework for evaluating and improving the robustness of Multimodal Sentiment Analysis models against modality-specific failures and dominant modality bias.

## Project Scope
* [cite_start]**Reproduction:** Validated the experimental framework of benchmark research on the CMU-MOSI and CMU-MOSEL datasets[cite: 20, 23].
* [cite_start]**Diagnostic Pipeline:** Engineered a testing pipeline to introduce controlled modality errors, such as zero-masking and white Gaussian noise, into language representations[cite: 21].
* **Optimization:** Optimized model training and parameter efficiency by implementing Low-Rank Adaptation (LoRA).
* [cite_start]**Robustness:** Developed a modality-perturbation robust training loop from scratch to balance missing and noisy data streams during model training[cite: 22].

## File Structure
* `apply_lora_optimization.py`: Script to integrate LoRA weights into the multimodal transformer backbone.
* `robust_training_loop.py`: Implementation of the diagnostic noise pipeline and robust loss balancing.

## Credits & Attribution
* [cite_start]**Benchmark Methodology:** This project is a reproduction of the experimental framework for evaluating modality robustness in MSA[cite: 18, 20].
* [cite_start]**Datasets:** Performance was validated using the industry-standard **CMU-MOSI** and **CMU-MOSEL** datasets[cite: 23].
* [cite_start]**My Role:** My contributions focus on the implementation of the diagnostic noise pipeline, the integration of **Low-Rank Adaptation (LoRA)**, and the development of the robust training loop[cite: 21, 22].
