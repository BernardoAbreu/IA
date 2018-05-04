#ifndef UCS_H
#define UCS_H

#include <queue>


class UCS: GraphSearch{
private:
    std::priority_queue<Node> frontier;

public:
    void init_frontier(int height, int width);

    void replace_insert_frontier(const Node&);

    void update_frontier(const Node& child);
};


#endif