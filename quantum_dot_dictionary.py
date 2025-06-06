quantum_dots = {
    "CdSe_ZnS": [
        {
            "biomarker": "HER2",
            "emission_nm": 480,
            "color": "blue",
            "channel": "visible",
            "surface_options": ["biotin-PEG", "amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for HER2 detection"
        },
        {
            "biomarker": "Estrogen Receptor (ER)",
            "emission_nm": 530,
            "color": "green",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for ER (surface variant)"
        }
    ],
    "CdTeSe_ZnS": [
        {
            "biomarker": "HER2",
            "emission_nm": 800,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for HER2, deep tissue imaging"
        },
        {
            "biomarker": "Low pH",
            "emission_nm": 780,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": True,
            "notes": "NIR QD for acidic pH, pH-sensitive"
        }
    ],
    "CdSe_ZnS_Luciferase": [
        {
            "biomarker": "HER2",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for HER2"
        }
    ],
    "Carbon_Dot": [
        {
            "biomarker": "Low pH",
            "emission_nm": 610,
            "color": "orange-red",
            "channel": "visible",
            "surface_options": ["carboxyl", "hydroxyl"],
            "compatible_tags": ["antibody", "peptide"],
            "pH_sensitive": True,
            "notes": "Visible QD for acidic pH, pH-sensitive"
        }
    ]
} 