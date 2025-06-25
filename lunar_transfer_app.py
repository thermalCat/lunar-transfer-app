import streamlit as st
import numpy as np
from simulate_earth_moon_transfer import simulate_transfer

st.set_page_config(layout="wide")
st.title("🌕 Earth-to-Moon Transfer Simulator")

st.sidebar.header("Initial Conditions")

x0_km = st.sidebar.number_input("Initial X Position (km)", value=6771.0, step=10.0)
y0_km = st.sidebar.number_input("Initial Y Position (km)", value=0.0, step=10.0)
vx0_kms = st.sidebar.number_input("Initial X Velocity (km/s)", value=0.0, step=0.1)
vy0_kms = st.sidebar.number_input("Initial Y Velocity (km/s)", value=10.9, step=0.1)

sim_time_days = st.sidebar.slider("Simulation Duration (days)", 1, 15, 5)
dt_sec = st.sidebar.selectbox("Time Step (seconds)", [10, 50, 100, 250, 500], index=2)

animate = st.sidebar.checkbox("Live Animation", value=False)
run = st.sidebar.button("🚀 Run Simulation")

if run:
    x0 = np.array([x0_km * 1e3, y0_km * 1e3])
    v0 = np.array([vx0_kms * 1e3, vy0_kms * 1e3])
    st.write("Simulating...")

    result = simulate_transfer(x0, v0, t_max=sim_time_days * 24 * 3600, dt=dt_sec, plot=animate)

    if result["outcome"] == "collision":
        st.error(f"☄️ Collision with {result['body']} at t = {result['time']:.1f} seconds.")
    else:
        st.success(f"✅ No collision. Nearest approach to Moon: {result['nearest_approach_km']:.1f} km")
        st.write(f"Closest point (km): {result['closest_point_km']}")
