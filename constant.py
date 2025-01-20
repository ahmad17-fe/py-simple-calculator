MENUS = {
    "PLUS": {
        "value": 1,
        "name": "Tambah"     
    },
    "MINUS": {
        "value": 2,
        "name": "Kurang"     
    },
    "KALI": {
        "value": 3,
        "name": "Kali"
    },
    "BAGI": {
        "value": 4,
        "name": "Bagi"     
    },
    "MODULUS": {
        "value": 5,
        "name": "Modulus"     
    },
}

def getMenu(key, type) -> str:
    return MENUS.get(key).get(type)