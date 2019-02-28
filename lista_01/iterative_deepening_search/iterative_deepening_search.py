from node import Node
import sys

def depth_limited_search(problem, limit=50):
    "Algoritmo de pesquisa em profundidade"

    def recursive_dls(node, problem, limit):
        cutoff_occurred = False
        if problem.goal_test(node.state):
            return node
        elif node.depth == limit:
            return -1
        else:
            for successor in node.expand(problem):
                result = recursive_dls(successor, problem, limit)
                if result == -1:
                    cutoff_occurred = True
                elif result != None:
                    return result
        if cutoff_occurred:
            return -1
        else:
            return None
    
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    '''
    Realiza a pesquisa em profundidade até o limite depth.
    '''
    for depth in range(1, 15):
        result = depth_limited_search(problem, depth)
        if result is not -1:
            return result