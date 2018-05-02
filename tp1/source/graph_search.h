
#define EMPTY 0
#define EXPLORED 1
#define FRONTIER 2


class GraphSearch{
private:
    int expanded_states;

public:
    GraphSearch();

    int get_expanded_states();

    void init_frontier();

    void add_cost(node);

    void update_frontier(child, explored);

    void run__(const Problem& problem, std::list<Node>& path);

    void run(const Problem& problem, std::list<Node>& path);
};
