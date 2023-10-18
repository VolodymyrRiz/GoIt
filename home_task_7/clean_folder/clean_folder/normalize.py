import re

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
