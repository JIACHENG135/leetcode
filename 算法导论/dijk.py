# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:43:44 2018

@author: ljc
"""
'''
graph
'''
# In[1]
graph={}
graph['sta'] = {}
graph['sta']['1'] = 5
graph['sta']['2'] = 2
graph['1'] = {}
graph['1']['3'] = 4
graph['1']['4'] = 2
graph['2'] = {}
graph['2']['4'] = 7
graph['2']['1'] = 8
graph['3'] = {}
graph['3']['4'] = 6
graph['3']['fin'] = 3
graph['4'] = {}
graph['4']['fin'] = 1
graph['fin'] = None
# cost
costs={}
costs['1'] = 5
costs['2'] = 2
costs['fin'] = float('inf')
costs['3'] = float('inf')
costs['4'] = float('inf')
# parent
parent={}
parent['1'] = 'sta'
parent['2'] = 'sta'
parent['fin'] = None
processed = []

# In[2]
#graph={}
#graph['sta'] = {}
#graph['sta']['1'] = 10
##graph['sta']['2'] = 2
#graph['1'] = {}
#graph['1']['2'] = 20
##graph['1']['4'] = 2
#graph['2'] = {}
#graph['2']['fin'] = 30
#graph['2']['3'] = 1
#graph['3'] = {}
#graph['3']['1'] = 1
##graph['3']['fin'] = 3
##graph['4'] = {}
##graph['4']['fin'] = 1
#graph['fin'] = None
## cost
#costs={}
#costs['1'] = 10
#costs['2'] = float('inf')
#costs['fin'] = float('inf')
#costs['3'] = float('inf')
#costs['4'] = float('inf')
## parent
#parent={}
#parent['1'] = 'sta'
##parent['2'] = 'sta'
#parent['fin'] = None
#processed = []

# In[3]
#graph={}
#graph['sta'] = {}
#graph['sta']['1'] = 2
#graph['sta']['2'] = 2
#graph['1'] = {}
#graph['1']['3'] = 2
#graph['1']['4'] = 2
#graph['2'] = {}
##graph['2']['4'] = 7
#graph['2']['1'] = 2
#graph['3'] = {}
#graph['3']['4'] = 6
#graph['3']['fin'] = 3
#graph['4'] = {}
#graph['4']['fin'] = 1
#graph['fin'] = None
## cost
#costs={}
#costs['1'] = 5
#costs['2'] = 2
#costs['fin'] = float('inf')
#costs['3'] = float('inf')
#costs['4'] = float('inf')
## parent
#parent={}
#parent['1'] = 'sta'
#parent['2'] = 'sta'
#parent['fin'] = None
#processed = []






# In[4]
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def parent2trace(parent):
    key = 'fin'
    path = ['fin']
    while parent[key] != 'sta':
        path.append(parent[key])
        key = parent[key]
    path.append('sta')
    return path[::-1]
node = find_lowest_cost_node(costs)
#while node is not None:
while node:
#    print(node)
    cost = costs[node]     
    neighbors = graph[node]
    if not neighbors:
#        print(parent)
        break
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost 
            parent[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)   
            
path = parent2trace(parent)
print(path)            
            
            
            
            
            
            
            
            
