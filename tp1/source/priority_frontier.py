from frontier import Frontier
import heapq


class PriorityFrontier(Frontier):
    def insert(self, item):
        heapq.heappush(self.frontier, item)
        self._frontier_hash.add(item)

    def remove(self):
        _, node = heapq.heappop(self.frontier)
        self._frontier_hash.remove(node)
        return node

    # if child.STATE is in frontier with higher PATH-COST
    # then replace frontier node with child
    def replace(self, item):
        for i, (_, node) in enumerate(self.frontier):
            if node.state == item[1].state:
                if node.path_cost > item[1].path_cost:
                    self.frontier[i] = item
                    heapq.heapify(self.frontier)
                break
