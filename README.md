# FileOrganizer
La clase FileOrganizer **permite organizar archivos en una carpeta según su tipo**.

## Instalación
No es necesario instalar nada para utilizar esta clase, ya que se basa en la biblioteca estándar de Python.

## Uso
Creación de una instancia

```python

from file_organizer import FileOrganizer

file_organizer = FileOrganizer()

```

## Configuración de la ruta de origen
Puedes configurar la ruta de origen utilizando el método `set_dir_path()`:

```python
file_organizer.set_dir_path('/ruta/a/tu/directorio')

```

Por defecto, la ruta de origen es la ruta actual en la que se encuentra el archivo Python que contiene la clase `FileOrganizer`.

Organización de archivos
Para organizar los archivos en una carpeta según su tipo, llama al método `organize()`:

```python
file_organizer.organize()
```

Este método crea una carpeta para cada tipo de archivo en la carpeta de origen y mueve los archivos correspondientes a la carpeta correspondiente.

## Tipos de archivo
Por defecto, FileOrganizer organiza los siguientes tipos de archivo:

- Documentos: .pdf, .doc, .docx, .txt
- Imágenes: .jpg, .jpeg, .png, .gif
- Música: .mp3, .wav
- Videos: .mp4, .avi, .mov


Puedes modificar o añadir tipos de archivo utilizando el diccionario `file_types`:

```python

file_organizer.file_types = {
    'Archivos de texto': ['.txt', '.md'],
    'Archivos de datos': ['.csv', '.json', '.xml'],
    'Archivos de código': ['.py', '.html', '.css', '.js']
}


```

## Ejemplo completo
```python


from file_organizer import FileOrganizer

# crea una instancia de FileOrganizer
file_organizer = FileOrganizer()

# organiza los archivos en la ruta actual
file_organizer.organize()


```

## Agregar al PATH
Aquí te resumo los pasos para que puedas ejecutar el archivo `TheOrganizer.py` desde cualquier ubicación de manera fácil:

1. Abre una **terminal o línea de comandos.**

2. Ejecuta el siguiente comando en la terminal para verificar la ubicación del archivo FileOrganizer.py:

```bash
pwd

```
Este comando te dará la **ruta actual en la que te encuentras**. Asegúrate de que estás en la ruta correcta donde se encuentra el archivo `FileOrganizer.py`.

3. Ahora, copia la ruta del directorio que contiene el archivo `FileOrganizer.py`.

4. Agrega la ruta al `PATH` del sistema operativo ejecutando el siguiente comando en la terminal:

### En Windows:
```bash
setx path "%path%;ruta_al_directorio"


```

### En Linux/MacOS:
```bash
export PATH=$PATH:ruta_al_directorio

```
Asegúrate de reemplazar `ruta_al_directorio` con la ruta que copiaste anteriormente.

5. Ahora puedes ejecutar el algoritmo desde cualquier ruta escribiendo el siguiente comando en la terminal:

```bash
python FileOrganizer.py

```
Asegúrate de reemplazar `ruta_personalizada` con la ruta que deseas usar.



