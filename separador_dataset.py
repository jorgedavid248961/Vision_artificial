import os
import random
import shutil

# Directorio principal que contiene las carpetas "imagenes" y "etiquetas"
directorio_principal = r'C:\Users\Jorge A David\Desktop\data botellas\dataset'

# Directorio donde se crearn las carpetas TRAIN, VALID y TEST
directorio_destino = r'C:\Users\Jorge A David\Desktop\data botellas\BASE_DE_DATOS'

# Porcentaje de datos para cada conjunto
porcentaje_train = 0.7
porcentaje_valid = 0.15
porcentaje_test = 0.15

# Obtener la lista de nombres de archivos en la carpeta "imagenes"
imagenes_dir = os.path.join(directorio_principal, 'imagenes')
nombres_imagenes = os.listdir(imagenes_dir)

# Barajar la lista de nombres de archivos
random.shuffle(nombres_imagenes)

# Calcular el tamao de cada conjunto
total_datos = len(nombres_imagenes)
num_train = int(total_datos * porcentaje_train)
num_valid = int(total_datos * porcentaje_valid)

# Dividir los datos en conjuntos de entrenamiento, validacin y prueba
train_nombres = nombres_imagenes[:num_train]
valid_nombres = nombres_imagenes[num_train:num_train + num_valid]
test_nombres = nombres_imagenes[num_train + num_valid:]

# Crear las carpetas TRAIN, VALID y TEST en el directorio de destino
for conjunto in ['TRAIN', 'VALID', 'TEST']:
    conjunto_dir = os.path.join(directorio_destino, conjunto)
    os.makedirs(conjunto_dir, exist_ok=True)
    # Crear las carpetas "imagenes" y "etiquetas" dentro de cada conjunto
    os.makedirs(os.path.join(conjunto_dir, 'imagenes'), exist_ok=True)
    os.makedirs(os.path.join(conjunto_dir, 'etiquetas'), exist_ok=True)

# Mover los archivos de imgenes y etiquetas a los conjuntos respectivos
for nombre_imagen in train_nombres:
    shutil.copy(os.path.join(imagenes_dir, nombre_imagen), os.path.join(directorio_destino, 'TRAIN', 'imagenes'))
    shutil.copy(os.path.join(directorio_principal, 'etiquetas', nombre_imagen.replace('.jpg', '.txt')), os.path.join(directorio_destino, 'TRAIN', 'etiquetas'))

for nombre_imagen in valid_nombres:
    shutil.copy(os.path.join(imagenes_dir, nombre_imagen), os.path.join(directorio_destino, 'VALID', 'imagenes'))
    shutil.copy(os.path.join(directorio_principal, 'etiquetas', nombre_imagen.replace('.jpg', '.txt')), os.path.join(directorio_destino, 'VALID', 'etiquetas'))

for nombre_imagen in test_nombres:
    shutil.copy(os.path.join(imagenes_dir, nombre_imagen), os.path.join(directorio_destino, 'TEST', 'imagenes'))
    shutil.copy(os.path.join(directorio_principal, 'etiquetas', nombre_imagen.replace('.jpg', '.txt')), os.path.join(directorio_destino, 'TEST', 'etiquetas'))