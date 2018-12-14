"""
CS 2302
Emilio Ramirez
Lab 6
Diego Aguirre,  Manoj Saha
Last Date Modified: December 14th, 2018
Purpose:  Implement Kruskal's Algorithm and Topoligic sort
"""


from LAB6sup import topological_sort
from Graph_AM import GraphAM



def main():

    Graph = GraphAM(6, True)
    Graph.add_edge(5,2, weight= 1)
    Graph.add_edge(2,1, weight= 1)
    Graph.add_edge(4,3, weight= 1)
    Graph.add_edge(3,2, weight= 1)
    Graph.add_edge(3,0, weight= 1) 
    
    print("The result of topological sort on the given graph is", topological_sort(Graph))

main()