import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image

image = Image.open("voltkit_page_logo.png")

# Page Configuration
st.set_page_config(page_title= "VoltKit Simulations", layout="centered", page_icon=image)

# Custom Style
st.markdown("""
<style>
            .main-title{
            font-size:2.5em;
            font-weight: bold;
            color: #004466;
            }

            .sub-title {
            font-size:1.2em;
            color: #444444;
            }

            .description {
            font-size : 1.05em;
            line-height:1.6;
            }
        footer {visibility : hidden;}
</style>
""", unsafe_allow_html = True)

# Sidebae Nevigation

with st.sidebar:
    selected = option_menu (
        menu_title = "Simulations",
        options = [
            "Home",
            "Signal Generator",
            "FFT Explorer",
            "Bode Plot",
            "RC Step Response",
            "Phasor Diagram Viewer"
        ],
        icons = ["house", "activity", "search", "bar-chart", "clock", "rulers", "graph-up"],
        menu_icon = "cast", default_index=0
    )

# Content Selecting

if selected == "Home":
    st.markdown("<div class='main-title'>⚡ Welcome to VoltKit</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>A Python-powered lab assistant for Electrical and Electronics Engineering</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.image('voltkit_logo.png', width=300)

    st.markdown("""
    <div class='description'>
        <b>VoltKit</b> is more than just a Python library — it's your digital companion for exploring, learning, and visualizing EE concepts through code and simulations.
        <br><br>
        Whether you're a student, educator, or engineer, VoltKit helps you:
        <ul>
            <li>🧮 Simplify circuit calculations (Ohm’s Law, impedance, AC power)</li>
            <li>📡 Generate and analyze signals (sine, square, FFT, harmonics)</li>
            <li>📊 Visualize core concepts interactively (phasors, filters, Bode plots)</li>
            <li>🧪 Experiment with real-time Streamlit simulations</li>
        </ul>
        <br>
        <b>Start exploring now →</b> Choose a simulation from the sidebar menu!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    🌐 <a href='https://github.com/ShobhitBhardwaj763/voltkit' target='_blank'>View Library on GitHub</a>  
    📘 <a href='https://colab.research.google.com/drive/1gL6y9mrg4zuumT950I7BGJqbdwQnsePH' target='_blank'>Explore the Rulebook (Colab)</a>  
    📩 Contact: voltkit.dev@gmail.com  
    """, unsafe_allow_html=True)

    st.caption("🚀 Built with ❤️ using Python, Streamlit, and Open Source power.")

# Selecting Apps to open

elif selected == "Signal Generator":
    exec(open("apps/signal_generator_app.py", encoding="utf-8").read())

elif selected == "FFT Explorer":
    exec(open("apps/fft_explorer_app.py", encoding="utf-8").read())

elif selected == "Bode Plot":
    exec(open("apps/bode_simulator_app.py", encoding="utf-8").read())

elif selected == "RC Step Response":
    exec(open("apps/rc_visualizer_app.py", encoding="utf-8").read())

# elif selected == "Phase Visualizer":
  #  exec(open("apps/phasor_visualizer_app.py",encoding="utf-8").read())

elif selected == "Phasor Diagram Viewer":
    exec(open("apps/phasor_diagram_visualizer_app.py", encoding="utf-8").read())
    
    
    
    
    
