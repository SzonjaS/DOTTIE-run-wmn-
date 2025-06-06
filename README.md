# DOTTIE Quantum Dot Library

A Python library for managing and querying quantum dot specifications for various biomarkers, with Mistral-7B integration for natural language interactions.

## Features

- Query quantum dots by biomarker and channel type (visible, NIR, BRET)
- Get detailed specifications including emission wavelengths, surface modifications, and compatibility
- Support for multiple quantum dot compositions (CdSe_ZnS, CdTeSe_ZnS, etc.)
- Logic gate functionality for complex biomarker detection
- Natural language interaction using Mistral-7B

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Files

- `functions.py` - Core functionality for querying QD data
- `qd_data.py` - Quantum dots specifications and properties
- `gate_types.py` - Logic gate implementations
- `test_functions.py` - Test suite for the library
- `model_utils.py` - Mistral-7B integration utilities

## Usage

### Basic QD Operations
```python
from functions import get_available_biomarkers, get_available_channels, get_qd_for_biomarker

# Get all available biomarkers
biomarkers = get_available_biomarkers()

# Get available channels for a specific biomarker
channels = get_available_channels("HER2")  # Returns ["visible", "nir", "bret"]

# Get QD specifications for a specific biomarker and channel
qd_specs = get_qd_for_biomarker("HER2", channel="visible")
```

### Using Mistral-7B
```python
from model_utils import load_mistral_model, generate_response

# Load the model (this may take a few minutes)
model, tokenizer = load_mistral_model()

# Ask questions about quantum dots
prompt = "What quantum dots are available for HER2 detection?"
response = generate_response(model, tokenizer, prompt)
print(response)
```

## System Requirements

- Python 3.8 or higher
- CUDA-capable GPU with at least 8GB VRAM (for Mistral-7B)
- 16GB+ RAM recommended

## Testing

Run the test suite:
```bash
python test_functions.py
```
