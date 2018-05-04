#ifndef HEURISTICSEARCH_H
#define HEURISTICSEARCH_H


#include "graph_search.h"


class HeuristicSearch: GraphSearch{

    HeuristicSearch(const string&);

    double heuristic_value();

    void insert_frontier(const Node& node);

    Node remove_frontier();

    void update_frontier(const Node& child);
};

#endif