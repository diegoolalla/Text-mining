# Guía de Uso - Clasificador Binario ProfNER

## Descripción General

Este proyecto implementa un **clasificador binario** para identificar tweets que mencionan profesiones durante la pandemia de COVID-19, utilizando el corpus ProfNER y modelos de HuggingFace.

## 📋 Contenido del Proyecto

### Archivos Principales

1. **profner_classifier.ipynb** - Notebook Jupyter principal con todo el pipeline
2. **predictions.tsv** - Archivo de predicciones en formato TSV
3. **create_deliverable.py** - Script para crear el entregable ZIP
4. **verify_project.py** - Script de verificación del proyecto
5. **requirements.txt** - Dependencias del proyecto
6. **README.md** - Documentación principal

## 🚀 Instalación y Configuración

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/diegoolalla/text-mining.git
cd text-mining
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

#### Dependencias Principales:
- `transformers` - Modelos de HuggingFace
- `datasets` - Carga y manejo de datasets
- `torch` - PyTorch para deep learning
- `scikit-learn` - Métricas y evaluación
- `pandas` - Manipulación de datos
- `matplotlib` y `seaborn` - Visualizaciones
- `wordcloud` - Nubes de palabras

### Paso 3: Verificar la Instalación

```bash
python verify_project.py
```

## 📊 Ejecución del Proyecto

### Opción 1: Jupyter Notebook (Recomendado)

```bash
jupyter notebook profner_classifier.ipynb
```

Luego, ejecutar todas las celdas en orden:
- Menu → Run → Run All Cells
- O usar Shift+Enter en cada celda

### Opción 2: Ejecución por Línea de Comandos

```bash
jupyter nbconvert --to notebook --execute profner_classifier.ipynb --inplace
```

### Opción 3: Google Colab

1. Subir el notebook a Google Colab
2. Ejecutar la primera celda para instalar dependencias
3. Ejecutar todas las celdas secuencialmente

## 🎯 Flujo del Proyecto

### 1. Análisis Exploratorio de Datos (EDA)

El notebook realiza un análisis completo incluyendo:
- Estadísticas del dataset (tamaño, distribución de clases)
- Análisis de longitud de textos
- Visualizaciones de distribuciones
- Nubes de palabras comparativas

**Salidas generadas:**
- `eda_visualizations.png`
- `wordcloud_comparison.png`

### 2. Selección del Modelo

**Modelo: BETO (dccuchile/bert-base-spanish-wwm-cased)**

Justificación detallada:
- ✅ Especializado en español
- ✅ Arquitectura Transformer con atención bidireccional
- ✅ Pre-entrenado con Whole Word Masking
- ✅ ~110M parámetros (balance capacidad/eficiencia)
- ✅ Rendimiento comprobado en NLP español

### 3. Entrenamiento del Modelo

Configuración por defecto:
- **Épocas:** 3
- **Batch Size:** 8
- **Learning Rate:** 2e-5
- **Max Length:** 128 tokens

El entrenamiento incluye:
- Tokenización de textos
- Fine-tuning del modelo BETO
- Validación por época
- Selección del mejor modelo

### 4. Evaluación

Métricas calculadas:
- **Accuracy** - Precisión general
- **Precision** - Por clase
- **Recall** - Exhaustividad
- **F1-Score** - Media armónica

**Salidas generadas:**
- `confusion_matrix.png`
- Reporte de clasificación completo

### 5. Predicciones en Test

Genera predicciones con:
- Etiqueta predicha (0 o 1)
- Probabilidades por clase
- Comparación con etiquetas reales

**Salida:** `predictions.tsv`

### 6. Análisis de Resultados

Visualizaciones finales:
- Distribución de probabilidades
- Comparación predicciones vs reales

**Salida:** `prediction_analysis.png`

## 📁 Formato del Archivo de Predicciones

El archivo `predictions.tsv` contiene columnas separadas por tabuladores:

```
text	true_label	predicted_label	probability_class_0	probability_class_1
Los cardiólogos...	1	1	0.1234	0.8766
La vacunación...	0	0	0.9012	0.0988
```

