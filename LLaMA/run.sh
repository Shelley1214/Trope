CUDA_VISIBLE_DEVICES=2 torchrun --nproc_per_node 1 example_chat_completion.py \
    --ckpt_dir llama-2-7b-chat/ \
    --tokenizer_path tokenizer.model \
    --temperature 0 \
    --max_batch_size 3 \
    --max_seq_len 2048
