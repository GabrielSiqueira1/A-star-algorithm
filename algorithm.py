from collections import OrderedDict

def initializeFiles(file1, file2):
    #TODO
    return dictGraph, dictHeuristic

def initialize(city):
    #TODO
    return accessed, node

def roundtrip(dictGraph):
    #TODO
    return dictGraph

def main():
    accessed, node = initialize('Arad')
    dictGraph, dictHeuristic = initializeFiles('Grafo.txt', 'Heuristica.txt')
    dictGraph = roundtrip(dictGraph)
    while currentCity[0] != 'Bucareste' and currentCity[1] != eval(smaller):
        smaller = node[0][1]
        smallerCity = ''
        for i in node:
            if i[1] <= smaller and not i[0] in accessed:
                smaller = i[1]
                smallerCity = i[0]

        currentCity = ((smallerCity, smaller))

        if dictGraph[smallerCity]:
            parcel = smaller.split('+')
            for i in dictGraph[smallerCity]:
                s = int(parcel[0])+int(i[0][1])
                node.append((i[0][0], str(s)+"+"dictHeuristic.get(i[0][0])[0]))

        for i in node:
            if i[0] == smallerCity:
                node.remove((smallerCity, i[1]))
                accessed.append(smallerCity)

        print(node)
        print("-------------------")

main()
