
void BestFirstSearch::update_frontier(const Node& child, const ExploredSet& explored, Frontier& frontier){
    if (!(explored.contains(child.state) || frontier.contains(child.state))){
        frontier.insert(child);
    }
}

double BestFirstSearch::heuristic_value(const Node& node){
    return this.heuristic(node.state, this.problem.goal);
}

