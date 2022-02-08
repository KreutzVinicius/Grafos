import queue
import sys
from itertools import combinations


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = 0
        self.pred = node
        self.d = sys.maxsize

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def getAdjacent(self):
        return self.adjacent


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def getNumVertex(self):
        return self.num_vertices

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        # comentar linha abaixo para grafo direcionado
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def getAdjacency(self, vertex1, vertex2):
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()

                if (vertex1 == vertex2):
                    return 0

                if (vid == vertex1 and wid == vertex2):
                    return(v.get_weight(w))

    def getAdjacencyMatrix(self):
        matrix = self.geraMatriz()
        for i, u in enumerate(self):
            for j, v in enumerate(self):
                if (self.getAdjacency(u.id, v.id) != None):
                    matrix[i][j] = g.getAdjacency(u.id, v.id)
                else:
                    matrix[i][j] = float("inf")
        return matrix

    def geraMatriz(self):
        return [[" "]*self.getNumVertex() for _ in range(self.getNumVertex())]

    def getDegree(self, target):
        count = 0
        for v in g:
            if (v == target):
                for u in v.getAdjacent():
                    count = count + 1
                return count

    def getEdges(self):
        done = []
        edges = []
        for v in self:
            done.append(v.id)
            for w in v.get_connections():
                test = 0
                vid = v.get_id()
                wid = w.get_id()

                for u in done:
                    if u == w.id:
                        test = 1
                if test == 0:
                    edges.append([vid, wid, v.get_weight(w)])
        return edges

    def getAdjacents(self):
        for v in g:
            print('%s' % (g.vert_dict[v.get_id()]))

    def isSubGraph(self):
        count = 0
        h = Graph()

        h.add_vertex('a')
        h.add_vertex('b')
        h.add_vertex('l')

        h.add_edge('a', 'b', 100)
        h.add_edge('a', 'l', 750)
        h.add_edge('b', 'l', 650)

        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()

                for a in h:
                    for b in a.get_connections():
                        vid2 = a.get_id()
                        wid2 = b.get_id()

                        if (vid == vid2 and wid == wid2 and v.get_weight(w) == a.get_weight(b)):
                            count += 1

        if (h.num_vertices == count/2):
            print("É subgrafo")
            return
        print("Não é subgrafo")

    def getEdgeNumber(self):
        count = 0
        for v in g:
            for w in v.get_connections():
                count += 1
        return count/2

    def isComplete(self):
        for v in self:
            numConexoes = 0
            for w in v.get_connections():
                numConexoes += 1
            if numConexoes != self.num_vertices-1:
                return 'Não é completo'
        return 'É completo'

    def setAllUnexplored(self):
        for v in self:
            v.explored = 0

    def BreadthSearch(self, vert):
        self.setAllUnexplored()
        vert.explored = 1
        q = queue.Queue()
        q.put(vert)
        while(q.qsize() != 0):
            vert = q.get()

            for x in vert.adjacent:
                if (x.explored == 0):
                    x.explored = 1
                    q.put(x)
                    # print("%s foi explorado" % (x))

    def DeepSearch(self, vert):
        self.setAllUnexplored()
        stack = []
        stack.append(vert)
        while (len(stack) != 0):
            vert = stack.pop()
            vert.explored = 1
            # print("%s foi explorado" % (vert))
            for x in self:
                if(x.explored == 0):
                    stack.append(x)

    def getMenorInexplorado(self):
        menor = sys.maxsize
        for v in self.vert_dict:
            if self.vert_dict[v].explored == 0 and self.vert_dict[v].d < menor:
                menorVertice = v
                menor = self.vert_dict[menorVertice].d
        return menorVertice

    def Dijkstra(self, vert):
        explored = []
        for v in self.vert_dict:
            self.vert_dict[v].explored = 0
            self.vert_dict[v].pred = -1
            self.vert_dict[v].d = sys.maxsize
        self.vert_dict[vert].d = 0
        while len(self.vert_dict) != len(explored):
            u = self.getMenorInexplorado()
            explored.append(u)
            self.vert_dict[u].explored = 1
            for v in self.vert_dict[u].get_connections():
                if v.explored == 0 and self.vert_dict[u].d+self.vert_dict[u].get_weight(v) < v.d:
                    v.d = self.vert_dict[u].d+self.vert_dict[u].get_weight(v)
                    v.pred = u

    def getmaiordistancia(self):
        aux = float("-inf")
        for v in self:
            if aux < v.d:
                aux = v.d
        return aux

    def BellmanFord(self, vert):
        for v in self.vert_dict:
            self.vert_dict[v].pred = -1
            self.vert_dict[v].d = sys.maxsize
        self.vert_dict[vert].d = 0

        for index, u in enumerate(self):
            if (index >= (self.getNumVertex())):
                break
            for v in self.vert_dict[u.id].get_connections():
                if u.d != sys.maxsize and u.d + self.vert_dict[u.id].get_weight(v) < v.d:
                    v.d = u.d + self.vert_dict[u.id].get_weight(v)
                    v.pred = u

        for u in self:
            for v in self.vert_dict[u.id].get_connections():
                if u.d != sys.maxsize and u.d + self.vert_dict[u.id].get_weight(v) < v.d:
                    print("Grafo contem ciclo de peso negativo")
                    return

    def FloydWarshall(self):
        d = self.geraMatriz()
        pred = self.geraMatriz()
        for i, u in enumerate(self):
            for j, v in enumerate(self):
                if (self.getAdjacency(u.id, v.id) != None):
                    d[i][j] = g.getAdjacency(u.id, v.id)
                    pred[i][j] = u.id
                else:
                    d[i][j] = float("inf")
        for k, w in enumerate(self):
            for i, u in enumerate(self):
                for j, v in enumerate(self):
                    if (d[i][j] > d[i][k] + d[k][j]):
                        d[i][j] = d[i][k] + d[k][j]
                        pred[i][j] = w.id
        return d, pred

    def isEulerian(self):
        if self.isConected() == 0:
            return 0
        impares = 0
        for v in self:
            if (self.getDegree(v) % 2) != 0:
                impares += 1
        print(impares)
        if impares == 0:
            print("ciclo")
        if impares == 2:
            print("caminho")
        if impares > 2:
            print("nao é Euleriano")

    def isConected(self):
        # somente grafos nao direcionados
        self.setAllUnexplored()
        u = self.getAnyNode()
        self.DeepSearch(u)
        for v in self:
            if v.explored == 0:
                return 0
            return 1

    def getAnyNode(self):
        for v in self:
            if self.getDegree(v) > 0:
                return v

    def Hierholezer(self):
        if self.isConected() == 1:
            self.setAllUnexplored()
            impares = 0
            for v in self:
                if (self.getDegree(v) % 2) != 0:
                    impares += 1
                    aux = v

            # if impares == 0:
            #     # ciclo nao está funcionando, nao imprime os nós onde ja passou
            #     print("Ciclo de Euler:")
            #     self.printEuler(self.getAnyNode())
            if impares == 2:
                print("Caminho de Euler:")
                self.printEuler(aux)
            else:
                print("Caminho nao existe")

    def printEuler(self, vert):
        c = []
        e = []
        explored = []

        c.insert(0, vert)
        vert.explored = 1

        while len(c):
            u = c[0].getAdjacent()
            aux = 0
            for v in u:
                if v.explored == 0:
                    aux = v
            if aux == 0:
                aux = c.pop()
                e.insert(0, aux)
            else:
                c.insert(0, aux)
                explored.append((u, aux))
                aux.explored = 1

        for i in e:
            print(i.id)

    def caixeiro(self):
        d = self.geraMatriz()
        for i, u in enumerate(self):
            for j, v in enumerate(self):
                if (self.getAdjacency(u.id, v.id) != None):
                    d[i][j] = g.getAdjacency(u.id, v.id)
                else:
                    d[i][j] = float("inf")
        n = g.getNumVertex()
        caixeiro = [[float("inf") for _ in range(n)] for __ in range(2**n)]
        caixeiro[1][0] = 0
        for tam in range(1, n):
            for caminho in combinations(range(1, n), tam):
                caminho = (0,) + caminho
                k = sum([2**i for i in caminho])
                for i in caminho:
                    if i == 0:
                        continue
                    for j in caminho:
                        if j == i:
                            continue
                        index_atual = k ^ (2**i)
                        caixeiro[k][i] = min(caixeiro[k][i],
                                             caixeiro[index_atual][j] + d[j][i])
        todos_index = (2**n) - 1
        return min([(caixeiro[todos_index][i] + d[0][i])
                    for i in range(n)])

    def Prim(self):
        adjacencyMatrix = self.getAdjacencyMatrix()
        key = [float("inf")] * self.getNumVertex()
        parent = [None] * self.getNumVertex()

        key[0] = 0
        mstSet = [False] * self.getNumVertex()
        parent[0] = -1

        for _ in range(self.getNumVertex()):
            mini = float("inf")
            for v in range(self.getNumVertex()):
                if key[v] < mini and mstSet[v] == False:
                    mini = key[v]
                    u = v  # index
            mstSet[u] = True
            for v in range(self.getNumVertex()):
                if adjacencyMatrix[u][v] > 0 and mstSet[v] == False and key[v] > adjacencyMatrix[u][v]:
                    key[v] = adjacencyMatrix[u][v]
                    parent[v] = u

        print("Ramos necessarios")
        for i in range(1, self.getNumVertex()):
            print("(", parent[i], ",", i, ") = ",
                  adjacencyMatrix[i][parent[i]])


