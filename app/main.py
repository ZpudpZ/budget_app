import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from styles import load_css
from model_loader import load_models, predict_cluster 
# Importamos las nuevas vistas
from views.analisis import show_analysis_view
from views.reportes import show_reports_view
from views.configuracion import show_config_view

st.set_page_config(
    page_title="Budget Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
kmeans, scaler, model_loaded = load_models()

# --- SIDEBAR ---
with st.sidebar:
    st.title("Navegación")
    opcion = st.radio("Ir a:", ["Análisis", "Reportes", "Configuración"])
    
    st.markdown("---")
    st.caption("Estado del Sistema")
    if model_loaded:
        st.success("✅ IA Activa (K-Means)")
    else:
        st.warning("⚠️ Modo Simulación")

# --- HEADER ---
st.markdown("""
<div class="main-header">
    <h1 class="main-title">Budget Intelligence Dashboard</h1>
    <p class="subtitle">Análisis Fiscal con Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)

# --- ENRUTAMIENTO ---
if opcion == "Análisis":
    show_analysis_view(kmeans, scaler, model_loaded, predict_cluster)

elif opcion == "Reportes":
    # Llamamos a la nueva vista de reportes
    show_reports_view()

elif opcion == "Configuración":
    # Llamamos a la nueva vista de configuración
    show_config_view()