
class BestFirstSearch : HeuristicSearch{

    void update_frontier(const Node& child, const ExploredSet& explored, Frontier& frontier);

    double heuristic_value(const Node& node);
}
