import streamlit as st
from typing import Dict, Tuple, Optional, List

# Data structure containing all prop information with improved organization
props_data: Dict[str, List[Tuple[float, float, Optional[float]]]] = {
    # ===== PUSH-PULL PROPS =====
    "Push-Pull Prop RS 210 (1.30-2.10 m)": [(1.30, 25.0, 25.0), (2.00, 25.0, 25.0), (2.10, 23.6, 25.0)],
    "Push-Pull Prop RS 260 (2.30-2.60 m)": [(2.30, 25.0, 25.0), (2.60, 22.1, 25.0)],
    "Push-Pull Prop RS 300 (1.90-3.00 m)": [(1.90, 25.0, 25.0), (2.30, 25.0, 25.0), (2.50, 21.6, 25.0), (3.00, 14.2, 25.0)],
    "Push-Pull Prop RS 450 (2.80-4.50 m)": [(2.80, 25.0, 25.0), (3.60, 25.0, 25.0), (4.00, 17.2, 25.0), (4.50, 11.8, 25.0)],
    "Push-Pull Prop RS 650 (4.30-6.50 m)": [(4.30, 25.0, 25.0), (4.90, 25.0, 25.0), (5.00, 24.4, 25.0), (5.50, 18.5, 25.0), (6.00, 15.9, 25.0), (6.50, 13.2, 25.0)],
    "Push-Pull Prop RS 1000 (6.40-10.00 m)": [(6.40, 34.2, 29.0), (6.64, 34.2, 29.0), (7.64, 25.9, 29.0), (8.44, 20.3, 29.0), (9.24, 16.0, 29.0), (10.00, 12.8, 29.0)],
    "Push-Pull Prop RS 1400 (6.40-14.00 m)": [(6.40, 28.8, 27.7), (10.46, 28.8, 27.7), (12.00, 26.8, 27.7), (13.00, 22.2, 27.7), (14.00, 18.1, 27.7)],
    "Push-Pull Prop RS I (1.84-2.94 m)": [(1.84, 16.3, 12.7), (2.45, 16.3, 12.7), (2.75, 14.6, 12.7), (2.94, 12.5, 12.7)],
    "Push-Pull Prop RS II (2.56-4.06 m)": [(2.56, 16.3, 12.7), (2.97, 16.3, 12.7), (3.37, 11.7, 12.7), (3.77, 8.5, 12.7), (4.06, 7.0, 12.7)],
    "Push-Pull Prop RSS I (2.05-2.94 m)": [(2.05, 34.2, 26.3), (2.30, 33.2, 26.3), (2.60, 22.7, 26.3), (2.94, 14.2, 26.3)],
    "Push-Pull Prop RSS II (2.91-3.80 m)": [(2.91, 31.7, 26.3), (3.21, 26.4, 26.3), (3.50, 17.1, 26.3), (3.80, 11.6, 26.3)],
    "Push-Pull Prop RSS III (4.60-6.00 m)": [(4.60, 27.8, 20.0), (4.95, 22.8, 20.0), (5.30, 18.6, 20.0), (5.65, 14.7, 20.0), (6.00, 11.1, 20.0)],

    # ===== KICKERS =====
    "Kicker AV 82 (0.50-0.82 m)": [(0.50, 34.1, 26.3), (0.66, 28.9, 26.3), (0.82, 23.2, 26.3)],
    "Kicker AV 111 (0.79-1.11 m)": [(0.79, 30.9, 26.3), (0.95, 24.9, 26.3), (1.11, 19.7, 26.3)],
    "Kicker AV 140 (1.08-1.40 m)": [(1.08, 25.7, 26.3), (1.24, 20.0, 26.3), (1.40, 15.7, 26.3)],
    "Kicker AV 190 (1.08-1.90 m)": [(1.08, 39.2, 21.1), (1.25, 38.5, 21.1), (1.50, 37.4, 21.1), (1.75, 34.6, 21.1), (1.90, 31.3, 21.1)],
    "Kicker AV 210 (1.28-2.10 m)": [(1.28, 34.2, 26.3), (1.69, 34.2, 26.3), (1.90, 25.5, 26.3), (2.10, 19.0, 26.3)],
    "Kicker AV RSS III (2.03-2.92 m)": [(2.03, 34.2, 26.3), (2.30, 33.2, 26.3), (2.60, 22.7, 26.3), (2.94, 14.2, 26.3)],


    # ===== COMPRESSION SPINDLES =====
    "Compression Brace SKS 2 (1.35-1.93 m)": [(1.35, 196.2, 63.8), (1.50, 191.2, 63.8), (1.65, 186.1, 63.8), (1.80, 175.6, 63.8), (1.93, 149.4, 63.8)],
    "Compression Brace SKS 3 (1.75-2.33 m)": [(1.75, 189.5, 63.8), (1.90, 185.2, 63.8), (2.05, 178.4, 63.8), (2.20, 166.4, 63.8), (2.33, 141.6, 63.8)],
    "Compression Brace SKS 4 (2.55-3.13 m)": [(2.55, 171.4, 63.8), (2.70, 164.4, 63.8), (2.85, 154.7, 63.8), (3.00, 143.0, 63.8), (3.13, 123.3, 63.8)],
    "Adjustable Brace CB 164-224 (1.64-2.24 m)": [(1.64, 137.1, 102.0), (1.79, 121.4, 102.0), (1.94, 105.6, 102.0), (2.09, 101.9, 102.0), (2.24, 97.0, 102.0)],
    "Strut VARIOKIT (2.75-4.50 m)": [(2.75, 160.0, 160.0), (4.50, 160.0, 160.0)],
    "Strut VARIOKIT (4.00-7.00 m)": [(4.00, 160.0, 160.0), (7.00, 160.0, 160.0)],
    "Strut VARIOKIT (6.00-9.00 m)": [(6.00, 160.0, 159.7), (7.00, 160.0, 159.7), (8.00, 146.5, 159.7), (9.00, 122.9, 159.7)],
    


    # ===== HEAVY-DUTY SPINDLES =====
     "SLS 40/80 (0.40-0.80 m)": [(0.40, 88.0, 70.8), (0.80, 88.0, 70.8)],
    "SLS 80/140 (0.80-1.40 m)": [(0.80, 107.1, 81.6), (1.40, 107.1, 81.6)],
    "SLS 100/180 (1.00-1.80 m)": [(1.00, 107.1, 81.6), (1.50, 107.1, 81.6), (1.60, 105.5, 81.6), (1.80, 90.4, 81.6)],
    "SLS 140/240 (1.40-2.40 m)": [(1.40, 138.4, 105.4), (1.50, 134.7, 105.4), (1.70, 122.6, 105.4), (1.90, 109.6, 105.4), 
                                 (2.00, 102.5, 105.4), (2.10, 95.2, 105.4), (2.20, 87.8, 105.4), (2.30, 80.5, 105.4), (2.40, 73.4, 105.4)],
    "SLS 200/300 (2.00-3.00 m)": [(2.00, 136.6, 105.4), (2.20, 123.6, 105.4), (2.40, 109.3, 105.4), (2.50, 101.9, 105.4),
                                 (2.60, 94.4, 105.4), (2.70, 87.2, 105.4), (2.80, 79.8, 105.4), (2.90, 72.9, 105.4), (3.00, 66.4, 105.4)],
    "SLS 260/360 (2.60-3.60 m)": [(2.60, 133.4, 105.4), (2.80, 116.2, 105.4), (3.00, 99.9, 105.4), (3.10, 91.9, 105.4),
                                 (3.20, 84.3, 105.4), (3.30, 77.3, 105.4), (3.40, 70.6, 105.4), (3.50, 64.6, 105.4), (3.60, 59.0, 105.4)],
    "SLS 320/420 (3.20-4.20 m)": [(3.20, 117.1, 105.4), (3.40, 101.2, 105.4), (3.50, 92.8, 105.4), (3.60, 85.5, 105.4),
                                 (3.70, 78.6, 105.4), (3.80, 72.1, 105.4), (3.90, 66.1, 105.4), (4.00, 60.2, 105.4), (4.10, 55.8, 105.4), (4.20, 51.2, 105.4)],
    "SLS 380/480 (3.80-4.80 m)": [(3.80, 85.5, 105.4), (3.90, 80.6, 105.4), (4.00, 76.1, 105.4), (4.10, 71.8, 105.4),
                                 (4.20, 67.6, 105.4), (4.30, 63.7, 105.4), (4.40, 59.9, 105.4), (4.50, 55.4, 105.4), (4.60, 51.3, 105.4), (4.70, 47.5, 105.4), (4.80, 43.9, 105.4)],
    
    # SLS with Adapter
    "SLS 40/80 + Adapter (0.48-0.80 m)": [(0.48, 88.0, 70.8), (0.80, 88.0, 70.8)],
    "SLS 80/140 + Adapter (0.99-1.50 m)": [(0.99, 107.1, 81.6), (1.20, 107.1, 81.6), (1.40, 94.9, 81.6), (1.50, 87.0, 81.6)],
    "SLS 100/180 + Adapter (1.19-1.91 m)": [(1.19, 107.1, 81.6), (1.30, 107.1, 81.6), (1.50, 99.9, 81.6), (1.80, 78.4, 81.6), (1.91, 69.5, 81.6)],
    "SLS 140/240 + Adapter (1.59-2.51 m)": [(1.59, 117.2, 105.4), (1.70, 110.4, 105.4), (1.90, 97.2, 105.4), (2.10, 83.7, 105.4),
                                           (2.30, 70.1, 105.4), (2.51, 58.1, 105.4)],
    "SLS 200/300 + Adapter (2.19-3.11 m)": [(2.19, 111.6, 105.4), (2.30, 103.9, 105.4), (2.50, 89.9, 105.4), (2.70, 76.2, 105.4),
                                           (2.90, 63.9, 105.4), (3.11, 52.9, 105.4)],
    "SLS 260/360 + Adapter (2.79-3.71 m)": [(2.79, 104.0, 105.4), (2.90, 95.2, 105.4), (3.10, 80.8, 105.4), (3.30, 67.6, 105.4),
                                           (3.50, 57.0, 105.4), (3.71, 47.5, 105.4)],
    "SLS 320/420 + Adapter (3.39-4.31 m)": [(3.39, 91.0, 105.4), (3.50, 82.5, 105.4), (3.70, 69.9, 105.4), (3.90, 59.1, 105.4),
                                           (4.10, 50.0, 105.4), (4.31, 41.8, 105.4)],
    "SLS 380/480 + Adapter (3.99-4.91 m)": [(3.99, 71.0, 105.4), (4.10, 66.4, 105.4), (4.30, 58.6, 105.4), (4.50, 50.3, 105.4),
                                           (4.70, 43.2, 105.4), (4.91, 36.4, 105.4)],
    
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
