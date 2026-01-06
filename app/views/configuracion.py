import streamlit as st
import pandas as pd
import os

def show_config_view():
    st.markdown("## ⚙️ Configuración y Datos Fuente")
    st.markdown("Inspecciona los datos reales que alimentan el modelo de Inteligencia Artificial.")
    st.divider()

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, 'data')

    tab1, tab2, tab3 = st.tabs(["📂 Datos de Gastos", "📂 Datos de Ingresos", "🔧 Sistema"])

    with tab1:
        st.subheader("Base de Datos: Gastos (SIAF)")
        try:
            df_gastos = pd.read_csv(os.path.join(data_dir, 'gastos.csv'), sep=';', encoding='latin-1', dtype=str)
            st.dataframe(df_gastos.head(50), use_container_width=True)
            st.caption(f"Total de registros cargados: {len(df_gastos)}")
        except Exception as e:
            st.error(f"Error cargando gastos.csv: {e}")

    with tab2:
        st.subheader("Base de Datos: Ingresos (SIAF)")
        try:
            df_ingresos = pd.read_csv(os.path.join(data_dir, 'ingresos.csv'), sep=';', encoding='latin-1', dtype=str)
            st.dataframe(df_ingresos.head(50), use_container_width=True)
            st.caption(f"Total de registros cargados: {len(df_ingresos)}")
        except Exception as e:
            st.error(f"Error cargando ingresos.csv: {e}")

    with tab3:
        st.subheader("Parámetros Técnicos del Sistema")      

        # DataFrame para mostrar la info
        info_sistema = {
            "Parámetro": [
                "Versión del Aplicativo", 
                "Modelo de IA", 
                "Pipeline CI/CD", 
                "Equipo Desarrollador"
            ],
            "Descripción": [
                "1.2.0 (Stable Release)", 
                "K-Means Clustering (Scikit-Learn)", 
                "GitHub Actions (Automatizado)", 
                "Ingeniería de Sistemas - UNA Puno"
            ]
        }
        df_sistema = pd.DataFrame(info_sistema)
        
        st.table(df_sistema)