# Unveiling Narrative Reasoning Limits of Large Language Models with Trope in Movie Synopses

Source code for the EMNLP 2024 Findings paper entitled "Unveiling Narrative Reasoning Limits of Large Language Models with Tropes in Movie Synopses"

Hung-Ting Su*, Ya-Ching Hsu*, Xudong Lin, Xiang-Qian Shi, Yulei Niu, Han-Yuan Hsu, Hung-yi Lee, Winston H. Hsu
(*: Equal contribution)

## Data Preparation
* unzip file `synopses.zip` in data folder
* execute `plot_segment.py` to separate synopses into individual sentences.


## How to RUN
### multi-label classification
* gpt_multi
    ```
    python gpt.py --task multi --openai_key "your_api_key"
    ```

### binary classification

* llama zero shot:
    ```
    llama/example_chat_completion.py \
    --ckpt_dir llama-2-7b-chat/ \
    --tokenizer_path tokenizer.model \
    --temperature 0 \
    --max_batch_size 3 \
    --max_seq_len 2048
    ```

* gpt chain of thought 
    ```
    python gpt.py --task binary_cot --openai_key "your_api_key"
    ```

* gpt base
    ```
    python gpt.py --task binary_base --openai_key "your_api_key"
    ```

### attack
* attack base:
    Execute the attack method in `attack/attack_base.py` and review `attack/analysis_base.py` to observe its success. 
* attack chain of thought:
    Execute the attack method in `attack/attack_cot.py` and review `attack/analysis_cot.py` to observe its success.


## Citation
```bibtex
@inproceedings{SuHsu2024unveiling,
  title={Unveiling Narrative Reasoning Limits of Large Language Models with Tropes in Movie Synopses},
  author={Hung-Ting Su and Ya-Ching Hsu and Xudong Lin and Xiang-Qian Shi and Yulei Niu and Han-Yuan Hsu and Hung-yi Lee and Winston H. Hsu},
  booktitle={Findings of EMNLP 2024},
  year={2024}
}
```

