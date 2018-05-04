#ifndef IDS_H
#define IDS_H


class IDS{

private:
    bool limit_reached;
    double limit;

    std::vector<std::vector<double> > explored;
    std::stack<Node> frontier;

public:

    void init_explored(int height, int width)

    void init_frontier(int height, int width)
    void add_explored(const Node& node);

    bool in_explored(const Point& p);

    void update_frontier(const Node& child);

    std::list<Node> run(const Problem& problem);

};

#endif