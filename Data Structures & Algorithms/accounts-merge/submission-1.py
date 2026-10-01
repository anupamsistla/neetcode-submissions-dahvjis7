from collections import defaultdict
class DisjointSet:
    def __init__(self, n):
        self.parent = [0] * n 
        for i in range(n):
            self.parent[i] = i
        self.size = [1] * n
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionBySize(self, u, v):
        uPar = self.findUPar(u)
        vPar = self.findUPar(v)

        if uPar == vPar:
            return
        
        if self.size[uPar] < self.size[vPar]:
            self.size[vPar] += self.size[uPar]
            self.parent[uPar] = vPar
        
        else:
            self.size[uPar] += self.size[vPar]
            self.parent[vPar] = uPar
        
        return

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DisjointSet(len(accounts))
        emailToAcc = {}
        
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.unionBySize(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroups = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.findUPar(i)
            emailGroups[leader].append(e)
    
        res = []
        for i, e in emailGroups.items():
            res.append([accounts[i][0]] + sorted(e))
        
        return res
        
            
