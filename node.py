class Node:
    def __init__(self, state, parent, action, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost               # Cost from the start node to this node
        self.h_cost = h_cost               # Heuristic cost to the goal node
        self.cost = g_cost + h_cost        # Total cost for A* (f = g + h)

    def __lt__(self, other):
        return self.cost < other.cost
