import joblib
import numpy as np
import os

# Definición de Perfiles
PERFILES = {
    0: {"titulo": "Alta Eficiencia", "descripcion": "Excelente recaudación con gasto controlado.", "status": "Eficiente", "icono": "✅"},
    1: {"titulo": "Gestión Equilibrada", "descripcion": "Balance adecuado entre ingresos y gastos.", "status": "Equilibrada", "icono": "⚖️"},
    2: {"titulo": "Ingresos Óptimos", "descripcion": "Buena recaudación pero gasto muy bajo.", "status": "Ahorradora", "icono": "💰"},
    3: {"titulo": "Déficit / Riesgo", "descripcion": "Gastos superan peligrosamente a los ingresos.", "status": "Riesgosa", "icono": "🚨"},
    4: {"titulo": "Ejecución Sólida", "descripcion": "Gestión robusta con indicadores saludables.", "status": "Sólida", "icono": "🛡️"}
}

def load_models():
    """Carga los modelos PKL desde la carpeta model/"""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_path, 'model')
    
    try:
        kmeans = joblib.load(os.path.join(model_path, "kmeans.pkl"))
        scaler = joblib.load(os.path.join(model_path, "scaler.pkl"))
        return kmeans, scaler, True
    except Exception:
        return None, None, False

def predict_cluster(kmeans, scaler, model_loaded, data):
    """
    Recibe data = [ingresos, gastos, ratio_gi, ratio_saldo]
    Retorna (cluster_id, diccionario_perfil)
    """
    ingresos, gastos, ratio_gi, ratio_saldo = data
    
    if model_loaded:
        X_new = np.array([[ingresos, gastos, ratio_gi, ratio_saldo]])
        X_scaled = scaler.transform(X_new)
        cluster = kmeans.predict(X_scaled)[0]
    else:
        if ratio_gi > 1.1: cluster = 3
        elif ingresos > 0.9: cluster = 0
        else: cluster = 1
            
    return cluster, PERFILES.get(cluster, PERFILES[1])