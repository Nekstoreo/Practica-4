# Analítica de Datos - 2025

## PRÁCTICA DE CALIDAD Y MINERÍA DE DATOS EN PYTHON (15%)

**Equipos de los proyectos**

Con los datos seleccionados en las prácticas anteriores, desarrollar los siguientes puntos.

---

## 1. CALIDAD DE DATOS (1.0)

### A. Perfilado de Datos
Genere el perfilado de datos en Python sobre los datos originales, adjunte el resultado en HTML.

**Resultado:** `water_potability_profiling_report.html`

### B. Diagnóstico de Calidad de Datos
Realice un diagnóstico de cada una de las dimensiones de la calidad de datos, teniendo en cuenta los resultados del perfilado. El diagnóstico debe estar en el notebook.

**Notebook de Referencia:** `calidad de datos.ipynb`

### C. Limpieza y Mejora de Datos
Implemente todos los pasos de limpieza y mejora de los datos en Python.

**Archivos Generados:**
- `water_potability_cleaned.csv` - Datos limpios
- `water_potability_scaled.csv` - Datos normalizados/escalados

---

## 2. MINERÍA DE DATOS EN PYTHON (3.0)

### A. Modelos Predictivos (1.0)
Crear un modelo predictivo en Python. En el notebook explicar:
- Objetivo del modelo
- Configuración de técnicas
- Evaluación de los modelos (árbol, KNN, red neuronal, SVM y random forest)
- Conclusiones sobre la calidad de los modelos

**Notebook de Referencia:** `mineria de datos.ipynb`

**Modelos Evaluados:**
1. Árbol de Decisión (Decision Tree)
2. K-Vecinos Más Cercanos (KNN)
3. Red Neuronal (MLPClassifier)
4. Máquina de Vectores de Soporte (SVM)
5. Bosque Aleatorio (Random Forest)

**Visualizaciones Generadas:**
- Comparación de métricas por modelo
- Matrices de confusión
- Curvas ROC

### B. Hiperparametrización con GridSearch (1.0)
El mejor modelo debe ser hiperparametrizado con GridSearch.

**Mejoras Realizadas:**
- Optimización de hiperparámetros del mejor modelo
- Comparación antes vs después de la optimización
- Importancia de características

**Archivos Generados:**
- `best_water_potability_model.pkl` - Modelo optimizado
- `model_info.pkl` - Información y metadatos del modelo

### C. Despliegue del Modelo con Interfaz Gráfica (1.0)
Realizar el despliegue del modelo predictivo con interfaz gráfica.

**Notebook de Referencia:** `despliegue.ipynb`

**Captura de Pantalla del Despliegue:**

![Interfaz de Despliegue](./deployment_screenshot.png)

---

## 3. COMUNICACIÓN DEL PROYECTO (1.0)

### A. Repositorio GitHub
Entregar el proyecto en GitHub. Adicionalmente adjuntar a la tarea de Teams los notebooks y otra información solicitada.

**Enlace del Repositorio:** [GitHub Repository URL]

### B. Resumen del Proyecto
Completar el resumen del proyecto en el enlace compartido en Teams - todas las secciones de Minería de Datos y Calidad de Datos.

---

## Entregables

- ✅ Jupyter notebook de calidad de datos (`calidad de datos.ipynb`)
- ✅ Jupyter notebook de aprendizaje del modelo predictivo (`mineria de datos.ipynb`)
- ✅ Jupyter notebook de despliegue con interfaz gráfica (`despliegue.ipynb`)
- ✅ Enlace a GitHub
- ⏳ Resumen del proyecto en el archivo compartido en Teams

---

## Estructura del Proyecto

```
Practica 4/
├── app.py                                    # Aplicación de despliegue
├── calidad de datos.ipynb                    # Notebook de calidad de datos
├── despliegue.ipynb                          # Notebook de despliegue
├── mineria de datos.ipynb                    # Notebook de minería de datos
├── requirements.txt                          # Dependencias del proyecto
├── PRACTICA_CALIDAD_MINERIA_DATOS.md        # Documentación de la práctica
├── .gitignore                                # Archivos a ignorar en Git
│
├── water_potability.csv                      # Datos originales
├── water_potability_cleaned.csv              # Datos limpios
├── water_potability_scaled.csv               # Datos escalados
├── water_potability_profiling_report.html    # Reporte de perfilado
│
├── best_water_potability_model.pkl           # Modelo optimizado guardado
├── model_info.pkl                            # Información del modelo
│
└── [Visualizaciones generadas]
    ├── neural_network_loss.png
    ├── comparacion_modelos.png
    ├── matrices_confusion.png
    ├── curvas_roc.png
    ├── modelo_optimizado.png
    ├── feature_importance.png
    └── deployment_screenshot.png
```

---

**Fecha de Elaboración:** 2025
