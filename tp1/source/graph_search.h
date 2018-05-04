#ifndef GRAPHSEARCH_H
#define GRAPHSEARCH_H


#include <list>
#include "point.h"
#include "node.h"
#include "problem.h"


class GraphSearch{
private:
    int expanded_states;
    Problem& problem;
    std::vector<std::vector<double> > explored;
    std::vector<std::vector<bool> > frontier_hash;

public:
    GraphSearch();

    inline int get_expanded_states() { return this.expanded_states; }

    void init_explored(int height, int width);

    void add_explored(const Node& node);

    bool in_explored(const Point& p);


    // Frontier
    void init_frontier(int height, int width);
    void init_frontier_hash(int height, int width);

    void insert_frontier(const Node& node);

    Node remove_frontier();

    bool in_frontier(const Node& node);

    bool frontier_is_empty();


    void update_frontier(const Node& child);

    void run__(const Problem& problem, std::list<Node>& path);

    void run(const Problem& problem, std::list<Node>& path);
};

#endif