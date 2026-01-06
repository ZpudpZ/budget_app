# 🏛️ Budget Intelligence Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![MLOps](https://img.shields.io/badge/MLOps-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)]()

> **Sistema Inteligente de Auditoría y Análisis Presupuestal basado en Machine Learning para el Sector Público Peruano**

---

## 📌 Descripción del Proyecto

**Budget Intelligence** es una solución tecnológica orientada al análisis y diagnóstico de la ejecución presupuestal en entidades del sector público del Perú. El sistema emplea **Aprendizaje Automático No Supervisado (K-Means)** para identificar patrones históricos de ingresos y gastos provenientes del **SIAF**, permitiendo evaluar la salud fiscal de una entidad en tiempo casi real.

El proyecto adopta una arquitectura **MLOps completa**, integrando automatización del entrenamiento, validación y despliegue del modelo ante la incorporación de nuevos datos, garantizando decisiones basadas en información actualizada y reproducible.

---

## 🎯 Objetivos

- Analizar patrones de ejecución presupuestal mediante clustering.
- Clasificar la gestión fiscal de entidades públicas en distintos perfiles.
- Automatizar el ciclo de vida del modelo de Machine Learning.
- Proporcionar una interfaz visual interactiva para análisis y simulación.
- Facilitar la trazabilidad y generación de reportes técnicos de auditoría.

---

## 🚀 Características Principales

- **🧠 Diagnóstico Inteligente:** Clasificación automática en 5 clusters fiscales:
  - Eficiente  
  - Equilibrada  
  - Ahorradora  
  - Riesgosa  
  - Sólida  

- **📊 Dashboard Interactivo:** Visualización dinámica de métricas, simulación de escenarios y feedback inmediato.
- **🔄 Pipeline MLOps (CI/CD):** Automatización del ciclo de vida del ML usando GitHub Actions.
- **📑 Reportes de Auditoría:** Exportación de informes técnicos con historial de sesiones.
- **☁️ Cloud Ready:** Aplicación preparada para despliegue en la nube.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Descripción |
|-----------|-----------|-------------|
| Lenguaje | Python 3.9+ | Lógica del sistema y modelado |
| Frontend | Streamlit | Interfaz web interactiva |
| ML Core | Scikit-Learn | Algoritmo K-Means y preprocesamiento |
| Data | Pandas / NumPy | Manipulación de datos presupuestales |
| CI/CD | GitHub Actions | Automatización de pruebas y entrenamiento |
| Testing | Pytest | Validación de datos y calidad del modelo |

---

## 📂 Estructura del Proyecto

```text
BUDGET_APP/
├── .github/workflows/        # ⚙️ Configuración del Pipeline CI/CD
├── app/
│   ├── main.py               # 🏠 Punto de entrada de la aplicación
│   ├── model_loader.py       # 🔌 Carga e inferencia del modelo
│   ├── styles.py             # 🎨 Estilos CSS personalizados
│   └── views/
│       ├── analisis.py       # 📊 Diagnóstico y simulación
│       ├── reportes.py       # 📑 Generación de reportes
│       └── configuracion.py  # ⚙️ Visualización de datos y parámetros
├── data/                     # 💾 Datos históricos (SIAF)
├── model/                    # 🧠 Modelos entrenados (.pkl)
├── training/                 # 🏗️ Scripts de entrenamiento
├── tests/                    # 🧪 Pruebas unitarias
├── requirements.txt          # 📦 Dependencias
└── README.md                 # 📘 Documentación
```

## ⚙️ Instalación y Uso Local
Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/budget_app.git
cd budget_app
```

### 2️⃣ Crear entorno virtual
Se recomienda utilizar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

### Activar el entorno virtual:
Windows

```bash
.\venv\Scripts\activate
```

Mac / Linux
```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
Instala todas las librerías necesarias (Streamlit, Pandas, Scikit-learn, etc.).

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación
Inicia el servidor local de Streamlit.

```bash
streamlit run app/main.py
```
La aplicación estará disponible en el navegador en:

👉 http://localhost:8501

## 🔄 Arquitectura MLOps (CI/CD Pipeline)

El proyecto implementa una arquitectura MLOps que automatiza todo el ciclo de vida del modelo de Machine Learning.

### 🔔 Trigger (Disparador)

El pipeline se activa automáticamente cuando ocurre alguno de los siguientes eventos:

  - Cambios en el código fuente

  - Actualización o incorporación de nuevos datos en la carpeta data/

### 🧪 Quality Assurance (QA)

Ejecución automática de pruebas unitarias con pytest

Validación de:

 - Integridad de los archivos CSV
 - Correcto preprocesamiento de datos
 - Consistencia del código

### 🏗️ Continuous Training (CT)

 - Se ejecuta el script training/train.py, el cual realiza:
 - Carga de nuevos datos presupuestales
 - Limpieza y preprocesamiento
 - Re-entrenamiento del modelo K-Means
 - Persistencia de artefactos entrenados (.pkl) en la carpeta model/

### 🚀 Continuous Deployment (CD)

 - La aplicación web consume automáticamente el modelo actualizado
 - El usuario final siempre interactúa con la versión más reciente e inteligente del sistema