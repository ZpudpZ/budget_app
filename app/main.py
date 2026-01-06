import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from styles import load_css
from model_loader import load_models
from views.analisis import show_analysis_view

# Configuración Inicial
st.set_page_config(
    page_title="Budget Intelligence Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilos CSS
load_css()

# Cargar Modelos (Backend)
kmeans, scaler, model_loaded = load_models()

# Sidebar de Navegación
with st.sidebar:
    st.markdown("### Navegación")
    page = st.radio(
        "Ir a:", 
        ["Análisis", "Reportes", "Historial", "Ayuda", "Configuración"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### Estado del Sistema")
    if model_loaded:
        st.success("✅ IA Activa")
    else:
        st.warning("⚠️ Modo Simulación")
        
    st.markdown("---")
    st.info("**Budget Intelligence**\n\nSistema de análisis presupuestal con IA para el sector público peruano.")

# Header Principal
st.markdown("""
<div class="main-header">
    <h1 class="main-title">Budget Intelligence Dashboard</h1>
    <p class="subtitle">Análisis Presupuestal Inteligente - Perú</p>
</div>
""", unsafe_allow_html=True)

# Enrutador de Páginas
if page == "Análisis":
    show_analysis_view(kmeans, scaler, model_loaded)

elif page == "Reportes":
    st.title("Generación de Reportes")
    st.info("🚧 Módulo en construcción. Aquí podrás exportar PDFs con tus análisis.")

else:
    st.info(f"Has seleccionado la página: {page}")