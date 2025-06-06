from transformers import AutoModelForCausalLM, AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer
import torch
import os

def load_mistral_model(token=None):
    """
    Load language model and tokenizer from HuggingFace.
    
    Args:
        token (str, optional): HuggingFace access token
        
    Returns:
        tuple: (model, tokenizer)
    """
    print("Loading local GPT-2 model...")
    
    try:
        # Try to load the model directly (offline mode)
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2', local_files_only=True)
        model = GPT2LMHeadModel.from_pretrained('gpt2', local_files_only=True)
    except Exception as e:
        print("Model not found locally, downloading from Hugging Face...")
        # If not available locally, download it
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        # Save the model locally for future use
        tokenizer.save_pretrained('gpt2')
        model.save_pretrained('gpt2')
    
    return model, tokenizer

def generate_response(model, tokenizer, prompt, max_length=100):
    """
    Generate a response using the model.
    
    Args:
        model: The language model
        tokenizer: The tokenizer
        prompt (str): The input prompt
        max_length (int): Maximum length of the response
        
    Returns:
        str: Generated response
    """
    try:
        # Add context about quantum dots to the prompt
        context = "In the context of quantum dots and biomarkers: "
        full_prompt = context + prompt
        
        # Encode the prompt
        inputs = tokenizer(full_prompt, return_tensors="pt", padding=True, truncation=True)
        
        # Generate response
        outputs = model.generate(
            inputs["input_ids"],
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )
        
        # Decode and return the response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Remove the context from the response
        response = response.replace(context, "").strip()
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Load model and tokenizer
    model, tokenizer = load_mistral_model()
    
    # Example prompt using your quantum dot data
    prompt = "What quantum dots are available for HER2 detection?"
    
    # Generate response
    response = generate_response(model, tokenizer, prompt)
    print(f"\nPrompt: {prompt}")
    print(f"Response: {response}") 