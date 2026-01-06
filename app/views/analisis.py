import streamlit as st
import numpy as np

from model_loader import predict_cluster

def show_analysis_view(kmeans, scaler, model_loaded):
    # --- Sección Hero ---
    st.markdown("## Evalúa tu Gestión Presupuestal")
    st.markdown("##### Utiliza inteligencia artificial para clasificar y optimizar la ejecución de tu presupuesto público")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Guía Expandible (Líneas 141-176 del PDF) ---
    with st.expander("ℹ️ ¿Cómo ingresar los datos? - Guía rápida", expanded=False):
        st.markdown("""
        ### No necesitas ser experto. Solo responde estas preguntas simples:
        
        **1. Ejecución de Ingresos** (Ej. 0.95 = 95%)
        * ¿Qué porcentaje del dinero planificado realmente se recaudó?
        
        **2. Ejecución de Gastos** (Ej. 0.70 = 70%)
        * ¿Qué porcentaje del dinero disponible realmente se gastó?
        
        **3. Ratio Gasto / Ingreso** (Ej. 0.70)
        * ¿Cuánto gastaste en relación al dinero que ingresó? (< 1.0 es Superávit)
        
        **4. Ratio Saldo / Gasto** (Ej. 0.43)
        * ¿Cuánto dinero quedó sin gastar respecto a lo que sí se gastó?
        """)

    # --- Formulario de Entrada (Líneas 178-242 del PDF) ---
    st.markdown("### Ingresa tus Indicadores Presupuestales")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 1. Ejecución de Ingresos")
        ingresos = st.slider(
            "Valor (Ingresos):",
            min_value=0.0, max_value=1.2, value=1.0, step=0.01,
            format="%.2f",
            key="ingresos",
            help="1.00 = Recaudaste todo lo planificado"
        )
        st.info(f"📊 **{ingresos*100:.1f}%** del presupuesto de ingresos")

        st.markdown("#### 3. Ratio Gasto / Ingreso")
        ratio_gi = st.slider(
            "Valor (Gasto/Ingreso):",
            min_value=0.0, max_value=1.5, value=0.5, step=0.01,
            format="%.2f",
            key="ratio_gi"
        )
        if ratio_gi < 1.0:
            st.success(f"Gastaste **{ratio_gi*100:.1f}%** de lo que ingresó (Superávit)")
        elif ratio_gi == 1.0:
            st.warning("Gastaste todo lo que ingresó (Equilibrio)")
        else:
            st.error(f"Gastaste **{ratio_gi*100:.1f}%** de lo que ingresó (Déficit)")

    with col2:
        st.markdown("#### 2. Ejecución de Gastos")
        gastos = st.slider(
            "Valor (Gastos):",
            min_value=0.0, max_value=1.2, value=0.7, step=0.01,
            format="%.2f",
            key="gastos",
            help="1.00 = Gastaste todo el presupuesto"
        )
        st.info(f"💸 **{gastos*100:.1f}%** del presupuesto de gastos")

        st.markdown("#### 4. Ratio Saldo / Gasto")
        ratio_saldo = st.slider(
            "Valor (Saldo/Gasto):",
            min_value=0.0, max_value=1.2, value=0.9, step=0.01,
            format="%.2f",
            key="ratio_saldo"
        )
        if ratio_saldo > 0.5:
            st.success(f"Sobró bastante dinero (Ratio: {ratio_saldo:.2f})")
        elif ratio_saldo > 0.2:
            st.warning(f"Sobró algo de dinero (Ratio: {ratio_saldo:.2f})")
        else:
            st.error(f"Sobró poco o nada (Ratio: {ratio_saldo:.2f})")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Botón y Lógica de Análisis ---
    if st.button("🔍 Analizar Comportamiento Fiscal"):
        with st.spinner("Analizando datos con IA..."):
            
            # Llamamos a la lógica encapsulada en model_loader.py
            data = [ingresos, gastos, ratio_gi, ratio_saldo]
            cluster_id, perfil = predict_cluster(kmeans, scaler, model_loaded, data)

            # Renderizamos la tarjeta de resultados (HTML del PDF limpio)
            st.markdown(f"""
            <div class="result-card cluster-{cluster_id}">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1.5rem;">
                    <div>
                        <p style="font-size: 0.9rem; opacity: 0.9; margin: 0;">Estado Fiscal</p>
                        <h2 style="font-size: 2.5rem; margin: 0.5rem 0;">{perfil['icono']} {perfil['status']}</h2>
                    </div>
                    <div class="status-badge">Cluster {cluster_id}</div>
                </div>
                <h3 style="font-size: 1.8rem; margin-bottom: 1rem;">{perfil['titulo']}</h3>
                <p style="font-size: 1.1rem; opacity: 0.95; line-height: 1.6;">{perfil['descripcion']}</p>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.3);">
                    <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 10px;">
                        <p style="font-size: 0.85rem; opacity: 0.9; margin: 0;">Ejecución Ingresos</p>
                        <p style="font-size: 2rem; font-weight: 700; margin: 0.5rem 0 0 0;">{ingresos*100:.1f}%</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.15); padding: 1rem; border-radius: 10px;">
                        <p style="font-size: 0.85rem; opacity: 0.9; margin: 0;">Ejecución Gastos</p>
                        <p style="font-size: 2rem; font-weight: 700; margin: 0.5rem 0 0 0;">{gastos*100:.1f}%</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
    # --- Features (Pie de página del PDF) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Características de la Plataforma")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card"><h4>🧠 Análisis Inteligente</h4><p>Machine Learning para clasificar el comportamiento presupuestal</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><h4>📊 Decisiones Informadas</h4><p>Soporte para la toma de decisiones en gestión pública</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><h4>👀 Monitoreo Continuo</h4><p>Evaluación constante de la eficiencia presupuestal</p></div>', unsafe_allow_html=True)