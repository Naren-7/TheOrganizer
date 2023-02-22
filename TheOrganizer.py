import os
import shutil
import pandas as pd


class FileOrganizer:
    def __init__(self):
        self.types = {
            'Documentos': ('.doc', '.docx', '.pdf', '.txt'),
            'Imagenes': ('.jpg', '.jpeg', '.png', '.gif'),
            'Musica': ('.mp3', '.wav', '.flac'),
            'Videos': ('.mp4', '.avi', '.mkv', '.mov'),
            'CSV': ('.csv'),
            'Excel': ('.xlsx')
        }
        self.dir_path = None

    def organize(self):
        # obtiene la ruta del directorio actual si no se proporciona una ruta personalizada
        if not self.dir_path:
            self.dir_path = os.getcwd()

        # recorre cada archivo en el directorio
        for filename in os.listdir(self.dir_path):
            # obtiene la ruta completa del archivo
            file_path = os.path.join(self.dir_path, filename)

            # verifica si es un archivo
            if os.path.isfile(file_path):
                # obtiene la extensión del archivo
                extension = os.path.splitext(filename)[1]

                # busca el tipo de archivo y mueve el archivo a la carpeta correspondiente
                for folder, extensions in self.types.items():
                    if extension in extensions:
                        folder_path = os.path.join(self.dir_path, folder)
                        if not os.path.exists(folder_path):
                            os.mkdir(folder_path)
                        shutil.move(file_path, os.path.join(folder_path, filename))
                        break

    def set_dir_path(self, dir_path):
        # verifica si la ruta proporcionada es válida
        if os.path.isdir(dir_path):
            self.dir_path = dir_path
        else:
            print(f"La ruta '{dir_path}' no es válida.")


if __name__ == '__main__':
    # crea una instancia de FileOrganizer
    file_organizer = FileOrganizer()

    # organiza los archivos en la ruta actual
    file_organizer.organize()

