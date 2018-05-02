
void AStar::update_frontier(const Node& child, const ExploredSet& explored, Frontier& frontier){
    if(frontier.contains(child.state)){
    	frontier.replace(child)
    }
    else if(!explored.contains(child.state)){
        frontier.insert(child);
    }
}

double AStar::heuristic_value(const Node& node){
    return this.heuristic(node.state, this.problem.goal) + node.path_cost;
}

