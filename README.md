# LLMind 2.0

## Introduction

<!-- - This is the repository for paper []().  -->

This repository includes the Llama-2-7B finetuning related files, including
- [finetuned lora weights of our method](finetune_results/epoch_1)
- [dataset for finetuning](#dataset)
- [training scripts](#training-scripts)

For finetuning, please refer to the [llama-recipes README](llama-recipes/README.md) for more details.

### Environment Setup
```
git clone https://github.com/1155157110/LLMind2.0.git
cd LLMind2.0/llama-recipes
pip install -U pip setuptools
pip install -e .
```

Llama-2-7b model weights and converted hugging face format weights needs to be put to the [7B](llama-2-7b/7B) folder before loading models.

### Dataset
<!-- ![](figures/datasets.png) -->
Datasets are stored in [datasets folder](datasets)

### Training Scripts
The training scripts is [train_eval.sh](llama-recipes/train_eval.sh).

Example usage:
```
cd llama-recipes
sh train_eval.sh
```

## Reference
<!-- To cite this paper, please add the following citation to your paper: -->

## Questions
For enquiries about the paper or the code, please feel free to open an issue.