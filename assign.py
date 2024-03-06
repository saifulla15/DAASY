import numpy as np
import copy


class Node:
    def __init__(self, parent, cost_matrix, assigned_tasks, worker):
        self.parent = parent
        self.cost_matrix = cost_matrix
        self.assigned_tasks = assigned_tasks
        self.worker = worker
        self.level = 0

    def find_min_cost(self):
        for i in range(len(self.cost_matrix)):
            min_val = min(self.cost_matrix[i])
            if min_val != np.inf:
                self.cost_matrix[i] -= min_val

        for i in range(len(self.cost_matrix[0])):
            min_val = min(self.cost_matrix[:, i])
            if min_val != np.inf:
                self.cost_matrix[:, i] -= min_val

        min_cost = sum(self.cost_matrix[i][j] for i, j in enumerate(
            self.assigned_tasks) if j != -1)
        return min_cost

    def __lt__(self, other):
        return self.level < other.level


def branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    min_cost = np.inf
    min_node = None
    initial_node = Node(None, cost_matrix, [-1] * n, -1)
    queue = [initial_node]

    while queue:
        node = queue.pop(0)

        if node.level == n:
            cost = node.find_min_cost()
            if cost < min_cost:
                min_cost = cost
                min_node = node
            continue

        for i in range(n):
            if i not in node.assigned_tasks:
                new_assigned_tasks = copy.deepcopy(node.assigned_tasks)
                new_assigned_tasks[node.level] = i
                new_cost_matrix = copy.deepcopy(node.cost_matrix)
                new_node = Node(node, new_cost_matrix, new_assigned_tasks, i)
                new_node.level = node.level + 1
                new_cost = new_node.find_min_cost()
                if new_cost < min_cost:
                    queue.append(new_node)

    assignment = [(worker, task)
                  for worker, task in enumerate(min_node.assigned_tasks)]
    return min_cost, assignment


cost_matrix = np.array([[4, 7, 3, 8],
                        [6, 7, 2, 9],
                        [5, 6, 3, 7],
                        [8, 4, 2, 5]])

min_cost, assignment = branch_and_bound(cost_matrix)
print("Minimum cost:", min_cost)
print("Assignment:", assignment)
