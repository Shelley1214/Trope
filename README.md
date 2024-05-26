
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

