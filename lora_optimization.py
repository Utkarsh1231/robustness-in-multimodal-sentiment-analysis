import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForSequenceClassification

def apply_lora_to_msa(model_name="bert-base-uncased"):
    """
    Applies Low-Rank Adaptation (LoRA) to a Multimodal Sentiment Analysis
    backbone to optimize parameter efficiency as described in my research.
    """
    # 1. Load the pre-trained benchmark model
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # 2. Configure LoRA parameters
    # We target the attention layers (query/value) which is standard for MSA robustness
    config = LoraConfig(
        r=8, 
        lora_alpha=16, 
        target_modules=["query", "value"], 
        lora_dropout=0.1, 
        bias="none", 
        task_type="SEQ_CLS"
    )

    # 3. Wrap the model with LoRA layers
    lora_model = get_peft_model(model, config)
    
    # 4. Freeze original weights to ensure only LoRA matrices train
    lora_model.print_trainable_parameters()
    
    return lora_model

if __name__ == "__main__":
    print("Initializing LoRA optimization for Multimodal Sentiment Analysis...")
    msa_model = apply_lora_to_msa()
