from collections import OrderedDict

# Função que toma como parâmetro os dois arquivos do exercício, o grafo e a heurística o separando em dois dicionários
# que facilitam a utilização nas funções que se seguem
def initializeFiles(file1, file2):
    dictGraph = OrderedDict()
    dictHeuristic = OrderedDict()

    file2 = open(file2, "r")
    for word in file2:
        w = word.replace('\n', '')
        token = w.split(';')
        if(token[0] in dictHeuristic.keys()):
            dictHeuristic[token[0]].append(token[1])
        else:
            dictHeuristic[token[0]] = []
            dictHeuristic[token[0]].append(token[1])

    file1 = open(file1, "r")
    for word in file1:
        w = word.replace('\n', '')
        token = w.split(';')
        if(token[0] in dictGraph.keys()):
            dictGraph[token[0]].append([(token[1],token[2])])
        else:
            dictGraph[token[0]] = []
            dictGraph[token[0]].append([(token[1],token[2])])

    return dictGraph, dictHeuristic

def initialize(city, dictHeuristic):
    accessed = []
    position = OrderedDict()
    for i in dictHeuristic.keys():
        if i == city:
            node = [(i, "0+"+dictHeuristic.get(i)[0])]
            if i not in position.keys():
                position[i] = 0 
    
    return accessed, node, position

def roundtrip(dictGraph):
    for key1 in dictGraph.keys():
        for key2 in dictGraph.keys():
            for x in dictGraph[key2]:
                if x[0][0] == key1:
                    dictGraph[key1].append([(key2, x[0][1])])
    return dictGraph

def main():
    dictGraph, dictHeuristic = initializeFiles('Grafo.txt', 'Heuristica.txt')
    accessed, node, position = initialize('Arad', dictHeuristic)
    dictGraph = roundtrip(dictGraph)
    currentCity = node[0]
    it = 0
    aux = 0
    smaller = '0'
    route = ''
    while currentCity[0] != 'Bucareste' and currentCity[1] != eval(smaller):
        
        print(f"Iteração = {it}, que tem os seguintes nós abertos!")
        print(node)
        print()

        smaller = node[0][1]
        smallerCity = ''
        for i in node:
            if eval(i[1]) <= eval(smaller) and not i[0] in accessed:
                smaller = i[1]
                smallerCity = i[0]

        currentCity = ((smallerCity, smaller))
    
        if position[smallerCity] >= aux:
            route = route+"--->"+str((smallerCity,eval(smaller)))
            aux += 1

        if(currentCity[0] != 'Bucareste' and currentCity[1] != eval(smaller)):
            if dictGraph[smallerCity]:
                parcel = smaller.split('+')
                for i in dictGraph[smallerCity]:
                    s = int(parcel[0])+int(i[0][1])
                    node.append((i[0][0], str(s)+"+"+dictHeuristic.get(i[0][0])[0]))
                    if i[0][0] not in position.keys():
                        position[i[0][0]] = (it + 1)        

            for i in node:
                if i[0] == smallerCity:
                    print(f"Abertura do nó {i[0]}")
                    node.remove((smallerCity, i[1]))
                    accessed.append(smallerCity)

        it += 1

    print("Cidades que tiveram os nós abertos, em ordem:")
    print(accessed)
    print()
    print("Rota final:")
    print(route)
main()
