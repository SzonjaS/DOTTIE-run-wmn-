from functions import get_available_biomarkers, get_available_channels, get_qd_for_biomarker

if __name__ == "__main__":
    # Test getting all biomarkers
    biomarkers = get_available_biomarkers()
    print("Available biomarkers:", biomarkers)
    assert "HER2" in biomarkers
    assert "Low pH" in biomarkers
    
    # Test getting channels for HER2
    her2_channels = get_available_channels("HER2")
    print("\nHER2 available channels:", her2_channels)
    assert "visible" in her2_channels
    assert "nir" in her2_channels
    assert "bret" in her2_channels
    
    # Test getting QD specifications
    her2_visible = get_qd_for_biomarker("HER2", channel="visible")
    print("\nHER2 visible QD specs:", her2_visible)
    assert her2_visible is not None
    assert her2_visible["emission_nm"] == 480
    assert her2_visible["color"] == "blue"
    assert "antibody" in her2_visible["compatible_tags"]
    
    print("\nAll tests passed successfully!") 