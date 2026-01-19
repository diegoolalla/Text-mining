#!/usr/bin/env python3
"""
Script de verificación para el proyecto ProfNER
Valida que todos los archivos necesarios estén presentes
"""

import os
import json
import sys

def check_file_exists(filename):
    """Verifica si un archivo existe"""
    exists = os.path.exists(filename)
    status = "✓" if exists else "✗"
    print(f"{status} {filename}")
    return exists

def validate_notebook(notebook_path):
    """Valida la estructura del notebook"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Verificar estructura básica
        assert 'cells' in nb, "Notebook no tiene celdas"
        assert 'metadata' in nb, "Notebook no tiene metadata"
        
        # Contar celdas
        code_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'code')
        markdown_cells = sum(1 for cell in nb['cells'] if cell['cell_type'] == 'markdown')
        
        print(f"\nEstructura del notebook:")
        print(f"  - Total de celdas: {len(nb['cells'])}")
        print(f"  - Celdas de código: {code_cells}")
        print(f"  - Celdas de markdown: {markdown_cells}")
        
        # Verificar secciones clave
        sections = [
            "Análisis Exploratorio",
            "Selección y Justificación del Modelo",
            "Entrenamiento",
            "Evaluación",
            "Predicciones"
        ]
        
        notebook_text = json.dumps(nb).lower()
        print(f"\nSecciones encontradas:")
        for section in sections:
            found = section.lower() in notebook_text
            status = "✓" if found else "✗"
            print(f"  {status} {section}")
        
        return True
    except Exception as e:
        print(f"✗ Error al validar notebook: {e}")
        return False

def main():
    print("="*60)
    print("VERIFICACIÓN DEL PROYECTO PROFNER")
    print("="*60)
    
    print("\n1. Verificando archivos requeridos:")
    required_files = [
        "profner_classifier.ipynb",
        "create_deliverable.py",
        "requirements.txt",
        "README.md",
        ".gitignore"
    ]
    
    all_present = all(check_file_exists(f) for f in required_files)
    
    print("\n2. Verificando estructura del notebook:")
    notebook_valid = validate_notebook("profner_classifier.ipynb")
    
    print("\n3. Archivos opcionales (generados al ejecutar el notebook):")
    optional_files = [
        "predictions.tsv",
        "eda_visualizations.png",
        "wordcloud_comparison.png",
        "confusion_matrix.png",
        "prediction_analysis.png"
    ]
    
    for f in optional_files:
        check_file_exists(f)
    
    print("\n" + "="*60)
    if all_present and notebook_valid:
        print("✓ VERIFICACIÓN COMPLETADA - TODOS LOS ARCHIVOS PRESENTES")
        print("\nPara ejecutar el proyecto:")
        print("1. pip install -r requirements.txt")
        print("2. jupyter notebook profner_classifier.ipynb")
        print("3. Ejecutar todas las celdas del notebook")
        print("4. python create_deliverable.py (para crear el ZIP)")
    else:
        print("✗ VERIFICACIÓN FALLIDA - REVISAR ARCHIVOS FALTANTES")
        sys.exit(1)
    print("="*60)

if __name__ == "__main__":
    main()
