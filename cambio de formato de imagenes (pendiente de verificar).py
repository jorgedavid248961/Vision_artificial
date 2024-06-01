import os

# Carpeta de entrada (contiene imágenes con extensión .jpeg)
carpeta_entrada = r"c:\Users\Jorge A David\Desktop\data botellas\imagenes de internet"

# Itera sobre los archivos en la carpeta de entrada
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith('.jpeg'):
        # Genera el nuevo nombre de archivo cambiando la extensión a .jpg
        nuevo_nombre = os.path.splitext(archivo)[0] + '.jpg'
        
        # Renombra el archivo
        os.rename(os.path.join(carpeta_entrada, archivo), os.path.join(carpeta_entrada, nuevo_nombre))

print('Cambio de extensión completo.')






