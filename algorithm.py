from collections import OrderedDict

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
    for i in dictHeuristic.keys():
        if i == city:
            node = [(i, "0+"+dictHeuristic.get(i)[0])]
    return accessed, node

def roundtrip(dictGraph):
    for key1 in dictGraph.keys():
        for key2 in dictGraph.keys():
            for x in dictGraph[key2]:
                if x[0][0] == key1:
                    dictGraph[key1].append([(key2, x[0][1])])
    return dictGraph

def main():
    dictGraph, dictHeuristic = initializeFiles('Grafo.txt', 'Heuristica.txt')
    accessed, node = initialize('Arad', dictHeuristic)
    dictGraph = roundtrip(dictGraph)
    currentCity = node[0]
    smaller = '0'
    route = ''
    while currentCity[0] != 'Bucareste' and currentCity[1] != eval(smaller):
        smaller = node[0][1]
        smallerCity = ''
        for i in node:
            if eval(i[1]) <= eval(smaller) and not i[0] in accessed:
                smaller = i[1]
                smallerCity = i[0]

        currentCity = ((smallerCity, smaller))
        route = route+"--->"+str((smallerCity,eval(smaller)))
        if(currentCity[0] != 'Bucareste' and currentCity[1] != eval(smaller)):
            if dictGraph[smallerCity]:
                parcel = smaller.split('+')
                for i in dictGraph[smallerCity]:
                    s = int(parcel[0])+int(i[0][1])
                    node.append((i[0][0], str(s)+"+"+dictHeuristic.get(i[0][0])[0]))

            for i in node:
                if i[0] == smallerCity:
                    node.remove((smallerCity, i[1]))
                    accessed.append(smallerCity)

    print(route)
main()
