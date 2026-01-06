import os
import joblib
import numpy as np
import pytest

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'model')

def test_model_files_exist():
    """Verifica que los archivos del modelo existan después del entrenamiento"""
    assert os.path.exists(os.path.join(MODEL_DIR, 'kmeans.pkl')), "Falta kmeans.pkl"
    assert os.path.exists(os.path.join(MODEL_DIR, 'scaler.pkl')), "Falta scaler.pkl"

def test_model_loading_and_prediction():
    """Verifica que el modelo cargue y prediga correctamente"""
    try:
        kmeans = joblib.load(os.path.join(MODEL_DIR, 'kmeans.pkl'))
        scaler = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
    except Exception as e:
        pytest.fail(f"No se pudieron cargar los modelos: {e}")

    # Datos de prueba simulados (un caso perfecto: todo al 100%)
    # [ingresos, gastos, ratio_gi, ratio_saldo]
    test_data = np.array([[1.0, 1.0, 1.0, 0.0]])
    
    try:
        X_scaled = scaler.transform(test_data)
        prediction = kmeans.predict(X_scaled)
        
        # Verificar que la predicción es un entero (cluster ID)
        assert isinstance(prediction[0], (int, np.integer)), "La predicción no es un entero"
        # Verificar que el cluster está en un rango razonable (0 a 4)
        assert 0 <= prediction[0] <= 5, "El cluster predicho está fuera de rango"
        
    except Exception as e:
        pytest.fail(f"Fallo al realizar una predicción de prueba: {e}")