""" {'A' : [(B, weight), ]}"""
from collections import defaultdict

import random as rand
import time 


class Graph(object):
    def __init__(self):
        self.__edges = defaultdict(list)

    def __str__(self):
        sort_keys =sorted(key for key in self.__edges)
        out = ""
        for key in sort_keys:
            out += str(key) + " : "
            for edges in self.__edges[key]:
                out += str(edges) + " "
            out += "\n" 
        return out

    
    def add_nodes(self, nodes: set):
        for node in nodes:
            self.__edges[node]
    
    def add_undirected_edge(self, node1: int , node2: int, weight: int):
        if node1 in self.__edges and node2 in self.__edges and weight >= 1:
            self.__edges[node1].append((node2, weight)) 
            self.__edges[node2].append((node1, weight))
    
    def add_directed_edge(self, source: int , target: int, weight: int):
        if source in self.__edges and target in self.__edges and weight >= 1:
            self.__edges[source].append((target, weight))
    
    def shortest_path(self, source: int, target: int): # This is a implementation of Dijkstra's Algorithm
        import math
        found = False
        Q = set()
        dist = {}
        prev = {}
        for v in self.__edges:
            Q.add(v)
            dist[v] = math.inf
            prev[v] = None
        
        dist[source] = 0
        
        while Q: # while Q is not empty
            u = min([node for node in dist if node in Q] , key=dist.get ) #returns the min of the distance so long as it is in Q
            
            if u == target:
                found = True
                break
            Q.remove(u)
            
            neighbors = {n for n in self.__edges[u]}
            for v in neighbors:
                alt = dist[u] + v[1]
                if alt < dist[v[0]]:
                    dist[v[0]] = alt
                    prev[v[0]] = u
            
       
        if not found:
            return None, None

        distance = dist[target]
        path = []
        node = target
        while node is not None:
            path.append(node)
            node = prev[node]
        
        return path, distance
    
    def generate_random_undirected_graph(self,num_edges: int, max_weight: int):
        if max_weight >= 1:
            self.clear_all_paths() #empty all paths
            if self.__edges:
                rand.seed(time.time())
                not_connected = []
                connected = []
                
                for key in self.__edges: # add all vertexs to not connected list
                    not_connected.append(key)
                
                rand_int = rand.randint(0, len(not_connected) -1)
                vertex_1 = not_connected[rand_int]
                connected.append(vertex_1)
                not_connected.remove(vertex_1)
                
                while not_connected:
                    rand_int = rand.randint(0, len(not_connected) -1)
                    rand_weight = rand.randint(1, max_weight)
                    vertex_2 = not_connected[rand_int]
                    connected.append(vertex_2)
                    not_connected.remove(vertex_2)
                    self.add_undirected_edge(vertex_1, vertex_2, rand_weight)
                    vertex_1 = vertex_2

                for _ in range(0, num_edges): #add random eddges to the graph
                    rand_weight = rand.randint(1, max_weight)
                    vertex = rand.sample(connected, 2)
                    self.add_undirected_edge(vertex[0],vertex[1],rand_weight)
            

    def clear_all_paths(self):
        for node in self.__edges:
            self.__edges[node] = []


    