def suma(a: int, b: int) -> int:
    return f"{a} + {b} = {a + b}"

def suma(a: int, b: int) -> int:
    return f"{a} - {b} =  {a - b} "

def inmultire(a: int, b : int) -> int:
    return f"{a} * {b} = {a * b}"

def impartire(a: int, b: int) -> str:
    if  b == 0:
            b = int(input("Aloca o noua valoare pentru b: "))
    if a % b == 0:
        c = int(a / b)
    else:
        c = float(a / b)
    return f"{a} / {b} = {a / b}"

def operator(op):
    op = input("Alege operatorul: ")
    if op not in ['*', '/', '+', '-']:
        while op not in ['*', '/', '+', '-']:
            op = input("Alege operatorul: ")
        return op

def conversie

def calculator():
    nr1 = input("Primul numar: ")
    if nr1.isdigit():
        nr1 = int(nr1)
    else:
        while nr1.isdigit() is False:
            nr1 = input("Primul numar: ")
    nr2 = input("Al doilea numar: ")
    while nr2.isdigit() is False:
        nr2 = input("Al doilea numar: ")
    op = operator()
    if op == '+'
        rezultat = sum(nr1, nr2)
    elif op == '-'
        rezultat = diferenta(nr1, nr2)
    elif op == '*':
        rezultat = inmultire(nrq, nr2)
    else:
        rezultat = impartire(nr1, nr2)
    return rezultat

print(calculator())


