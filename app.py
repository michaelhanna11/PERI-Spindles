import streamlit as st
from typing import Dict, Tuple, Optional, List

# Data structure containing all prop information with improved organization
props_data: Dict[str, List[Tuple[float, float, Optional[float]]]] = {
    # ===== PUSH-PULL PROPS =====
    "Push-Pull Prop RS 210 (1.30-2.10 m)": [
        (1.30, 25.0, 25.0), (2.00, 25.0, 25.0), (2.10, 23.6, 25.0)],
    
    "Push-Pull Prop RS 260 (2.30-2.60 m)": [
        (2.30, 25.0, 25.0), (2.60, 22.1, 25.0)],
    
    "Push-Pull Prop RS 300 (1.90-3.00 m)": [
        (1.90, 25.0, 25.0), (2.30, 25.0, 25.0), 
        (2.50, 21.6, 25.0), (3.00, 14.2, 25.0)],
    
    # ... (other push-pull props remain the same)

    # ===== KICKERS =====
    "Kicker AV 82 (0.50-0.82 m)": [
        (0.50, 34.1, 26.3), (0.66, 28.9, 26.3), (0.82, 23.2, 26.3)],
    
    # ... (other kickers remain the same)

    # ===== COMPRESSION SPINDLES =====
    "Compression Brace SKS 2 (1.35-1.93 m)": [
        (1.35, 196.2, 63.8), (1.50, 191.2, 63.8), 
        (1.65, 186.1, 63.8), (1.80, 175.6, 63.8), 
        (1.93, 149.4, 63.8)],
    
    # ... (other compression spindles remain the same)

    # ===== HEAVY-DUTY SPINDLES =====
    "SLS 40/80 (0.40-0.80 m)": [
        (0.40, 88.0, 70.8), (0.80, 88.0, 70.8)],
    
    # ... (other SLS spindles remain the same)

    # ===== SCS SPINDLES =====
    "SCS 198/250 (1.98-2.50 m)": [
        (1.98, 264, 211), (2.10, 247, 211), 
        (2.20, 233, 211), (2.30, 217, 211), 
        (2.40, 197, 211), (2.50, 175, 211)]
}

def interpolate_value(x: float, x0: float, y0: float, x1: float, y1: float) -> Optional[float]:
    """Linear interpolation between two points with null checks."""
    if None in (y0, y1) or x0 == x1:
        return None
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def get_capacities(prop_type: str, length: float) -> Tuple[Optional[float], Optional[float]]:
    """Calculate compression and tension capacities with improved interpolation."""
    data = props_data.get(prop_type, [])
    if not data:
        return None, None
    
    min_len, max_len = data[0][0], data[-1][0]
    
    # Boundary checks
    if length < min_len or length > max_len:
        return None, None
    
    # Check for exact match
    for len_val, comp, tension in data:
        if length == len_val:
            return comp, tension
    
    # Find interpolation interval
    for i in range(len(data)-1):
        lower_len, lower_comp, lower_tension = data[i]
        upper_len, upper_comp, upper_tension = data[i+1]
        
        if lower_len <= length <= upper_len:
            # Interpolate both compression and tension
            comp = interpolate_value(length, lower_len, lower_comp, upper_len, upper_comp)
            tension = interpolate_value(length, lower_len, lower_tension, upper_len, upper_tension)
            return comp, tension
    
    return None, None

# ===== STREAMLIT UI =====
st.set_page_config(
    page_title="PERI Prop Capacity Calculator",
    page_icon="🏗️",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .header {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #2c3e50 !important;
    }
    .result {
        font-size: 20px !important;
        padding: 10px !important;
        border-radius: 5px !important;
    }
    .compression {
        background-color: #e6f7ff !important;
    }
    .tension {
        background-color: #fff7e6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="header">PERI Push-Pull Prop Capacity Calculator</p>', unsafe_allow_html=True)
st.markdown("---")

# Prop selection with category grouping
prop_category = st.selectbox(
    "Select Prop Category",
    ["Push-Pull Props", "Kickers", "Compression Spindles", "Heavy-Duty Spindles", "SCS Spindles"]
)

# Filter props based on category
filtered_props = {
    "Push-Pull Props": [p for p in props_data.keys() if p.startswith("Push-Pull")],
    "Kickers": [p for p in props_data.keys() if p.startswith("Kicker")],
    "Compression Spindles": [p for p in props_data.keys() if "SKS" in p or "CB" in p or "VARIOKIT" in p],
    "Heavy-Duty Spindles": [p for p in props_data.keys() if "SLS" in p],
    "SCS Spindles": [p for p in props_data.keys() if "SCS" in p]
}

prop_type = st.selectbox(
    "Select Prop Type",
    filtered_props[prop_category],
    help="Select the specific prop model from the dropdown"
)

# Get length range and input
min_length = props_data[prop_type][0][0]
max_length = props_data[prop_type][-1][0]

length = st.slider(
    "Extension Length (m)",
    min_value=min_length,
    max_value=max_length,
    value=min_length,
    step=0.01,
    help=f"Valid range: {min_length:.2f}m to {max_length:.2f}m"
)

# Calculation and results
if st.button("Calculate Capacities", type="primary"):
    comp, tension = get_capacities(prop_type, length)
    
    if comp is None:
        st.error("Invalid length input or calculation error")
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f'<div class="result compression">'
                f'<strong>Compression Capacity:</strong> {comp:.1f} kN'
                f'</div>',
                unsafe_allow_html=True
            )
        with col2:
            tension_display = f"{tension:.1f} kN" if tension is not None else "Not specified"
            st.markdown(
                f'<div class="result tension">'
                f'<strong>Tension Capacity:</strong> {tension_display}'
                f'</div>',
                unsafe_allow_html=True
            )
        
        # Show note about tension values if needed
        if tension is None:
            st.info("Note: Tension capacity is only specified at specific lengths for this prop type.")

# Footer
st.markdown("---")
st.caption("""
    **Note:** All capacities are based on PERI technical documentation. 
    For critical applications, always consult the original specifications.
""")
