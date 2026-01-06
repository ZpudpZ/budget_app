import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* Header Principal */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .main-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }
    .subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    /* Tarjetas de Métricas y Resultados */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .result-card {
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        color: white;
    }
    
    /* Colores de Clusters */
    .cluster-0 { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }
    .cluster-1 { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); }
    .cluster-2 { background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); }
    .cluster-3 { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); }
    .cluster-4 { background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); }

    /* Badges y Botones */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        background: rgba(255,255,255,0.2);
        font-weight: 600;
        margin-top: 0.5rem;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        width: 100%;
        font-size: 1.1rem;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Features Cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        text-align: center;
        transition: transform 0.3s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Ajustes Sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8fafc 0%, #e2e8f0 100%);
    }
    </style>
    """, unsafe_allow_html=True)