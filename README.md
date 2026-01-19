# text-mining
Tarea text mining

## Clasificador Binario ProfNER - COVID-19

Este proyecto implementa un clasificador binario para reconocer tweets que mencionan profesiones durante la pandemia de COVID-19, utilizando datos del corpus ProfNER.

### Descripción del Proyecto

El proyecto incluye:
- 📊 Análisis exploratorio de datos (EDA) con estadísticas y visualizaciones
- 🤖 Clasificador binario usando modelo BETO de HuggingFace
- 📈 Entrenamiento y evaluación del modelo
- 🎯 Predicciones en conjunto de test
- 📄 Resultados exportados en formato TSV

### Modelo Seleccionado

**BETO (dccuchile/bert-base-spanish-wwm-cased)** - BERT base entrenado en español con Whole Word Masking

**Justificación:**
- Especializado en textos en español
- Arquitectura Transformer con atención bidireccional
- Pre-entrenado en corpus grande incluyendo redes sociales
- Rendimiento comprobado en tareas de NLP en español
- Balance óptimo entre capacidad y eficiencia (~110M parámetros)

### Archivos del Proyecto

- `profner_classifier.ipynb` - Notebook Jupyter ejecutable con todo el pipeline
- `predictions.tsv` - Archivo con predicciones del conjunto de test
- `create_deliverable.py` - Script para generar el archivo ZIP entregable

### Estructura del Notebook

1. **Instalación de Dependencias** - Setup del entorno
2. **Importación de Librerías** - Carga de paquetes necesarios
3. **Carga de Datos** - Dataset ProfNER
4. **Análisis Exploratorio** - Estadísticas y visualizaciones
5. **Selección de Modelo** - Justificación de BETO
6. **Preparación de Datos** - Tokenización y procesamiento
7. **Entrenamiento** - Fine-tuning del modelo
8. **Evaluación** - Métricas en validación
9. **Predicciones** - Generación de resultados en test
10. **Exportación** - Guardar resultados en TSV
11. **Análisis de Resultados** - Visualizaciones finales
12. **Resumen** - Conclusiones del proyecto

### Requisitos

```bash
pip install transformers datasets torch scikit-learn pandas numpy matplotlib seaborn wordcloud
```

### Uso

#### Ejecutar el Notebook

```bash
jupyter notebook profner_classifier.ipynb
```

O ejecutar todas las celdas desde la línea de comandos:

```bash
jupyter nbconvert --to notebook --execute profner_classifier.ipynb
```

#### Crear el Entregable ZIP

```bash
python create_deliverable.py
```

Esto genera: `profner_binary_classifier_deliverable.zip` conteniendo:
- `profner_classifier.ipynb`
- `predictions.tsv`

### Formato del Archivo de Predicciones

El archivo `predictions.tsv` contiene las siguientes columnas separadas por tabuladores:

| Columna | Descripción |
|---------|-------------|
| text | Texto del tweet |
| true_label | Etiqueta real (0: Sin profesión, 1: Con profesión) |
| predicted_label | Etiqueta predicha por el modelo |
| probability_class_0 | Probabilidad de clase 0 (Sin profesión) |
| probability_class_1 | Probabilidad de clase 1 (Con profesión) |

### Visualizaciones Generadas

El notebook genera las siguientes visualizaciones:

- `eda_visualizations.png` - Análisis exploratorio (distribución de clases, longitud de texto, etc.)
- `wordcloud_comparison.png` - Nubes de palabras comparativas
- `confusion_matrix.png` - Matriz de confusión del modelo
- `prediction_analysis.png` - Análisis de las predicciones

### Métricas de Evaluación

El modelo se evalúa usando:
- **Accuracy** - Precisión general
- **Precision** - Precisión por clase
- **Recall** - Exhaustividad
- **F1-Score** - Media armónica de precisión y recall

### Resultados

Los resultados detallados se encuentran en el notebook ejecutado, incluyendo:
- Métricas en conjunto de validación
- Matriz de confusión
- Reporte de clasificación completo
- Distribución de probabilidades de predicción

### Autor

Proyecto desarrollado para la tarea de Text Mining

### Licencia

Este proyecto es de uso académico.
