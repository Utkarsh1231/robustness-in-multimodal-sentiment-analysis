# ML-Guided Search Space Pruning for ASIC Technology Mapping

This repository contains a high-performance C-based implementation of a Machine Learning "Scout" integrated into the UC Berkeley ABC logic synthesis compiler. The system uses a Bilinear Cross-Attention mechanism to optimize the search space during technology mapping.

## Technical Highlights
* **Early-Rejection Scout:** Deployed a Bilinear Cross-Attention mechanism directly inside the ABC compiler to predict the structural compatibility of graph cuts before merging.
* **Quantized Execution:** Model weights are quantized into integers to achieve nanosecond latency, enabling real-time O(1) search space pruning without floating-point overhead.
* **Feature Engineering:** Utilizes an 8-element structural embedding (Size, Depth, XOR Density, Complexity, etc.) to identify globally superior logic paths.
* **Efficiency:** Successfully eliminated over 2.28 million redundant structural merges across arithmetic benchmarks with zero logic degradation.
* **Results:** Achieved matching or improved area/delay metrics while eliminating ~35% of computational exploration.

## File Structure
* `ai_pruning_scout.c`: Core logic for the quantized attention predictor and the structural guardrail.

## Credits & Attribution
* **Original Framework:** This implementation is designed for integration with the UC Berkeley ABC open-source logic synthesis and verification system.
* **Research Basis:** The Bilinear Cross-Attention logic and quantization parameters are based on my M.Tech research at IIT Guwahati.
* **My Role:** I engineered the early-rejection predictor, optimized the weight matrix for C-level execution, and validated the pruning efficacy against EPFL benchmarks.
