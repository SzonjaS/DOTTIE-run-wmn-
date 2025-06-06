# DOTTIE-run-wmn-
# DOTTIE Quantum Dot Library

A Python library for managing and querying quantum dot specifications for various biomarkers.

## Features

- Query quantum dots by biomarker and channel type (visible, NIR, BRET)
- Get detailed specifications including emission wavelengths, surface modifications, and compatibility
- Support for multiple quantum dot compositions (CdSe_ZnS, CdTeSe_ZnS, etc.)
- Logic gate functionality for complex biomarker detection

## Files

- `functions.py` - Core functionality for querying QD data
- `qd_data.py` - Quantum dots specifications and properties
- `gate_types.py` - Logic gate implementations
- `test_functions.py` - Test suite for the library

## Usage

```python
from functions import get_available_biomarkers, get_available_channels, get_qd_for_biomarker

# Get all available biomarkers
biomarkers = get_available_biomarkers()

# Get available channels for a specific biomarker
channels = get_available_channels("HER2")  # Returns ["visible", "nir", "bret"]

# Get QD specifications for a specific biomarker and channel
qd_specs = get_qd_for_biomarker("HER2", channel="visible")
```

## Testing

Run the test suite:
```bash
python test_functions.py
```