import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* --- FUENTES --- */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* --- HEADER PRINCIPAL (El gradiente morado original) --- */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        color: white;
        text-align: center;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    .subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }

    /* --- TARJETAS DE RESULTADOS --- */
    .result-card {
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15);
        color: white;
        transition: transform 0.3s ease;
    }
    .result-card:hover {
        transform: translateY(-5px);
    }

    /* --- COLORES DE CLUSTERS (Originales) --- */
    .cluster-0 { background: linear-gradient(135deg, #10b981 0%, #059669 100%); } /* Verde */
    .cluster-1 { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); } /* Azul */
    .cluster-2 { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); } /* Amarillo */
    .cluster-3 { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); } /* Rojo */
    .cluster-4 { background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); } /* Violeta */

    /* --- BADGES Y TEXTOS --- */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        background: rgba(255,255,255,0.2);
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* --- TARJETAS DE FEATURES (Footer) --- */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        text-align: center;
        height: 100%;
        border-top: 4px solid #667eea;
    }
    .feature-card h4 {
        margin: 10px 0 5px 0;
        color: #333;
    }
    .feature-card p {
        font-size: 0.9rem;
        color: #666;
    }

    /* --- BOTONES --- */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)