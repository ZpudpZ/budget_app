import streamlit as st
import textwrap

def show_analysis_view(kmeans, scaler, model_loaded, predict_function):
    
    # Titulo
    st.markdown("## ")
    st.markdown("##### Utiliza inteligencia artificial para clasificar y optimizar la ejecución de tu presupuesto público")
    
    # Guia Desplegable
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

    st.markdown("<br>", unsafe_allow_html=True)

    # Formulario de indicadores
    st.subheader("Ingresa tus Indicadores Presupuestales")
    
    with st.container():
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("#### 1. Ejecución de Ingresos")
            ingresos = st.slider("Valor (Ingresos):", 0.0, 1.2, 1.0, 0.01)
            st.caption(f"📊 {ingresos*100:.1f}% del presupuesto de ingresos")
            
            st.markdown("#### 3. Ratio Gasto / Ingreso")
            ratio_gi = st.slider("Valor (Gasto/Ingreso):", 0.0, 1.5, 0.5, 0.01)
            
            if ratio_gi < 1.0:
                st.success(f"Superávit ({ratio_gi*100:.1f}%)")
            else:
                st.error(f"Déficit ({ratio_gi*100:.1f}%)")

        with col2:
            st.markdown("#### 2. Ejecución de Gastos")
            gastos = st.slider("Valor (Gastos):", 0.0, 1.2, 0.7, 0.01)
            st.caption(f"💸 {gastos*100:.1f}% del presupuesto de gastos")
            
            st.markdown("#### 4. Ratio Saldo / Gasto")
            ratio_saldo = st.slider("Valor (Saldo/Gasto):", 0.0, 1.5, 0.9, 0.01)
            
            if ratio_saldo > 0.5:
                st.success(f"Respaldo Alto ({ratio_saldo:.2f})")
            else:
                st.warning(f"Respaldo Bajo ({ratio_saldo:.2f})")

    st.markdown("<br>", unsafe_allow_html=True)

    # Boton analisis
    if st.button("🔍 Analizar Comportamiento Fiscal", type="primary", use_container_width=True):
        
        with st.spinner("Procesando datos con IA..."):
            # Lógica de predicción
            data = [ingresos, gastos, ratio_gi, ratio_saldo]
            cluster_id, perfil = predict_function(kmeans, scaler, model_loaded, data)

            import datetime
            nuevo_registro = {
                'Timestamp': datetime.datetime.now().strftime("%H:%M:%S"),
                'Ingresos': f"{ingresos*100:.0f}%",
                'Gastos': f"{gastos*100:.0f}%",
                'Ratio G/I': ratio_gi,
                'Ratio S/G': ratio_saldo,
                'Cluster': cluster_id,
                'Estado': perfil['status']
            }

            st.session_state['ultimo_analisis'] = {
                'ingresos': ingresos,
                'gastos': gastos,
                'ratio_gi': ratio_gi,
                'ratio_saldo': ratio_saldo,
                'cluster': cluster_id,
                'perfil': perfil
            }

            if 'historial_sesion' not in st.session_state:
                st.session_state['historial_sesion'] = []

            st.session_state['historial_sesion'].insert(0, nuevo_registro)

            html_code = f"""
            <div class="result-card cluster-{cluster_id}" style="color: white; border-radius: 15px; padding: 25px; margin-top: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
            <p style="margin: 0; opacity: 0.8; font-size: 0.9rem;">Estado Fiscal</p>
            <h2 style="margin: 5px 0; font-size: 2.2rem;">{perfil['icono']} {perfil['status']}</h2>
            </div>
            <div class="status-badge">Cluster {cluster_id}</div>
            </div>
            <h3 style="margin-top: 20px;">{perfil['titulo']}</h3>
            <p style="font-size: 1.1rem; opacity: 0.95;">{perfil['descripcion']}</p>
            <hr style="border-color: rgba(255,255,255,0.2); margin: 20px 0;">
            <div style="display: flex; gap: 15px;">
            <div style="background: rgba(0,0,0,0.2); padding: 15px; border-radius: 10px; flex: 1; text-align: center;">
            <small>Ingresos</small><br>
            <strong style="font-size: 1.4rem;">{ingresos*100:.0f}%</strong>
            </div>
            <div style="background: rgba(0,0,0,0.2); padding: 15px; border-radius: 10px; flex: 1; text-align: center;">
            <small>Gastos</small><br>
            <strong style="font-size: 1.4rem;">{gastos*100:.0f}%</strong>
            </div>
            </div>
            </div>
            """
            st.markdown(html_code, unsafe_allow_html=True)
            st.success("✅ Análisis agregado al historial. Ve a 'Reportes' para verlo.")

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card"><h4>🧠 Análisis IA</h4><p>Clasificación K-Means</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><h4>📊 Data-Driven</h4><p>Histórico MEF</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><h4>🛡️ MLOps</h4><p>Mantenimiento Automático</p></div>', unsafe_allow_html=True)