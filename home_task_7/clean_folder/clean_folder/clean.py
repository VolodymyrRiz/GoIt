import sys
import re
import shutil
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
WAV_AUDIO = []
AVI_VIDEOS = []
MP4_VIDEOS = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
XLS_DOCUMENTS = []
PDF_DOCUMENTS = []
MY_OTHER = []
ZIP_ARCHIVES = []
RAR_ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'PDF': PDF_DOCUMENTS,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'WAV': WAV_AUDIO,
    'XLS': XLS_DOCUMENTS,
    'RAR': RAR_ARCHIVES,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  # suffix[1:] -> .jpg -> jpg

def scan(folder: Path):
    print("СКАНУЮ ПАПКИ ТА ФАЙЛИ. Зачекайте..........")
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():  # перевіряємо чи обєкт папка
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        # Робота з файлом
        extension = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  # .mp4, .mov, .avi
                MY_OTHER.append(full_name)


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"?*()+-%!№=@# '
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "_", "y", "_", "e", "yu", "u", "ja", "je", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    print("ПЕРЕЙМЕНОВУЮ ПАПКИ ТА ФАЙЛИ З МЕТОЮ НОРМАЛІЗАЦІЇ НАЗВ........")
    translate_name = re.sub(r'\W\[^.]', '_', name.translate(TRANS))
    return translate_name


def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))
    
def handle_doc(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    print('ПОЧИНАЮ УПОРЯДКУВАННЯ ВАШОЇ ПАПКИ. Невідомі файли будуть у папці "MY_OTHER"')
    scan(folder)
    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')        
    for file in AVI_VIDEOS:
        handle_media(file, folder / 'videos' / 'AVI')
    for file in MP4_VIDEOS:
        handle_media(file, folder / 'videos' / 'MP4')        
    for file in MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3_AUDIO')
    for file in WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV_AUDIO')         
    for file in DOC_DOCUMENTS:
        handle_doc(file, folder / 'documents' / 'DOC')  
    for file in DOCX_DOCUMENTS:
        handle_doc(file, folder / 'documents' / 'DOCX')   
    for file in PDF_DOCUMENTS:
        handle_doc(file, folder / 'documents' / 'PDF') 
    for file in XLS_DOCUMENTS:
        handle_doc(file, folder / 'documents' / 'XLS')        
    for file in MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')
    for file in ZIP_ARCHIVES:
        handle_archive(file, folder / 'ARCHIVES')
    for file in RAR_ARCHIVES:
        handle_archive(file, folder / 'ARCHIVES')

    for folder in FOLDERS[::-1]:
        # Видаляємо пусті папки після сортування
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')
            
def start():
    if sys.argv[1]:
        folder_process = Path(sys.argv[1])
        main(folder_process.resolve())  
        print('РОБОТУ ЗАВЕРШЕНО!')          

# if __name__ == "__main__":
#     folder_process = Path(sys.argv[1])
#     main(folder_process.resolve())
#     print('РОБОТУ ЗАВЕРШЕНО!')