### Columnas:
- **text**: Texto del tweet
- **true_label**: Etiqueta real (0: Sin profesión, 1: Con profesión)
- **predicted_label**: Etiqueta predicha
- **probability_class_0**: P(Sin profesión)
- **probability_class_1**: P(Con profesión)

## 📦 Crear el Entregable

### Generar archivo ZIP con los entregables:

```bash
python create_deliverable.py
```

Esto crea: `profner_binary_classifier_deliverable.zip`

**Contenido del ZIP:**
1. `profner_classifier.ipynb` - Notebook ejecutable
2. `predictions.tsv` - Archivo de predicciones

## 🔍 Verificación del Proyecto

Para verificar que todo está correcto:

```bash
python verify_project.py
```

Este script verifica:
- ✅ Presencia de archivos requeridos
- ✅ Estructura del notebook
- ✅ Archivos opcionales generados

## 📈 Resultados Esperados

### Estructura de Archivos Final:

```
text-mining/
├── profner_classifier.ipynb          # Notebook principal
├── predictions.tsv                    # Predicciones en TSV
├── create_deliverable.py              # Script para ZIP
├── verify_project.py                  # Verificación
├── requirements.txt                   # Dependencias
├── README.md                          # Documentación
├── USAGE.md                           # Esta guía
├── .gitignore                         # Archivos ignorados
├── eda_visualizations.png             # Generado
├── wordcloud_comparison.png           # Generado
├── confusion_matrix.png               # Generado
├── prediction_analysis.png            # Generado
└── profner_binary_classifier_deliverable.zip  # Entregable
```

## 🛠️ Troubleshooting

### Error: Módulo no encontrado

```bash
pip install -r requirements.txt --upgrade
```

### Error: CUDA no disponible

El código funciona en CPU automáticamente. Para usar GPU:
- Instalar PyTorch con soporte CUDA
- Verificar drivers NVIDIA

### Error: Memoria insuficiente

Reducir batch size en el notebook:
```python
BATCH_SIZE = 4  # o menor
```

### Notebook no se ejecuta completamente

Ejecutar celdas una por una para identificar errores específicos.

## 📊 Personalización

### Cambiar el Modelo

En el notebook, modificar:
```python
MODEL_NAME = "otro-modelo-español"
```

Opciones alternativas:
- `"PlanTL-GOB-ES/roberta-base-bne"`
- `"bertin-project/bertin-roberta-base-spanish"`
- `"mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"`

### Ajustar Hiperparámetros

```python
EPOCHS = 5              # Más épocas
BATCH_SIZE = 16         # Mayor batch
LEARNING_RATE = 3e-5    # Diferente LR
MAX_LENGTH = 256        # Secuencias más largas
```

## 📝 Notas Importantes

1. **Dataset**: El notebook incluye lógica para cargar el dataset ProfNER desde HuggingFace o crear uno sintético para demostración.

2. **Reproducibilidad**: Se establece semilla aleatoria (seed=42) para resultados reproducibles.

3. **Guardado de Modelo**: El notebook incluye opción para guardar el modelo entrenado en `./profner_model/`.

4. **Tiempo de Ejecución**: 
   - CPU: ~10-15 minutos
   - GPU: ~2-5 minutos

## 🔗 Referencias

- **ProfNER Dataset**: Corpus de tweets COVID-19 con anotaciones de profesiones
- **BETO**: BERT en español con Whole Word Masking
- **HuggingFace Transformers**: https://huggingface.co/transformers/

## 📧 Soporte

Para preguntas o problemas:
1. Revisar esta guía
2. Ejecutar `verify_project.py`
3. Verificar logs del notebook
4. Revisar issues en el repositorio

## ✅ Checklist de Entrega

- [ ] Ejecutar el notebook completo
- [ ] Verificar que se generó `predictions.tsv`
- [ ] Revisar las visualizaciones generadas
- [ ] Ejecutar `verify_project.py`
- [ ] Crear el ZIP con `create_deliverable.py`
- [ ] Verificar contenido del ZIP

---

**Proyecto de Text Mining - Clasificador Binario ProfNER**
**Última actualización:** Enero 2026
