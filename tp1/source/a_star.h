
class AStar : HeuristicSearch{

    void update_frontier(const Node& child, const ExploredSet& explored);

    double heuristic_value(const Node& node);
}

