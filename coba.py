graph1 = {
    'dosen' : ['TMP','TNT'],
    'TMP' : ['DASPRO', 'ALSRUDAT'],
    'TNT' : ['PSW','PAP'],
    'DASPRO' : ['31TI', '31TK'],
    'ALSRUDAT' : ['31TI', '31TK'],
    'PSW' : ['31TI', '32TI'],
    'PAP' : ['31TI', '32TI'],
    '31TI' : ['SENIN','SELASA'],
    '32TI' : ['SENIN','SELASA'],
    '31TK' : ['SENIN','SELASA']
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited

visited = dfs(graph1,'dosen', [])
print(visited)