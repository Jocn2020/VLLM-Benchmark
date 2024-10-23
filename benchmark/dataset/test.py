from datasets import load_dataset, concatenate_datasets
from typing import Any, AsyncGenerator, Collection, Dict, List, Optional, Tuple

# Load the GSM8K dataset
dataset = load_dataset("gsm8k", 'main')

# Print the dataset structure
print(dataset)
from pdb import set_trace as bp
# concatenate train and test
gsm8k_train = dataset['train'].map(lambda x: {'question': x['question'], 'answer': x['answer']})
gsm8k_test = dataset['test'].map(lambda x: {'question': x['question'], 'answer': x['answer']})
combined_dataset = concatenate_datasets([gsm8k_train, gsm8k_test])

sampled_requests: List[Tuple[str, int, int]] = []

for data in combined_dataset:
    # Tokenize the prompts and answer.
    prompt = data["question"]
    prompt_token_ids = tokenizer(prompt).input_ids
    answer = data["answer"]
    answer_token_ids = tokenizer(completion).input_ids
    prompt_len = len(prompt_token_ids)
    output_len = len(answer_token_ids
                        ) if fixed_output_len is None else fixed_output_len
    if fixed_output_len is None and (prompt_len < 4 or output_len < 4):
        # Prune too short sequences.
        continue
    if fixed_output_len is None and \
        (prompt_len > 1024 or prompt_len + output_len > 2048):
        # Prune too long sequences.
        continue

    else:
        mm_content = None

sampled_requests.append((prompt, prompt_len, output_len))
bp()