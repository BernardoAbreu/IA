#include "graph_search.h"



GraphSearch::GraphSearch(){
    this->expanded_states = 0;
}

void init_explored(int height, int width){
    this->explored = std::vector<std::vector<bool> >(height);
    for(int i = 0; i < height; i++){
        this->explored[i].resize(width, -1.0);
    }

}

void init_frontier(int height, int width){
    this->frontier = std::stack<Node>();
    this->init_frontier_hash(height, width);
}

void init_frontier_hash(int height, int width){
    this->frontier_hash = std::vector<std::vector<bool> >(height);
    for(int i = 0; i < height; i++){
        this->frontier_hash[i].resize(width, false);
    }
}

void insert_frontier(const Node& node){
    this->frontier.push(node);
    Point state = node.get_state();
    this->frontier_hash[state.get_x()][state.get_y()] = true;
}

Node remove_frontier(){
    Node node = this->frontier.top();
    this->frontier.pop();
    Point state = node.get_state();
    this->frontier_hash[state.get_x()][state.get_y()] = false;
    return node;
}

bool in_frontier(const Node& node){
    Point state = node.get_state();
    return this->frontier_hash[state.get_x()][state.get_y()];
}

bool frontier_is_empty(){
    return this->frontier.empty();
}

void add_explored(const Node& node){
    Point state = node.get_state();
    int x = state.get_x();
    int y = state.get_y();
    this->explored[x][y] = true;
}

bool in_explored(const Point& p){
    return this->explored[p.get_x()][p.get_y()];
}

void update_frontier(const Node& child){
    if(!this->in_explored(child) && !this->in_frontier(child)){
        this->insert_frontier(child)
    }
}

std::list<Node> _run(const Problem& problem){
    this->init_explored(problem.get_heigth(), problem.get_width());
    this->init_frontier(problem.get_heigth(), problem.get_width());
    this->insert_frontier(Node(problem.get_initial(), 0.0));

    std::list<Node> result;

    while(true){
        if(this->frontier_is_empty()){
            return result;
        }

        Node node = this->remove_frontier();
        this->expanded_states++;

        if (problem.goal_test(node.get_state())){
            return solution(&node);
        }

        this->add_explored(node);

        for (auto action : problem.get_actions(node.get_state())){
            Node child = child_node(problem, &node, action);
            this->update_frontier(child);
        }
    }

    return result;
}

std::list<Node> run(const Problem& problem){
    return this->run_(problem);
}