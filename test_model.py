from model_utils import load_mistral_model, generate_response
from functions import get_qd_for_biomarker, get_available_biomarkers, get_available_channels

def test_model_integration():
    """
    Test GPT-2 integration with quantum dot library.
    """
    print("Starting model integration test...")
    
    # Load model and tokenizer
    model, tokenizer = load_mistral_model()
    
    # Test 1: Basic QD query
    print("\nTest 1: Basic QD query")
    prompt = "What quantum dots are available for HER2 detection?"
    print(f"Prompt: {prompt}")
    response = generate_response(model, tokenizer, prompt)
    print(f"Response: {response}")
    
    # Test 2: Technical specifications query
    print("\nTest 2: Technical specifications query")
    her2_specs = get_qd_for_biomarker("HER2", channel="visible")
    prompt = f"Explain these quantum dot specifications in simple terms: {her2_specs}"
    print(f"Prompt: {prompt}")
    response = generate_response(model, tokenizer, prompt)
    print(f"Response: {response}")
    
    # Test 3: Comparison query
    print("\nTest 3: Comparison query")
    prompt = "Compare quantum dots available for HER2 detection in visible vs NIR channels."
    print(f"Prompt: {prompt}")
    response = generate_response(model, tokenizer, prompt)
    print(f"Response: {response}")

if __name__ == "__main__":
    test_model_integration() 