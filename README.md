[//]: # (# USB: A Comprehensive and Unified Safety Evaluation Benchmark for Multimodal Large Language Models)

<p align="center">
  <img src="image/title.png" width="800px"/>
</p>

<div align="center">
  <a href="https://arxiv.org/abs/2505.23793">📝 Paper</a> •
  <a href="https://huggingface.co/datasets/cgjacklin/USB/tree/main">🤗 Dataset</a> •
  <a href="https://anonymous.4open.science/r/USB-SafeBench-4EE3">💻 Code</a> •
  <a href="https://hongqiong12.github.io/usb_for_leadboard/">🏆 Leaderboard</a>
</div>

## 👀 About USB-SafetyBench
![Safety-Evaluation](https://img.shields.io/badge/Task-Safety--Evaluation-brown) 
![Multi-Modal](https://img.shields.io/badge/Task-Multi--Modal-red) 
![USB](https://img.shields.io/badge/Dataset-USB-blue)   
![GPT-4](https://img.shields.io/badge/Model-GPT-mediumseagreen) 
![Gemini-Pro](https://img.shields.io/badge/Model-Gemini-darkmagenta)
![Claude-3](https://img.shields.io/badge/Model-Claude-peru)  ![Claude-3](https://img.shields.io/badge/Model-Qwen-blue)  

USB is an advanced safety benchmark for Multimodal Large Language Models (MLLMs) that offers:

- **Modality**: 4 distinct modality combinations, encompassing all risk categories. USB-SafeBench includes: "Risky-Image/Risky-Text (RIRT)", "Risky-Image/Safe-Text (RIST)", "Safe-Image/Risky-Text (SIRT)", and "Safe-Image/Safe-Text (SIST)".
- **Category**: A hierarchical structure of 3 primary categories(National Safety、 Public Safety、Ethical Safety ), branching into 16 secondary categories and further expanding into 61 tertiary categories.
- **Evaluation Domains**: Detailed assessment across vulnerability and over-refusal dimensions.
- **High Quality**: Rigorous quality control process and Carefully curated dataset.

This refined architecture ensures a robust framework for assessing safety in MLLMs, enhancing both clarity and expressiveness of evaluation metrics.
<p align="center">
  <img src="image/category_en.png" width="700px"/>
</p>


# 🏆 LeaderBoard

Here, we present the ASR rankings of various models:
<p align="center">
  <img src="image/learderboard_v1.png" width="800px"/>
</p>
For those interested in a more comprehensive overview of the leaderboard, please click the "Leaderboard" button located below the heading.


# 🔧 Data Construction Pipline
<p align="center">
  <img src="image/overveiwv3_final.png" width="800px"/>
</p>


# ✨ Safety Test Dataset Examples
<p align="center">
  <img src="image/demo_case.png" width="800px"/>
</p>

# ✨ Over Refusal Dataset Examples
<p align="center">
  <img src="image/refusal_vs_helpful.png" width="800px"/>
</p>

# 💡 Dataset Usage 
## 🪜 Download
You can download this dataset by visit [USB-SafeBench](https://huggingface.co/datasets/cgjacklin/USB/tree/main) or use the following command (make sure that you have installed [Huggingface Datasets](https://huggingface.co/docs/datasets/quickstart)):
```python
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
dataset = load_dataset("cgjacklin/USB")
```

# 📐 Evaluation
Utilize the GPT-4o model to conduct ASR and ARR evaluation using the prompts found within the scripts below:
```shell
python3 scripts/vlsbench.py   # ASR evaluation
python3 scripts/oversensitive.py # ARR evaluation
```

# 🔒 License
Usage and License Notices: This dataset is designated and licensed solely for research purposes. It is also subject to restrictions that adhere to the licensing agreements of GPT-4 and Stable Diffusion. The dataset is governed by Apache License 2.0.

