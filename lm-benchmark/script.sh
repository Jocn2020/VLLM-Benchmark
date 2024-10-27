lm_eval --model vllm \
    --model_args pretrained=facebook/opt-125m,tensor_parallel_size=1,dtype=auto,gpu_memory_utilization=0.8,data_parallel_size=1 \
    --tasks gsm8k-cot \
    --batch_size auto