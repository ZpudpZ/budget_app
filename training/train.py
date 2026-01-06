import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data')
MODEL_PATH = os.path.join(BASE_DIR, 'model')

def load_and_process_data():
    print("[INFO] Cargando datos...")
    
    try:
        gastos_path = os.path.join(DATA_PATH, 'gastos.csv')
        ingresos_path = os.path.join(DATA_PATH, 'ingresos.csv')

        df_gastos = pd.read_csv(gastos_path, sep=';', encoding='latin-1', dtype=str)
        df_ingresos = pd.read_csv(ingresos_path, sep=';', encoding='latin-1', dtype=str)
        
    except Exception as e:
        print(f"[ERROR] Fallo al leer CSV: {e}")
        return pd.DataFrame()

    print(f"[INFO] Filas leidas - Gastos: {len(df_gastos)}, Ingresos: {len(df_ingresos)}")

    # Limpieza de nombres de columnas
    df_gastos.columns = df_gastos.columns.str.lower().str.strip()
    df_ingresos.columns = df_ingresos.columns.str.lower().str.strip()

    # Procesamiento de gastos
    print("[INFO] Procesando Gastos...")
    cols_gastos = ['pim', 'devengado', 'saldo', 'sec_ejec']
    
    # Verificar columnas existentes
    actual_cols_g = [c for c in cols_gastos if c in df_gastos.columns]
    df_g = df_gastos[actual_cols_g].copy()
    
    # Limpieza numérica
    for col in ['pim', 'devengado', 'saldo']:
        if col in df_g.columns:
            df_g[col] = df_g[col].str.replace(',', '', regex=False)
            df_g[col] = pd.to_numeric(df_g[col], errors='coerce').fillna(0)

    df_g_grouped = df_g.groupby('sec_ejec')[['pim', 'devengado', 'saldo']].sum().reset_index()
    
    # Ratios
    df_g_grouped['gastos'] = np.where(df_g_grouped['pim'] > 0, df_g_grouped['devengado'] / df_g_grouped['pim'], 0)
    df_g_grouped['ratio_saldo'] = np.where(df_g_grouped['devengado'] > 0, df_g_grouped['saldo'] / df_g_grouped['devengado'], 0)

    # Procesamiento de ingresos
    print("[INFO] Procesando Ingresos...")
    cols_ingresos = ['pim', 'total_prog', 'sec_ejec']
    
    actual_cols_i = [c for c in cols_ingresos if c in df_ingresos.columns]
    df_i = df_ingresos[actual_cols_i].copy()
    
    for col in ['pim', 'total_prog']:
        if col in df_i.columns:
            df_i[col] = df_i[col].str.replace(',', '', regex=False)
            df_i[col] = pd.to_numeric(df_i[col], errors='coerce').fillna(0)
        
    df_i_grouped = df_i.groupby('sec_ejec')[['pim', 'total_prog']].sum().reset_index()
    df_i_grouped.rename(columns={'pim': 'pim_ingresos', 'total_prog': 'recaudado'}, inplace=True)
    
    # Ratios
    df_i_grouped['ingresos'] = np.where(df_i_grouped['pim_ingresos'] > 0, df_i_grouped['recaudado'] / df_i_grouped['pim_ingresos'], 0)

    # Union (Merge)
    print("[INFO] Uniendo tablas por Unidad Ejecutora (sec_ejec)...")
    df_final = pd.merge(df_g_grouped, df_i_grouped, on='sec_ejec', how='inner')
    
    # Ratio Final
    df_final['ratio_gi'] = np.where(df_final['recaudado'] > 0, df_final['devengado'] / df_final['recaudado'], 0)

    features = ['ingresos', 'gastos', 'ratio_gi', 'ratio_saldo']
    dataset = df_final[features].fillna(0)
    
    print(f"[OK] Datos listos: {len(dataset)} registros encontrados.")
    return dataset

def train():
    print("--- INICIANDO ENTRENAMIENTO ---")
    df = load_and_process_data()
    
    # Validación mínima relajada (si hay 1 fila, la duplicamos para que k-means corra)
    if df.empty:
        print("[ERROR] No hay coincidencias entre Gastos e Ingresos (verifica los códigos sec_ejec).")
        return

    if len(df) < 5:
        print("[WARN] Pocos datos. Duplicando filas para fines academicos (clustering)...")
        df = pd.concat([df]*5, ignore_index=True)
        # Ruido mínimo para que no sean puntos idénticos
        noise = np.random.normal(0, 0.01, df.shape)
        df = df + noise

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    
    n_clusters = 5
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)
        
    joblib.dump(kmeans, os.path.join(MODEL_PATH, 'kmeans.pkl'))
    joblib.dump(scaler, os.path.join(MODEL_PATH, 'scaler.pkl'))
    
    print(f"[EXITO] Modelos guardados en: {MODEL_PATH}")

if __name__ == "__main__":
    train()