if __name__ == '__main__':

    g = Graph()

    # n, m = input("Qual o numero de vertices e arestas?").split()

    # n = int(n)
    # m = int(m)
    # s = "id"

    # for i in range(0, n):
    #     g.add_vertex('{}{}'.format(s, i))
    # g.getAdjacents()
    # for j in range(0, m):
    #     u, v, w = input("qual cidade cidade distancia ?").split()
    #     w = int(w)
    #     g.add_edge(u, v, w)

    # g.getEdges()

g.add_vertex('id0')
g.add_vertex('id1')
g.add_vertex('id2')
g.add_vertex('id3')
g.add_vertex('id4')

g.add_edge("id0", "id1", 15)
g.add_edge("id0", "id2", 12)
g.add_edge("id1", "id2", 6)
g.add_edge("id1", "id3", 13)
g.add_edge("id1", "id4", 5)
g.add_edge("id2", "id3", 6)


# print(g.getAdjacency('id1', 'id1'))
# print(g.getDegree('id1'))
# g.isSubGraph()
# print(g.getEdgeNumber())
# print(g.getEdges())
# print(g.isComplete())
# g.BreadthSearch(g.get_vertex('id0'))
# g.DeepSearch(g.get_vertex('id0'))


# aux = float("inf")
# for v in g:
#     g.Dijkstra(v.id)
#     if aux > g.getmaiordistancia():
#         aux = g.getmaiordistancia()
# print(aux)


# g.BellmanFord('id0')
# for v in g:
#     print(v.d)

# d, p = g.FloydWarshall()
# print(d)
# print("\n")
# print(p)

# g.isEulerian()

# g.Hierholezer()

# txt = input()
# txt = txt.split()
# soma = 0
# for i, x in enumerate(txt):
#     if i % 2 == 1:
#         soma = soma + int(x)
# if g.caixeiro() > soma:
#     print("menor caminho")
# else:
#     print("nao, existe percurso menor")
# print(g.caixeiro())

g.Prim()
