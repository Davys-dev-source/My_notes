# ===============================================
# Programa: Escritura y lectura de un archivo de texto
# Autor: Davys Gaona
# Asignatura: Fundamentos de programación
# Descripción: Este programa crea un archivo de texto,
# escribe notas personales, las lee y muestra su contenido.
# ===============================================

# --- Escritura de Archivo de Texto ---
# Creamos un archivo llamado "my_notes.txt" en modo escritura ('w')
# Si el archivo no existe, Python lo creará automáticamente.
file = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales en el archivo
file.write("Primera nota: Hoy aprendí a crear y leer archivos en Python.\n")
file.write("Segunda nota: Es importante cerrar los archivos después de usarlos.\n")
file.write("Tercera nota: El manejo de archivos permite guardar información de forma permanente.\n")

# Cerramos el archivo después de escribir para liberar recursos
file.close()

# --- Lectura de Archivo de Texto ---
# Abrimos nuevamente el archivo, esta vez en modo lectura ('r')
file = open("my_notes.txt", "r")

# Leemos y mostramos cada línea del archivo
print("Contenido del archivo my_notes.txt:\n")
line = file.readline()  # Leemos la primera línea

# Usamos un bucle while para leer todas las líneas
while line:
    print(line.strip())  # Mostramos la línea sin saltos de línea adicionales
    line = file.readline()  # Leemos la siguiente línea

# --- Cierre de Archivos ---
# Cerramos el archivo al finalizar la lectura
file.close()

print("\nEl archivo ha sido leído y cerrado correctamente.")
