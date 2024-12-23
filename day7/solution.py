from itertools import product

filename = "data"
with open(f"data/{filename}.txt", "r") as f:
    raw = f.readlines()

data = [[j.strip() for j in i.split(":")] for i in raw]
#print(data)
def eval_gauche_droite(expression, p1=True):
    #print(expression)
    result = int(expression[0])
    add = 0
    for i in range(1,len(expression)):
        item = expression[i]
        if item == "+":
            add = 0
        elif item == "*":
            add = 1
        elif item == "||":
            add = 2
        else:
            if add == 0:
                result = result + int(item)
            elif add == 1:
                result = result * int(item)
            elif add == 2:
                result = int(str(result) + str(item))

    return result

operators = ["*", "+", "||"]

def process_eq(result: int, params: list):
    permu = product(operators, repeat=len(params)-1)
    eqs = {}
    for p in permu:
        eq = []
        for i in range(len(params)):
            eq.append(str(params[i]))
            if i < len(p):
                eq.append(str(p[i]))
        if "".join(eq) not in eqs:
            eqs["".join(eq)] = eq

    for eq, eqv in eqs.items():
        rez = eval_gauche_droite(eqv)
        if rez == result:
            return result
    return 0

somme = 0

for equation in data:
    result = int(equation[0])
    params = [int(i) for i in equation[1].split(" ")]
    somme += process_eq(result, params)
print(somme)