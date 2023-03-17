from collections import OrderedDict

arquivo = open("Heuristica.txt", "r")

listaHeuristica = []
for palavra in arquivo:
    p = palavra.replace('\n', '')
    teste = p.split(';')
    listaHeuristica.append(teste)

arquivo2 = open("Grafo.txt", "r")

dicio = OrderedDict()
for palavra in arquivo2:
    p = palavra.replace('\n','')
    teste = p.split(';')
    if teste[0] in dicio.keys():
        dicio[teste[0]].append([(teste[1], teste[2])])
    else:
        dicio[teste[0]] = []
        dicio[teste[0]].append([(teste[1], teste[2])])

acesso = []

for j in listaHeuristica:
    if j[0] == 'Arad':
       abertas = [(j[0], "0+"+j[1])]

###########

menor = abertas[0][1]
menorCidade = ''
for j in abertas:
    if j[1] <= menor:
        menor = j[1]
        menorCidade = j[0]

#print(eval(menor))

for dii in dicio.keys():
    for di in dicio.keys():
        for x in dicio[di]:
            if x[0][0] == dii:
                dicio[dii].append([(di, x[0][1])])

print(dicio)

for sla in dicio.keys():
    if dicio[menorCidade]:
        y = menor.split('+')
        for x in dicio[menorCidade]:
            abertas.append((x[0][0], y[0]+x[0][1]+"+"+listaHeuristica[]))
        
        
