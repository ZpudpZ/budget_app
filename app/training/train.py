import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data')
MODEL_PATH = os.path.join(BASE_DIR, 'model')

def get_data():
    try:
        # Aquí iría la lógica real de unión de tus CSVs.
        # Por ahora, simularemos la estructura necesaria basándonos en el PDF
        # Si tienes tus CSV reales listos, aquí haríamos pd.read_csv(...)
        print("Generando dataset de entrenamiento...")
        
        # Simulamos 1000 registros con los 4 indicadores del PDF
        np.random.seed(42)
        data = {
            'ingresos': np.random.uniform(0.8, 1.1, 1000),     # Ejecución Ingresos
            'gastos': np.random.uniform(0.6, 1.0, 1000),       # Ejecución Gastos
            'ratio_gi': np.random.uniform(0.5, 1.2, 1000),     # Ratio Gasto/Ingreso
            'ratio_saldo': np.random.uniform(0.0, 1.0, 1000)   # Ratio Saldo
        }
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error generando datos: {e}")
        return pd.DataFrame()

def train():
    print(" Iniciando proceso de re-entrenamiento...")
    
    # 1. Obtener datos
    df = get_data()
    
    if df.empty:
        print(" Error: No hay datos para entrenar.")
        return

    # 2. Preprocesamiento
    X = df[['ingresos', 'gastos', 'ratio_gi', 'ratio_saldo']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 3. Entrenamiento (KMeans con 5 clusters como en el PDF)
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    
    # 4. Guardar Modelos
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
        
    joblib.dump(kmeans, os.path.join(MODEL_PATH, 'kmeans.pkl'))
    joblib.dump(scaler, os.path.join(MODEL_PATH, 'scaler.pkl'))
    
    print(f" ÉXITO: Modelos guardados en {MODEL_PATH}")

if __name__ == "__main__":
    train()