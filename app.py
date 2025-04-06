import streamlit as st
import pandas as pd
from typing import Dict, Tuple, Optional

# Data structure containing all prop information
props_data = {
    "Push-Pull Prop RS 210 (1.30-2.10 m)": [(1.30, 25.0, 25.0), (2.00, 25.0, 25.0), (2.10, 23.6, None)],
    "Push-Pull Prop RS 260 (2.30-2.60 m)": [(2.30, 25.0, 25.0), (2.60, 22.1, None)],
    "Push-Pull Prop RS 300 (1.90-3.00 m)": [(1.90, 25.0, 25.0), (2.30, 25.0, None), (2.50, 21.6, None), (3.00, 14.2, None)],
    "Push-Pull Prop RS 450 (2.80-4.50 m)": [(2.80, 25.0, 25.0), (3.60, 25.0, None), (4.00, 17.2, None), (4.50, 11.8, None)],
    "Push-Pull Prop RS 650 (4.30-6.50 m)": [(4.30, 25.0, 25.0), (4.90, 25.0, None), (5.00, 24.4, None), (5.50, 19.5, None), (6.00, 15.9, None), (6.50, 13.2, None)],
    "Push-Pull Prop RS 1000 (6.40-10.00 m)": [(6.40, 34.2, 29.0), (6.64, 34.2, None), (7.64, 25.9, None), (8.44, 20.3, None), (9.24, 16.0, None), (10.00, 12.8, None)],
    "Push-Pull Prop RS 1400 (6.40-14.00 m)": [(6.40, 28.8, 27.7), (10.46, 28.8, None), (12.00, 26.8, None), (13.00, 22.2, None), (14.00, 18.1, None)],
    "Push-Pull Prop RS I (1.84-2.94 m)": [(1.84, 16.3, 12.7), (2.45, 16.3, None), (2.75, 14.6, None), (2.94, 12.5, None)],
    "Push-Pull Prop RS II (2.56-4.06 m)": [(2.56, 16.3, 12.7), (2.97, 16.3, None), (3.37, 11.7, None), (3.77, 8.5, None), (4.06, 7.0, None)],
    "Push-Pull Prop RSS I (2.05-2.94 m)": [(2.05, 34.2, 26.3), (2.30, 33.2, None), (2.60, 22.7, None), (2.94, 14.2, None)],
    "Push-Pull Prop RSS II (2.91-3.80 m)": [(2.91, 31.7, 26.3), (3.21, 26.4, None), (3.50, 17.1, None), (3.80, 11.6, None)],
    "Push-Pull Prop RSS III (4.60-6.00 m)": [(4.60, 27.8, 20.0), (4.95, 22.8, None), (5.30, 18.6, None), (5.65, 14.7, None), (6.00, 11.1, None)],
    "Compression Brace SKS 2 (1.75-2.33 m)": [(1.75, 189.5, None), (1.90, 195.2, None), (2.05, 178.4, 63.8), (2.20, 166.4, None), (2.33, 141.6, None)],
    "Compression Brace SKS 4 (2.55-3.13 m)": [(2.55, 171.4, None), (2.70, 164.4, None), (2.85, 154.7, None), (3.00, 143.0, None), (3.13, 123.3, None)],
    "Adjustable Brace CB 164-224 (1.64-2.24 m)": [(1.64, 137.1, None), (1.79, 121.4, None), (1.94, 105.6, None), (2.09, 101.9, None), (2.24, 97.0, None)],
    "Strut VARIOKIT (2.75-4.50 m)": [(2.75, 160.0, 160.0), (4.50, 160.0, None)],
    "Strut VARIOKIT (4.00-7.00 m)": [(4.00, 160.0, 160.0), (7.00, 160.0, None)],
    "Strut VARIOKIT (6.00-9.00 m)": [(6.00, 160.0, None), (6.80, 160.0, None), (7.00, 160.0, None), (8.00, 146.5, None), (9.00, 122.9, None)],
    "SLS 40/80 (0.40-0.80 m)": [(0.40, 88.0, 70.8), (0.80, 88.0, None)],
    "SLS 80/140 (0.80-1.40 m)": [(0.80, 107.1, 81.6), (1.40, 107.1, None)],
    "SLS 100/180 (1.00-1.80 m)": [(1.00, 107.1, None), (1.50, 107.1, None), (1.60, 105.5, None), (1.80, 90.4, None)],
    # Add more prop types as needed...
}

def interpolate_value(x: float, x0: float, y0: float, x1: float, y1: float) -> float:
    """Linear interpolation between two points."""
    if y1 is None or y0 is None:
        return None
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def get_capacities(prop_type: str, length: float) -> Tuple[Optional[float], Optional[float]]:
    """Calculate compression and tension capacities for given prop and length."""
    data = props_data[prop_type]
    min_length = data[0][0]
    max_length = data[-1][0]
    
    if length < min_length or length > max_length:
        return None, None
    
    # Find the bracketing data points
    for i in range(len(data)-1):
        if data[i][0] <= length <= data[i+1][0]:
            comp = interpolate_value(length, data[i][0], data[i][1], data[i+1][0], data[i+1][1])
            # Tension is only specified at minimum length for most props
            tension = data[i][2] if length == data[i][0] else None
            return comp, tension
    
    # Exact match at a data point
    for length_val, comp, tension in data:
        if length == length_val:
            return comp, tension
    
    return None, None

# Streamlit app
st.title("Push-Pull Prop Capacity Calculator")

# Prop selection
prop_type = st.selectbox("Select Prop Type", list(props_data.keys()))

# Get min and max lengths for selected prop
min_length = props_data[prop_type][0][0]
max_length = props_data[prop_type][-1][0]

# Length input
length = st.number_input(
    "Enter Extension Length (m)",
    min_value=min_length,
    max_value=max_length,
    value=min_length,
    step=0.01
)

if st.button("Calculate Capacities"):
    comp_capacity, tension_capacity = get_capacities(prop_type, length)
    
    if comp_capacity is not None:
        st.write(f"Permissible Compressive Force: {comp_capacity:.1f} kN")
        if tension_capacity is not None:
            st.write(f"Permissible Tension Force: {tension_capacity:.1f} kN")
        else:
            st.write("Permissible Tension Force: Only specified at minimum length")
    else:
        st.error("Error calculating capacities. Please check input values.")

st.write(f"Note: Valid length range for {prop_type} is {min_length:.2f} m to {max_length:.2f} m")
