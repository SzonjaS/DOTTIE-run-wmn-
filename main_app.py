import streamlit as st
from gate_types import AND, OR, NOT, NAND
from functions import get_available_biomarkers, get_available_channels, get_qd_for_biomarker
from model_utils import recommend_qds

st.set_page_config(page_title="NanoLogix Quantum Dot Logic Demo", page_icon="🧬", layout="centered")

st.title("🧬 NanoLogix: Quantum Dot Logic for Breast Cancer")
st.markdown("""
Welcome to NanoLogix!  
Design, simulate, and visualize quantum dot logic circuits for breast cancer detection.  
Select your biomarkers, logic gate, and see which quantum dots light up!  
""")

# Get available biomarkers
biomarker_options = get_available_biomarkers()

# Select biomarkers
st.header("🔬 Select Biomarkers")
selected_biomarkers = st.multiselect("Choose biomarkers to detect:", biomarker_options, default=["HER2", "Low pH"])

# Select channel for each biomarker
st.header("📡 Select Detection Channel")
biomarker_channels = {}
for biomarker in selected_biomarkers:
    available_channels = get_available_channels(biomarker)
    if available_channels:
        selected_channel = st.selectbox(
            f"Channel for {biomarker}:",
            available_channels,
            key=f"channel_{biomarker}"
        )
        biomarker_channels[biomarker] = selected_channel

# Select logic gate
st.header("🔗 Select Logic Gate")
logic_gate_name = st.selectbox("Choose logic gate:", ["AND", "OR", "NOT", "NAND"])
gate_func_map = {
    "AND": AND, "OR": OR, "NOT": NOT, "NAND": NAND
}
logic_gate_func = gate_func_map[logic_gate_name]

# Input signals
st.header("🧪 Biomarker Detection")
input_signals = []
for biomarker in selected_biomarkers:
    detected = st.checkbox(f"Is {biomarker} detected?", value=True)
    input_signals.append(int(detected))

# Compute logic output
if logic_gate_name == "NOT":
    # NOT gate only works on first input
    output = logic_gate_func(input_signals[0]) if input_signals else None
else:
    output = logic_gate_func(input_signals) if input_signals else None

st.markdown(f"### 🎛️ Logic Gate Output: :orange[{output}]")

# QD Recommendations
st.header("✨ Recommended Quantum Dots")
require_ph_sensitive = st.checkbox("Require pH-sensitive QDs?", value=False)
preferred_colors = st.multiselect(
    "Preferred QD colors (optional):",
    ["blue", "green", "yellow-green", "yellow", "orange", "red-orange", "red", "NIR", "BRET"]
)

# Get AI recommendations
recommendations = recommend_qds(
    selected_biomarkers,
    biomarker_channels,
    require_ph_sensitive,
    preferred_colors if preferred_colors else None
)

for rec in recommendations:
    st.markdown(
        f"**🔹 {rec['biomarker']}**: "
        f"{rec['composition']} QD, "
        f":rainbow[{rec['color']}] "
        f"({rec['emission_nm']} nm)  \n"
        f"Surface: {', '.join(rec['surface']) if rec['surface'] else 'N/A'}  \n"
        f"Notes: {rec['notes']}"
    )

# Cute footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-size: 1.2em;'>"
    "✨🧬🦋 Made with <span style='color:pink;'>love</span> for breast cancer research! 🦋🧬✨"
    "</div>", unsafe_allow_html=True
)
