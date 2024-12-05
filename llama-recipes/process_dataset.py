# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

import copy
import datasets

def get_preprocessed_custom(dataset_config, tokenizer, split):
    dataset = datasets.load_dataset("json", data_files="../datasets/dataset_48k.jsonl", split='train')
    dataset = dataset.shuffle(seed=42)

    if split == 'train':
        dataset = dataset.filter(lambda x, idx: idx < int(dataset.num_rows*0.9), with_indices=True)
    elif split == 'test':
        dataset = dataset.filter(lambda x, idx: int(dataset.num_rows*0.9) <= idx < int(dataset.num_rows*0.95), with_indices=True)
    elif split == 'validation':
        dataset = dataset.filter(lambda x, idx: int(dataset.num_rows*0.95) < idx, with_indices=True)
    else:
        raise NotImplementedError

    def tokenize_add_label(sample):
        prompt = tokenizer.encode(tokenizer.bos_token + sample["prompt"], add_special_tokens=False)
        response = tokenizer.encode(sample["response"] +  tokenizer.eos_token, add_special_tokens=False)

        sample = {
            "input_ids": prompt + response,
            "attention_mask" : [1] * (len(prompt) + len(response)),
            "labels": [-100] * len(prompt) + response
        }

        return sample

    dataset = dataset.map(tokenize_add_label, remove_columns=list(dataset.features))

    return dataset