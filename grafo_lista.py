import queue
import sys


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

    def getDegree(self):
        count = 0
        target = (
            (input(("Digite o nome do vertice que pretende verificar o grau\n"))))
        for v in g:
            if (v.get_id() == target):
                print(g.vert_dict[v.get_id()])

    def getEdges(self):
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

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
        edges = self.getEdgeNumber()
        if (edges != (self.num_vertices * self.num_vertices-1)/2):
            print("o grafo nao é completo")
            return
        print("o grafo é completo")

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
                    print("%s foi explorado" % (x))

    def DeepSearch(self, vert):
        self.setAllUnexplored()
        stack = []
        stack.append(vert)
        while (len(stack) != 0):
            vert = stack.pop()
            vert.explored = 1
            print("%s foi explorado" % (vert))
            for x in vert.adjacent:
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

    def geraMatriz(self):
        return [[" "]*self.getNumVertex() for _ in range(self.getNumVertex())]


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
# g.add_vertex('id4')
# g.add_edge('id0', 'id1', -1)
# g.add_edge('id0', 'id2', 4)
# g.add_edge('id1', 'id2', 3)
# g.add_edge('id1', 'id3', 2)
# g.add_edge('id1', 'id4', 2)
# g.add_edge('id3', 'id2', 5)
# g.add_edge('id3', 'id1', 1)
# g.add_edge('id4', 'id3', -3)

g.add_edge('id0', 'id1', 2)
g.add_edge('id1', 'id2', 4)
g.add_edge('id2', 'id3', 5)
g.add_edge('id3', 'id0', 11)


# print(g.getAdjacency('id1', 'id1'))

# g.getDegree()
# g.isSubGraph()
# g.getEdgeNumber()
# g.isComplete()
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

d, p = g.FloydWarshall()
print(d)
print("\n")
print(p)
