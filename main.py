from pygame import *
import math
from queue import PriorityQueue
#I think that's all we will need for sure, we can add later if we need it
'''
#Initialization of the window
length, width = 800, 800
window = display.set_mode(length, width)
display.set_caption("Path Finding Algorithm")
'''


#Graph is testing only
graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}
vis = []
def dfs(graph, node):
    global vis
    if node not in vis:
        vis.append(node)
        for n in graph[node]: dfs(graph,n)
dfs(graph,"A")
'''
making the grid
'''

'''
main function that calls the others
'''

