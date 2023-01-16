"""class FormulaError(Exception):
    pass
calc = input("Please input the number of variables: ")

try:
    calc = int(calc)
except ValueError:
    print("Introduce a natural number")

if calc < 2:
    print("Please write a number that is equal or greater then 2")

listnr = []

while len(listnr) != calc:
    x = input("Please insert a number: ")

    try:
        x = float(x)
        listnr.append(x)
    except ValueError:
        print("Introduce a natural number")

print(listnr)

# oper = calc - 1
# opernr = []
# perop = ["-", "+", "*", "/", "//", "%", "**"]
#
# for y in range(0, oper):
#     x = input("Please insert an operation: ")
#     if x not in perop:
#         x = input("Please insert an operation: ")
#     else:
#         opernr.append(x)


class FormulaError(Exception):
    pass
calc = input("Please input the number of variables: ")

try:
    calc = int(calc)
except ValueError:
    print("Introduce a natural number")

if calc < 2:
    print("Please write a number that is equal or greater then 2")

listnr = []

while len(listnr) != calc:
    x = input("Please insert a number: ")

    try:
        x = float(x)
        listnr.append(x)
    except ValueError:
        print("Introduce a natural number")

print(listnr)

oper = calc - 1
opernr = []
perop = ["-", "+", "*", "/", "//", "%", "**"]
while len(opernr)<oper:
#for y in range(0, oper):
    x = input("Please insert an operation: ")
    if x not in perop:
        x = input("Please insert another operation: ")
    else:
        opernr.append(x)
print(opernr)

ecuatie = []

for x in range(0, calc-1):
    ecuatie.append(listnr[x])
    if len(opernr) < len(listnr):
        ecuatie.append(opernr[x])
else:
    ecuatie.append(listnr[calc-1])
print(ecuatie)


while oper > 0:
    x = 1
    poz = 1
    prim = x - 1
    if ecuatie[x] == "+":
        ras = ecuatie[prim] + ecuatie[poz + 1]
    if ecuatie[x] == "-":
        ras = ecuatie[prim] - ecuatie[poz + 1]
    if ecuatie[x] == "*":
        ras = ecuatie[prim] * ecuatie[poz + 1]
    if ecuatie[x] == "/":
        ras = ecuatie[prim] / ecuatie[poz + 1]
    if ecuatie[x] == "//":
        ras = ecuatie[prim] // ecuatie[poz + 1]
    if ecuatie[x] == "%":
        ras = ecuatie[prim] % ecuatie[poz + 1]
    if ecuatie[x] == "**":
        ras = ecuatie[prim] ** ecuatie[poz + 1]
    oper = oper - 1
    ecuatie = ecuatie[3:]
    ecuatie.insert(0, ras)
    print(ecuatie)"""
