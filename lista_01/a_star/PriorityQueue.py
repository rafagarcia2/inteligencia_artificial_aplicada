import heapq

class PriorityQueue:
    '''
    Uma Fila ordenada pela prioridade dos itens.
    '''
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def put(self, item_cost, position):
        self.elements.insert(position, item_cost)
        #heapq.heappush(self.elements, (item, cost))
    
    def get(self):
        return heapq.heappop(self.elements)