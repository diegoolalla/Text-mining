#!/usr/bin/env python3
"""
Script para crear el entregable final del proyecto ProfNER
Genera el archivo .zip con el notebook y el archivo de predicciones
"""

import os
import zipfile
from datetime import datetime

def create_zip_deliverable():
    """
    Crea el archivo .zip con el formato requerido:
    - profner_classifier.ipynb (notebook ejecutable)
    - predictions.tsv (archivo de predicciones)
    """
    
    # Nombre del archivo zip
    zip_filename = "profner_binary_classifier_deliverable.zip"
    
    # Archivos a incluir
    files_to_include = [
        "profner_classifier.ipynb",
        "predictions.tsv"
    ]
    
    # Verificar que los archivos existen
    missing_files = []
    for file in files_to_include:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("⚠ Advertencia: Los siguientes archivos no existen aún:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nNota: Ejecuta el notebook 'profner_classifier.ipynb' primero para generar predictions.tsv")
        print("Creando zip solo con los archivos disponibles...")
        files_to_include = [f for f in files_to_include if f not in missing_files]
    
    # Crear el archivo ZIP
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in files_to_include:
            zipf.write(file, arcname=file)
            print(f"✓ Agregado: {file}")
    
    # Información del archivo creado
    zip_size = os.path.getsize(zip_filename)
    print(f"\n{'='*60}")
    print(f"ARCHIVO ZIP CREADO EXITOSAMENTE")
    print(f"{'='*60}")
    print(f"Nombre: {zip_filename}")
    print(f"Tamaño: {zip_size:,} bytes ({zip_size/1024:.2f} KB)")
    print(f"Archivos incluidos: {len(files_to_include)}")
    print(f"{'='*60}")
    
    return zip_filename

if __name__ == "__main__":
    create_zip_deliverable()
