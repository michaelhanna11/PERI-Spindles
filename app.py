import streamlit as st
import pandas as pd
from typing import Dict, Tuple, Optional

# Data structure containing all prop information
props_data = {
    "Push-Pull Prop RS 210 (1.30-2.10 m)": [(1.30, 25.0, 25.0), (2.00, 25.0, 25.0), (2.10, 23.6, 25.0)],
    "Push-Pull Prop RS 260 (2.30-2.60 m)": [(2.30, 25.0, 25.0), (2.60, 22.1, 25.0)],
    "Push-Pull Prop RS 300 (1.90-3.00 m)": [(1.90, 25.0, 25.0), (2.30, 25.0, 25.0), (2.50, 21.6, 25.0), (3.00, 14.2, 25.0)],
    "Push-Pull Prop RS 450 (2.80-4.50 m)": [(2.80, 25.0, 25.0), (3.60, 25.0, 25.0), (4.00, 17.2, 25.0), (4.50, 11.8, 25.0)],
    "Push-Pull Prop RS 650 (4.30-6.50 m)": [(4.30, 25.0, 25.0), (4.90, 25.0, 25.0), (5.00, 24.4, 25.0), (5.50, 19.5, 25.0), (6.00, 15.9, 25.0), (6.50, 13.2, 25.0)],
    "Push-Pull Prop RS 1000 (6.40-10.00 m)": [(6.40, 34.2, 29.0), (6.64, 34.2, 29.0), (7.64, 25.9, 29.0), (8.44, 20.3, 29.0), (9.24, 16.0, 29.0), (10.00, 12.8, 29.0)],
    "Push-Pull Prop RS 1400 (6.40-14.00 m)": [(6.40, 28.8, 27.7), (10.46, 28.8, 27.7), (12.00, 26.8, 27.7), (13.00, 22.2, 27.7), (14.00, 18.1, 27.7)],
    "Push-Pull Prop RS I (1.84-2.94 m)": [(1.84, 16.3, 12.7), (2.45, 16.3, 12.7), (2.75, 14.6, 12.7), (2.94, 12.5, 12.7)],
    "Push-Pull Prop RS II (2.56-4.06 m)": [(2.56, 16.3, 12.7), (2.97, 16.3, 12.7), (3.37, 11.7, 12.7), (3.77, 8.5, 12.7), (4.06, 7.0, 12.7)],
    "Push-Pull Prop RSS I (2.05-2.94 m)": [(2.05, 34.2, 26.3), (2.30, 33.2, 26.3), (2.60, 22.7, 26.3), (2.94, 14.2, 26.3)],
    "Push-Pull Prop RSS II (2.91-3.80 m)": [(2.91, 31.7, 26.3), (3.21, 26.4, 26.3), (3.50, 17.1, 26.3), (3.80, 11.6, 26.3)],
    "Push-Pull Prop RSS III (4.60-6.00 m)": [(4.60, 27.8, 20.0), (4.95, 22.8, 20.0), (5.30, 18.6, 20.0), (5.65, 14.7, 20.0), (6.00, 11.1, 20.0)],
    "Kicker AV 82 (0.50-0.82 m)": [(0.50, 34.1, 26.3), (0.66, 28.9, 26.3), (0.82, 23.2, 26.3),
    "Kicker AV 111 (0.79-1.11 m)": [(0.79, 30.9, 26.3), (0.95, 24.9, 26.3), (1.11, 19.7, 26.3),
    "Kicker AV 140 (1.08-1.40 m)": [(1.08, 25.7, 26.3), (1.24, 20.0, 26.3), (1.40, 15.7, 26.3),
    "Kicker AV 190 (1.08-1.90 m)": [(1.08, 39.2, 21.1), (1.25, 38.5, 21.1), (1.50, 37.4, 21.1), (1.75, 34.6, 21.1), (1.90, 31.3, 21.1),
    "Kicker AV 210 (1.28-2.10 m)": [(1.28, 34.2, 26.3), (1.69, 34.2, 26.3), (1.90, 25.5, 26.3), (2.10, 19.0, 26.3),
    "Kicker AV RSS III (2.03-2.92 m)": [(2.03, 34.2, 26.3), (2.30, 33.2, 26.3), (2.60, 22.7, 26.3), (2.94, 14.2, 26.3),
    "Compression Brace SKS 2 (1.35-1.93 m)": [(1.35, 196.2, 63.8), (1.50, 191.5, 63.8), (1.65, 186.1, 63.8), (1.80, 175.6, 63.8), (1.93, 149.4, 63.8)],
    "Compression Brace SKS 3 (1.75-2.33 m)": [(1.75, 189.5, 63.8), (1.90, 195.2, 63.8), (2.05, 178.4, 63.8), (2.20, 166.4, 63.8), (2.33, 141.6, 63.8)],
    "Compression Brace SKS 4 (2.55-3.13 m)": [(2.55, 171.4, 63.8), (2.70, 164.4, 63.8), (2.85, 154.7, 63.8), (3.00, 143.0, 63.8), (3.13, 123.3, 63.8)],
    "Adjustable Brace CB 164-224 (1.64-2.24 m)": [(1.64, 137.1, 102.0), (1.79, 121.4, 102.0), (1.94, 105.6, 102.0), (2.09, 101.9, 102.0), (2.24, 97.0, 102.0)],
    "Strut VARIOKIT (2.75-4.50 m)": [(2.75, 160.0, 160.0), (4.50, 160.0, 160.0)],
    "Strut VARIOKIT (4.00-7.00 m)": [(4.00, 160.0, 160.0), (7.00, 160.0, 160.0)],
    "Strut VARIOKIT (6.00-9.00 m)": [(6.00, 160.0, 159.7), (6.80, 160.0, 159.7), (7.00, 160.0, 159.7), (8.00, 146.5, 159.7), (9.00, 122.9, 159.7)],
    "SLS 40/80 (0.40-0.80 m)": [(0.40, 88.0, 70.8), (0.80, 88.0, 70.8)],
    "SLS 80/140 (0.80-1.40 m)": [(0.80, 107.1, 81.6), (1.40, 107.1, 81.6)],
    "SLS 100/180 (1.00-1.80 m)": [(1.00, 107.1, 81.6), (1.50, 107.1, 81.6), (1.60, 105.5, 81.6), (1.80, 90.4, 81.6)],
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
