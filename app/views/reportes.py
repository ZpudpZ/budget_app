import streamlit as st
import pandas as pd
import datetime

def show_reports_view():
    st.markdown("## 📑 Centro de Reportes")
    st.markdown("Generación de documentos de auditoría y trazabilidad de análisis.")
    st.divider()

    # Reporte actual
    st.subheader("📄 Último Análisis Generado")

    if 'ultimo_analisis' not in st.session_state:
        st.info("👋 **No hay reportes pendientes.**")
        st.caption("Ve a la pestaña 'Análisis' y ejecuta una simulación.")
    else:
        datos = st.session_state['ultimo_analisis']
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        # Tarjeta de Vista Previa
        with st.container():
            st.markdown(f"""
            <div style="background-color: white; color: black; padding: 30px; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                <div style="border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; display: flex; justify-content: space-between;">
                    <strong>REPORTE TÉCNICO DE GESTIÓN PRESUPUESTAL</strong>
                    <span>{fecha}</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <p style="margin:0; color:#666;">Diagnóstico IA:</p>
                        <h3 style="margin:0;">{datos['perfil']['status']}</h3>
                        <p>Cluster #{datos['cluster']}</p>
                    </div>
                    <div style="text-align: right;">
                        <p style="margin:0; color:#666;">ID Auditoría:</p>
                        <code>{hash(str(datos)) % 1000000}</code>
                    </div>
                </div>
                <hr style="margin: 20px 0;">
                <p><strong>Detalle de Indicadores:</strong></p>
                <ul>
                    <li>Ejecución de Ingresos: {datos['ingresos']*100:.1f}%</li>
                    <li>Ejecución de Gastos: {datos['gastos']*100:.1f}%</li>
                    <li>Ratio Gasto/Ingreso: {datos['ratio_gi']}</li>
                    <li>Ratio Saldo/Gasto: {datos['ratio_saldo']}</li>
                </ul>
                <div style="background: #f9f9f9; padding: 10px; margin-top: 20px; font-size: 0.9rem;">
                    <em>Conclusión: {datos['perfil']['descripcion']}</em>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Botón de Descarga
            df_export = pd.DataFrame([datos])
            csv = df_export.to_csv(index=False).encode('utf-8')
            
            st.download_button(
                label="💾 Descargar Reporte Oficial (CSV)",
                data=csv,
                file_name=f"auditoria_fiscal_{fecha.replace('/','-')}.csv",
                mime="text/csv",
                type="primary"
            )

    st.divider()

    # Historial de sesion
    st.subheader("🕒 Historial de Sesión")
    st.markdown("Registro de todos los análisis realizados desde que abriste la aplicación.")

    if 'historial_sesion' in st.session_state and st.session_state['historial_sesion']:
        df_historial = pd.DataFrame(st.session_state['historial_sesion'])
        st.dataframe(df_historial, use_container_width=True, hide_index=True)
        
        if st.button("🗑️ Limpiar Historial"):
            st.session_state['historial_sesion'] = []
            st.rerun()
    else:
        st.caption("El historial está vacío.")