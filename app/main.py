import streamlit as st
import sys
import os

# Configurar rutas para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from styles import load_css
from model_loader import load_models, predict_cluster 
from views.analisis import show_analysis_view

# Configuración de la Página
st.set_page_config(
    page_title="Budget Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar Estilos y Modelos
load_css()
kmeans, scaler, model_loaded = load_models()

# SIDEBAR
with st.sidebar:
    st.title("Navegación")
    opcion = st.radio("Ir a:", ["Análisis", "Reportes", "Configuración"])
    
    st.markdown("---")
    st.caption("Estado del Sistema")
    if model_loaded:
        st.success("✅ IA Activa (K-Means)")
    else:
        st.warning("⚠️ Modo Simulación")
        
    st.info("Sistema de Análisis Presupuestal v1.0")

# HEADER
st.markdown("""
<div class="main-header">
    <h1 class="main-title">Budget Intelligence Dashboard</h1>
    <p class="subtitle">Análisis Fiscal con Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)

# RUTAS
if opcion == "Análisis":
    show_analysis_view(kmeans, scaler, model_loaded, predict_cluster)

elif opcion == "Reportes":
    st.title("📂 Reportes Automatizados")
    st.info("Generación de PDFs para auditoría (En construcción por equipo MLOps).")

else:
    st.title("⚙️ Configuración")
    st.write("Parámetros del modelo y conexión a base de datos.")