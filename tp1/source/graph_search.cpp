#include "graph_search.h"



void Pattern::run__(Problem& problem, std::list<Node>& path){
    this.problem = problem;
    node = Node(problem.initial, 0)

    explored = ExploredSet(problem.get_dimensions());
    frontier = Frontier(problem.get_dimensions());
    frontier.insert(node);
    this.initialize_costs();

    // explored = ExploredSet(problem.get_dimensions())
    // this.costs = np.zeros(problem.dimensions)

    while(true){
        if this._frontier_is_empty():
            return []

        node = frontier.remove();
        this.expanded_states++;

        if problem.goal_test(node.state){
            return solution(node);
        }

        // explored.add(node.state)
        explored.add(node.state);
        this.add_cost(node);

        for(auto action: problem.get_actions(node.state)){
            child = child_node(problem, node, action);
            this.update_frontier(frontier, child);
        }
    }
}

    