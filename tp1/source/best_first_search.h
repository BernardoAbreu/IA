#ifndef BESTFIRSTSEARCH_H
#define BESTFIRSTSEARCH_H

class BestFirstSearch : HeuristicSearch{

    double heuristic_value(const Node& node);

    void update_frontier(const Node& child);
};

#endif