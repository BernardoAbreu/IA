#include "ucs.h"


void UCS::init_frontier(int height, int width){
    this->frontier = std::priority_queue<Node>;
    this->init_frontier_hash(height, width);
}

void UCS::replace_insert_frontier(const Node& n){
    for(int i = 0;)
    for i, node in enumerate(self.frontier):
        if node.state == item.state:
            if node.path_cost > item.path_cost:
                self.frontier[i] = item
                heapq.heapify(self.frontier)
            break
}

void UCS::update_frontier(const Node& child){
    if(this->in_frontier(child)){
        // if child.STATE is in frontier with higher PATH-COST
        // then replace frontier node with child
        self._replace_insert_frontier(child);
    }
    else if(!this->in_explored(child)){
        this->insert_frontier(child);
    }
}
