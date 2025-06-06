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
        },
        {
            "biomarker": "CD44",
            "emission_nm": 520,
            "color": "green",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for CD44"
        },
        {
            "biomarker": "CD24",
            "emission_nm": 540,
            "color": "yellow-green",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for CD24"
        },
        {
            "biomarker": "CD133",
            "emission_nm": 560,
            "color": "yellow",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for CD133"
        },
        {
            "biomarker": "EpCAM",
            "emission_nm": 580,
            "color": "orange",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for EpCAM"
        },
        {
            "biomarker": "MUC1",
            "emission_nm": 600,
            "color": "red-orange",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for MUC1"
        },
        {
            "biomarker": "E-cadherin",
            "emission_nm": 620,
            "color": "red",
            "channel": "visible",
            "surface_options": ["amine-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "Visible QD for E-cadherin"
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
        },
        {
            "biomarker": "Estrogen Receptor (ER)",
            "emission_nm": 850,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for ER (surface variant)"
        },
        {
            "biomarker": "CD44",
            "emission_nm": 820,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for CD44"
        },
        {
            "biomarker": "CD24",
            "emission_nm": 830,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for CD24"
        },
        {
            "biomarker": "CD133",
            "emission_nm": 840,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for CD133"
        },
        {
            "biomarker": "EpCAM",
            "emission_nm": 850,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for EpCAM"
        },
        {
            "biomarker": "MUC1",
            "emission_nm": 860,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for MUC1"
        },
        {
            "biomarker": "E-cadherin",
            "emission_nm": 870,
            "color": "NIR",
            "channel": "nir",
            "surface_options": ["carboxyl-PEG"],
            "compatible_tags": ["antibody"],
            "pH_sensitive": False,
            "notes": "NIR QD for E-cadherin"
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
        },
        {
            "biomarker": "Low pH",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": True,
            "notes": "BRET pair for acidic pH, pH-sensitive"
        },
        {
            "biomarker": "Estrogen Receptor (ER)",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for ER (surface variant)"
        },
        {
            "biomarker": "CD44",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for CD44"
        },
        {
            "biomarker": "CD24",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for CD24"
        },
        {
            "biomarker": "CD133",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for CD133"
        },
        {
            "biomarker": "EpCAM",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for EpCAM"
        },
        {
            "biomarker": "MUC1",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for MUC1"
        },
        {
            "biomarker": "E-cadherin",
            "emission_nm": None,
            "color": "BRET",
            "channel": "bret",
            "surface_options": ["biotin-PEG"],
            "compatible_tags": ["antibody", "luciferase"],
            "pH_sensitive": False,
            "notes": "BRET pair for E-cadherin"
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

for comp, qd_list in quantum_dots.items():
    for props in qd_list:
        print(f"{comp} - {props['biomarker']}: {props['color']} ({props['emission_nm']} nm), tags: {props['compatible_tags']}")
