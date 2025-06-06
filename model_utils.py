from functions import get_qd_for_biomarker

def recommend_qds(biomarkers, biomarker_channels, require_ph_sensitive=False, preferred_colors=None):
    """
    Function to recommend quantum dots based on biomarker selection and preferences.
    
    Args:
        biomarkers (list): List of selected biomarkers
        biomarker_channels (dict): Dictionary mapping biomarkers to their selected channels
        require_ph_sensitive (bool): Whether to require pH-sensitive QDs
        preferred_colors (list): Optional list of preferred QD colors
    
    Returns:
        list: List of recommended QD specifications
    """
    recommendations = []
    
    for biomarker in biomarkers:
        # Get the selected channel for this biomarker, default to 'visible' if not specified
        channel = biomarker_channels.get(biomarker, 'visible')
        
        # Get QD specifications for this biomarker and channel
        qd_specs = get_qd_for_biomarker(biomarker, channel)
        
        if qd_specs:
            # Apply filters based on preferences
            if require_ph_sensitive and not qd_specs['pH_sensitive']:
                continue
                
            if preferred_colors and qd_specs['color'] not in preferred_colors:
                continue
            
            # Add to recommendations
            recommendations.append({
                'biomarker': biomarker,
                'composition': qd_specs['composition'],
                'color': qd_specs['color'],
                'emission_nm': qd_specs['emission_nm'],
                'surface': qd_specs['surface'],
                'notes': qd_specs['notes']
            })
    
    return recommendations

# Example usage
if __name__ == "__main__":
    # Example biomarkers and channels
    biomarkers = ["HER2", "ER"]
    biomarker_channels = {"HER2": "visible", "ER": "visible"}
    
    # Example preferences
    require_ph_sensitive = True
    preferred_colors = ["red"]
    
    # Generate recommendations
    recommendations = recommend_qds(biomarkers, biomarker_channels, require_ph_sensitive, preferred_colors)
    
    # Print recommendations
    for recommendation in recommendations:
        print(f"Biomarker: {recommendation['biomarker']}")
        print(f"Composition: {recommendation['composition']}")
        print(f"Color: {recommendation['color']}")
        print(f"Emission nm: {recommendation['emission_nm']}")
        print(f"Surface: {recommendation['surface']}")
        print(f"Notes: {recommendation['notes']}")
        print("\n") 
