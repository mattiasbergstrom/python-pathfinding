# -*- coding: utf-8 -*-
#py_algorithms.py
"""This module stores the implementations of the pathfinding algorithms"""
import heapq
__all__ = ['astar']

def astar(start_node, target_node):
    """The A* pathfinding algorithm
    """
    # TODO: tie break f values with h (tuple (f, h, node), not (f, node))
    # reduces searching in general, am I right?
    closed = set()
    open_set = set()
    open = []
    
    h_score = {start_node: start_node.heuristic(target_node)}
    g_score = {start_node: 0}
    f_score = {start_node: h_score[start_node] + g_score[start_node]}
    
    came_from = {}
    start_pair = [f_score[start_node], h_score[start_node], start_node]
    heapq.heappush(open, start_pair)
    open_d = {start_node: start_pair}
    while open:
        f, h, node = heapq.heappop(open)
        del open_d[node]
        if node == target_node:
            return reconstruct_path(came_from, target_node) #fix <-- what did that mean?
        closed.add(node)
        for neighbor in node.get_neighbors():
            if neighbor in closed:
                continue
         
            tentative_g_score = g_score[node] + node.move_cost(neighbor)
            if neighbor not in open_d:
                came_from[neighbor] = node
                g_score[neighbor] = tentative_g_score
                h = h_score[neighbor] = neighbor.heuristic(target_node)
                f = f_score[neighbor] = g_score[neighbor] + h_score[neighbor]
                d = open_d[neighbor] = [f, h, neighbor]
                heapq.heappush(open, d)
            elif tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = node
                g_score[neighbor] = tentative_g_score
                f = f_score[neighbor] = g_score[neighbor] + h_score[neighbor]
                open_d[neighbor][0] = f
                heapq.heapify(open)
                
    
    raise ValueError("No path exists.")

def reconstruct_path(came_from, target_node):
    path = []
    node = target_node
    while node in came_from:
        path.append(node)
        node = came_from[node]
    return reversed(path)