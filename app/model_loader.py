import joblib
import numpy as np
import os

# Definición de Perfiles
PERFILES = {
    0: {
        "titulo": "Alta Eficiencia en Ingresos",
        "descripcion": "Excelente recaudación con gasto controlado. Gestión fiscal óptima.",
        "status": "Eficiente",
        "icono": "✅"
    },
    1: {
        "titulo": "Gestión Equilibrada",
        "descripcion": "Balance adecuado entre ingresos y gastos elevados. Monitoreo recomendado.",
        "status": "Equilibrada",
        "icono": "⚖️"
    },
    2: {
        "titulo": "Ingresos Óptimos",
        "descripcion": "Excelente ejecución de ingresos con gasto crítico bajo. Situación favorable.",
        "status": "Óptima",
        "icono": "⭐"
    },
    3: {
        "titulo": "Gestión Ineficiente",
        "descripcion": "Desbalance en la ejecución del gasto. Requiere atención inmediata.",
        "status": "Riesgosa",
        "icono": "⚠️"
    },
    4: {
        "titulo": "Ejecución Sólida y Balanceada",
        "descripcion": "Gestión presupuestal robusta con indicadores saludables.",
        "status": "Sólida",
        "icono": "🛡️"
    }
}

def load_models():
    """Intenta cargar los modelos .pkl, retorna None si fallan."""
    # Ajustamos la ruta para que busque subiendo un nivel desde 'app' hacia 'model'
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_path, 'model')
    
    try:
        kmeans = joblib.load(os.path.join(model_path, "kmeans.pkl"))
        scaler = joblib.load(os.path.join(model_path, "scaler.pkl"))
        return kmeans, scaler, True
    except Exception as e:
        print(f"Error cargando modelos: {e}")
        return None, None, False

def predict_cluster(kmeans, scaler, model_loaded, data):
    """
    Realiza la predicción. Si no hay modelo, usa la lógica manual del PDF.
    data: [ingresos, gastos, ratio_gi, ratio_saldo]
    """
    ingresos, gastos, ratio_gi, ratio_saldo = data
    
    if model_loaded and kmeans and scaler:
        # Predicción con IA
        X_new = np.array([[ingresos, gastos, ratio_gi, ratio_saldo]])
        X_scaled = scaler.transform(X_new)
        cluster = kmeans.predict(X_scaled)[0]
    else:
        # Lógica de simulación manual
        if ingresos > 0.95 and gastos < 0.3:
            cluster = 0
        elif gastos > 0.85 and ingresos > 0.8:
            cluster = 1
        elif ingresos > 0.95 and gastos < 0.6:
            cluster = 2
        elif ratio_gi > 1.0 or gastos > ingresos * 1.1:
            cluster = 3
        else:
            cluster = 4
            
    return cluster, PERFILES[cluster]