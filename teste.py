from collections import OrderedDict

arquivo = open("Heuristica.txt", "r")

dicioHeuristica = OrderedDict()
for palavra in arquivo:
    p = palavra.replace('\n', '')
    token = p.split(';')
    if token[0] in dicioHeuristica.keys():
        dicioHeuristica[token[0]].append(token[1])
    else:
        dicioHeuristica[token[0]] = []
        dicioHeuristica[token[0]].append(token[1])

arquivo2 = open("Grafo.txt", "r")

dicioGrafo = OrderedDict()
for palavra in arquivo2:
    p = palavra.replace('\n','')
    token = p.split(';')
    if token[0] in dicioGrafo.keys():
        dicioGrafo[token[0]].append([(token[1], token[2])])
    else:
        dicioGrafo[token[0]] = []
        dicioGrafo[token[0]].append([(token[1], token[2])])

acesso = []

for j in dicioHeuristica.keys():
    if j == 'Arad':
       abertas = [(j, "0+"+dicioHeuristica.get(j)[0])]

# Inicialização
################################

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if j[1] <= menor:
        menor = j[1]
        menorCidade = j[0]

## Realizar a ida e a volta com o grafo
for key1 in dicioGrafo.keys(): 
    for key2 in dicioGrafo.keys():
        for x in dicioGrafo[key2]:
            if x[0][0] == key1:
                dicioGrafo[key1].append([(key2, x[0][1])])

if dicioGrafo[menorCidade]:
    y = menor.split('+')
    for x in dicioGrafo[menorCidade]:
        soma = int(y[0]+x[0][1])
        abertas.append((x[0][0], str(soma)+"+"+dicioHeuristica.get(x[0][0])[0]))

for y in abertas:
    if y[0] == menorCidade:
        abertas.remove((menorCidade, y[1])) 
        acesso.append(menorCidade)

print(abertas)  

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if eval(j[1]) <= eval(menor):
        menor = j[1]
        menorCidade = j[0]

if dicioGrafo[menorCidade]:
    y = menor.split('+')
    for x in dicioGrafo[menorCidade]:
        soma = int(y[0])+int(x[0][1])
        if not x[0][0] in acesso:
            abertas.append((x[0][0], str(soma)+"+"+dicioHeuristica.get(x[0][0])[0]))

for y in abertas:
    if y[0] == menorCidade:
        abertas.remove((menorCidade, y[1]))
        acesso.append(menorCidade)

print(abertas)  

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if eval(j[1]) <= eval(menor):
        menor = j[1]
        menorCidade = j[0]

if dicioGrafo[menorCidade]:
    y = menor.split('+')
    for x in dicioGrafo[menorCidade]:
        soma = int(y[0])+int(x[0][1])
        if not x[0][0] in acesso:
            abertas.append((x[0][0], str(soma)+"+"+dicioHeuristica.get(x[0][0])[0]))

for y in abertas:
    if y[0] == menorCidade:
        abertas.remove((menorCidade, y[1]))
        acesso.append(menorCidade)

print(abertas)  

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if eval(j[1]) <= eval(menor):
        menor = j[1]
        menorCidade = j[0]

if dicioGrafo[menorCidade]:
    y = menor.split('+')
    for x in dicioGrafo[menorCidade]:
        soma = int(y[0])+int(x[0][1])
        if not x[0][0] in acesso:
            abertas.append((x[0][0], str(soma)+"+"+dicioHeuristica.get(x[0][0])[0]))

for y in abertas:
    if y[0] == menorCidade:
        abertas.remove((menorCidade, y[1]))
        acesso.append(menorCidade)

print(abertas)  

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if eval(j[1]) <= eval(menor):
        menor = j[1]
        menorCidade = j[0]

if dicioGrafo[menorCidade]:
    y = menor.split('+')
    for x in dicioGrafo[menorCidade]:
        soma = int(y[0])+int(x[0][1])
        if not x[0][0] in acesso:
            abertas.append((x[0][0], str(soma)+"+"+dicioHeuristica.get(x[0][0])[0]))

for y in abertas:
    if y[0] == menorCidade:
        abertas.remove((menorCidade, y[1]))
        acesso.append(menorCidade)

print(abertas)  

