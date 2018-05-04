#ifndef ASTAR_H
#define ASTAR_H

#include "heuristic_search.h"


class AStar : HeuristicSearch{

    void update_frontier(const Node& child);

    double heuristic_value(const Node& node);
};

#endif