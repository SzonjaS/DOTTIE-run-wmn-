from qd_data import quantum_dots

def get_available_biomarkers():
    """Returns a list of all available biomarkers across all QD types."""
    biomarkers = set()
    for qd_list in quantum_dots.values():
        for qd in qd_list:
            biomarkers.add(qd["biomarker"])
    return sorted(list(biomarkers))

def get_available_channels(biomarker):
    """Returns available channels for a specific biomarker."""
    channels = set()
    for qd_list in quantum_dots.values():
        for qd in qd_list:
            if qd["biomarker"] == biomarker:
                channels.add(qd["channel"])
    return sorted(list(channels))

def get_qd_for_biomarker(biomarker, channel="visible"):
    """
    Get quantum dot specifications for a given biomarker and channel.
    Args:
        biomarker: The biomarker to target
        channel: The desired channel (visible, nir, or bret)
    Returns:
        Dictionary with QD specifications or None if not found
    """
    for composition, qd_list in quantum_dots.items():
        for qd in qd_list:
            if qd["biomarker"] == biomarker and qd["channel"] == channel:
                return {
                    "composition": composition,
                    "emission_nm": qd["emission_nm"],
                    "surface": qd["surface_options"],
                    "color": qd["color"],
                    "compatible_tags": qd["compatible_tags"],
                    "pH_sensitive": qd["pH_sensitive"],
                    "notes": qd["notes"]
                }
    return None

def generate_gate_design(gate_type, biomarkers, input_states=None, channel_override=None):
    # This function will be implemented later when we work on the logic gate library
    pass

