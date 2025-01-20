def plus(a, b) -> float:
    return float(a) + float(b)

def minus(a, b) -> float:
    return float(a) - float(b)

def multiply(a, b) -> float:
    return float(a) * float(b)

def safe_divide(a,b):
    return int(b) != 0

def divide(a, b) -> float:
    if(safe_divide(a, b)):
        return float(a) / float(b)
    return "Error: Pembagian dengan nol!"
    
def modulus(a, b) -> float:
    return float(a) % float(b)