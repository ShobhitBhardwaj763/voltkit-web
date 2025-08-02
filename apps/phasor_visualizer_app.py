import os
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from voltkit.core import phasor_components, time_domain_signal, to_rect, to_polar

# App Config
st.set_page_config(page_title="Phasor Diagram Visualizer", layout="centered")
st.title("📐 Phasor Diagram & Waveform Explorer")

# Sidebar Inputs
st.sidebar.header("🧮 Phasor Parameters")
signal_type = st.sidebar.selectbox("Signal Type", ["Voltage", "Current"])
magnitude = st.sidebar.slider("Magnitude (V or A)", 1.0, 100.0, 10.0)
angle = st.sidebar.slider("Phase Angle (°)", -180, 180, 30)
frequency = st.sidebar.slider("Frequency (Hz)", 10, 100, 50)

# Generate time-domain signal
t = np.linspace(0, 0.05, 1000)
y = time_domain_signal(magnitude, angle, frequency, t)

# Phasor coordinates
x, y_rect = phasor_components(magnitude, angle)
phasor_complex = to_rect(magnitude, angle)
mag, ang = to_polar(phasor_complex)

# Layout
col1, col2 = st.columns(2)

# Plot Phasor Diagram
with col1:
    fig1, ax1 = plt.subplots()
    ax1.arrow(0, 0, x, y_rect, head_width=2, head_length=3, color='blue')
    ax1.set_xlim(-magnitude - 5, magnitude + 5)
    ax1.set_ylim(-magnitude - 5, magnitude + 5)
    ax1.set_title(f"{signal_type} Phasor Diagram")
    ax1.set_xlabel("Real Axis")
    ax1.set_ylabel("Imaginary Axis")
    ax1.grid(True)
    ax1.axhline(0, color='gray', lw=0.5)
    ax1.axvline(0, color='gray', lw=0.5)
    st.pyplot(fig1)

# Plot Time-Domain Signal
with col2:
    fig2, ax2 = plt.subplots()
    ax2.plot(t * 1000, y, color='green', label=f"{signal_type} Signal")
    ax2.set_title("Time-Domain Signal")
    ax2.set_xlabel("Time (ms)")
    ax2.set_ylabel("Amplitude")
    ax2.grid(True)
    ax2.legend()
    st.pyplot(fig2)

# Phasor Info
st.markdown("---")
st.subheader("📊 Phasor Information")
st.write(f"**Rectangular Form:** {phasor_complex.real:.2f} + {phasor_complex.imag:.2f}j")
st.write(f"**Polar Form:** {mag:.2f} ∠ {ang:.2f}°")
