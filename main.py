# import constant # Ex: constant.MENUS 
# from constant import * # Export all function
from constant import MENUS, getMenu
import calculation

def menus():
    print("%d. %s" % (getMenu("PLUS", "value"), getMenu("PLUS", "name")))
    print("%d. %s" % (getMenu("MINUS", "value"), getMenu("MINUS", "name")))
    print("%d. %s" % (getMenu("KALI", "value"), getMenu("KALI", "name")))
    print("%d. %s" % (getMenu("BAGI", "value"), getMenu("BAGI", "name")))
    print("%d. %s" % (getMenu("MODULUS", "value"), getMenu("MODULUS", "name")))

def getMenuInput() -> str:
    return input("Pilih menu: ")

def getNumberInput(num) -> float:
    while True:
        try:
            return float(input(f"Masukkan angka ke-{num}: "))
        except ValueError:
            print("Input harus berupa angka.")

def getGroupNumberInput():
    value1 = getNumberInput(1)
    value2 = getNumberInput(2)
    return [value1, value2]

def getResult(choice) -> str:
    choice = int(choice) 
    
    operations = {
        getMenu("PLUS", "value"): calculation.plus,
        getMenu("MINUS", "value"): calculation.minus,
        getMenu("KALI", "value"): calculation.multiply,
        getMenu("BAGI", "value"): calculation.divide,
        getMenu("MODULUS", "value"): calculation.modulus,
    }
    
    if choice in operations:
        value1, value2 = getGroupNumberInput()
        result = operations[choice](value1, value2)
        return str(result)
    
    return "Pilihan tidak valid!"

def main():
    print("--- Calculator Sederhana ---")
    menus()
    value = getMenuInput()
    result = getResult(value)
    print("\nHasil: \n" + result)
    
    
if __name__ == "__main__":
    main()