import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Cargar modelo e información
with open('best_water_potability_model.pkl', 'rb') as file:
    modelo = pickle.load(file)

with open('model_info.pkl', 'rb') as file:
    model_info = pickle.load(file)

# Cargar datos de entrenamiento para obtener parámetros de normalización
df_original = pd.read_csv('water_potability_cleaned.csv')
X_original = df_original.drop('Potability', axis=1)

# Crear y ajustar el scaler con los datos de entrenamiento
scaler = StandardScaler()
scaler.fit(X_original)

# Obtener nombres de características
feature_names = model_info['feature_names']

# INTERFAZ GRÁFICA
st.title('🚰 Predicción de Potabilidad del Agua')
st.write('Ingrese los parámetros fisicoquímicos del agua para determinar si es potable')

st.header('Parámetros del Agua')

# Captura de datos con rangos típicos y valores seguros por defecto
ph = st.slider('pH (acidez/alcalinidad)', min_value=0.0, max_value=14.0, value=7.2, step=0.1)
hardness = st.number_input('Hardness (Dureza) [mg/L]', min_value=0.0, max_value=500.0, value=200.0, step=10.0)
solids = st.number_input('Solids (Sólidos disueltos) [ppm]', min_value=0.0, max_value=50000.0, value=15000.0, step=100.0)
chloramines = st.slider('Chloramines (Cloraminas) [ppm]', min_value=0.0, max_value=10.0, value=3.5, step=0.1)
sulfate = st.number_input('Sulfate (Sulfato) [mg/L]', min_value=0.0, max_value=500.0, value=250.0, step=10.0)
conductivity = st.number_input('Conductivity (Conductividad) [µS/cm]', min_value=0.0, max_value=1000.0, value=350.0, step=10.0)
organic_carbon = st.slider('Organic Carbon (Carbono orgánico) [ppm]', min_value=0.0, max_value=50.0, value=12.0, step=0.5)
trihalomethanes = st.slider('Trihalomethanes (Trihalometanos) [µg/L]', min_value=0.0, max_value=200.0, value=50.0, step=5.0)
turbidity = st.slider('Turbidity (Turbidez) [NTU]', min_value=0.0, max_value=10.0, value=3.5, step=0.1)

# Crear dataframe con los datos capturados
datos = [[
    ph, hardness, solids, chloramines, sulfate, 
    conductivity, organic_carbon, trihalomethanes, turbidity
]]

data = pd.DataFrame(datos, columns=feature_names)
st.write('### Datos capturados:')
st.dataframe(data)

# PREPARACIÓN DE DATOS
# Normalizar datos usando los parámetros del entrenamiento
data_preparada = pd.DataFrame(
    scaler.transform(data),
    columns=feature_names
)

st.write('### Datos normalizados (con parámetros del entrenamiento):')
st.dataframe(data_preparada)

# PREDICCIÓN
if st.button('🔍 Predecir Potabilidad', type='primary'):
    
    # Realizar predicción
    prediccion = modelo.predict(data_preparada)[0]
    probabilidad = modelo.predict_proba(data_preparada)[0]
    
    st.write('---')
    st.header('📊 Resultado de la Predicción')
    
    # Mostrar resultado
    if prediccion == 1:
        st.success('✅ AGUA POTABLE')
        st.write(f'El agua **ES POTABLE** según el modelo {model_info["nombre"]}')
    else:
        st.error('❌ AGUA NO POTABLE')
        st.write(f'El agua **NO ES POTABLE** según el modelo {model_info["nombre"]}')
    
    # Mostrar probabilidades
    st.write('### Probabilidades:')
    col1, col2 = st.columns(2)
    with col1:
        st.metric('No Potable', f'{probabilidad[0]:.2%}')
    with col2:
        st.metric('Potable', f'{probabilidad[1]:.2%}')
    
    # Mostrar métricas del modelo
    st.write('### Métricas del Modelo:')
    metricas = model_info['metricas']
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Accuracy', f"{metricas['accuracy']:.3f}")
        st.metric('Precision', f"{metricas['precision']:.3f}")
    with col2:
        st.metric('Recall', f"{metricas['recall']:.3f}")
        st.metric('F1-Score', f"{metricas['f1_score']:.3f}")
    with col3:
        st.metric('ROC-AUC', f"{metricas['roc_auc']:.3f}")
    
    # Mostrar hiperparámetros
    with st.expander('⚙️ Ver Hiperparámetros del Modelo'):
        st.json(model_info['hiperparametros'])
    
    # Advertencia
    st.warning('⚠️ Esta predicción es solo una estimación basada en Machine Learning. '
               'Para consumo humano, siempre realice análisis de laboratorio certificados.')

# INFORMACIÓN ADICIONAL
st.write('---')
st.write('### 📋 Rangos de Referencia (WHO/EPA):')

referencias = pd.DataFrame({
    'Parámetro': ['pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                  'Conductivity', 'Organic Carbon', 'Trihalomethanes', 'Turbidity'],
    'Rango Seguro': [
        '6.5 - 8.5',
        '0 - 500 mg/L',
        '0 - 1000 ppm',
        '0 - 4 ppm',
        '0 - 500 mg/L',
        '0 - 400 µS/cm',
        '0 - 4 ppm',
        '0 - 80 µg/L',
        '0 - 5 NTU'
    ]
})

st.dataframe(referencias, use_container_width=True)
