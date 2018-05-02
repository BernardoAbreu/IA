
#define EMPTY 0
#define EXPLORED 1
#define FRONTIER 2


class GraphSearch{
private:
    int expanded_states;
    Problem& problem;

public:
    GraphSearch();

    inline int get_expanded_states() { return this.expanded_states; }

    void init_frontier();

    void add_cost(const Node& node);

    void update_frontier(const Node& child, const ExploredSet& explored, Frontier& frontier);

    void run__(const Problem& problem, std::list<Node>& path);

    void run(const Problem& problem, std::list<Node>& path);
};
