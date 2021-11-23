
class Graph():
    def __init__(self, nvertices):
        self.N = nvertices
        self.graph = [[0 for column in range(nvertices)]
                      for row in range(nvertices)]
        self.V = ['0' for v in range(nvertices)]

    def nameVertexes(self):
        for i in range(self.N):
            self.V[i] = input(("Qual o rotulo de %i?\n" % (i)))

    def readWeights(self):
        for i in range(self.N):
            for j in range(self.N):
                if (i != j):
                    self.graph[i][j] = int(
                        input(("Digite o peso entre %s e %s\n" % (self.V[i], self.V[j]))))

    def setEdge(self, u, v, w):
        self.graph[u][v] = w

    def loadEdges(self):
        for i in range(self.N):
            for j in range(self.N):
                if (i != j):
                    print("Qual o peso entre %c e %c?\n" %
                          (self.V[i], self.V[j]))
                    self.setEdge(i, j, input())

    def getAdjacency(self):
        target1 = (
            (input(("Digite os nome dos dois vertices que pretende verificar a distancia\n"))))
        target2 = (input())
        for i in range(self.N):
            if (target1 == self.V[i]):
                aux = i

            if (target2 == self.V[i]):
                aux2 = i
        print("A distancia entre os ponto selecionados é %i\n" %
              (self.graph[aux][aux2]))

    def getDegree(self):
        count = 0
        target = (
            (input(("Digite os nome do vertices que pretende verificar o grau\n"))))
        for i in range(self.N):
            if (target == self.V[i]):
                aux = i

        for i in range(self.N):
            if (self.graph[aux][i] != 0):
                count += 1

        print("o grau do vertice é %i\n" % (count))

    def isSubGraph(self):
        print("Qual o numero de vertices?\n")
        n = int(input())
        h = Graph(n)
        print(h.graph)
        h.nameVertexes()
        print(h.V)
        h.readWeights()
        print(h.graph)
        # le o segundo grafo
        count = 0
        aux = 0
        for i in range(h.N):
            for j in range(g.N):
                if (h.V[i] == g.V[j]):
                    count += 1
        if (count == h.N):
            count = 0
            for row in range(h.N):
                for column in range(h.N):
                    if h.graph[row][column] == self.graph[row][column]:
                        count += 1
            if(count == h.N**2):
                print("É subgrafo")
                return
        print("Não é subgrafo")

    def getEdgeNumber(self):
        count = 0
        for i in range(self.N):
            for j in range(self.N):
                if (i >= j):
                    if (self.graph[i][j] != 0):
                        count += 1

        print("o numero de arestas é %i \n" % (count))

    def isComplete(self):
        count = 0
        for i in range(self.N):
            for j in range(self.N):
                if (self.graph[i][j] == 0):
                    count += 1

        if (count > self.N):
            print("o grafo nao é completo\n")
            return
        print("o grafo é completo\n")

    def isCicle(self):
        txt = (input(("Digite a sequencia que planeja verificar separada por espaços\n")))
        seq = txt.split()
        for i in seq:
            count = 0
            for j in range(len(seq)-1):
                if (i == seq[j]):
                    count += 1
            if (count > 1):  # verifica se algum vertice alem do primeiro se repete
                print("Não é um ciclo")
                return
        if (seq[0] == seq[-1]):  # verifica se o ciclo é fechado
            for i in range(len(seq)-1):
                for j in range(self.N):
                    if (seq[i] == self.V[j]):
                        aux = j
                    if (seq[i+1] == self.V[j]):
                        aux2 = j
                if (self.graph[aux][aux2] == 0):  # verifica adjacencia
                    print("Não é um ciclo")
                    return
            print("é um ciclo")
            return
        print("Não é um ciclo")


print("Qual o numero de vertices?")
n = int(input())
g = Graph(n)
print(g.graph)
g.nameVertexes()
print(g.V)
g.readWeights()
print(g.graph)

# g.getAdjacency()
# g.getDegree()
# g.isSubGraph()
# g.getEdgeNumber()
# g.isComplete()
g.isCicle()
