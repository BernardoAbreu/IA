#include "node.h"

Node::Node(const Point& state, double path_cost, const Point& action, Node* parent){
    this->state = state;
    this->parent = parent;
    this->action = action;
    this->path_cost = path_cost;
}

Node::Node(const Point& state, double path_cost, Node* parent){
    this->state = state;
    this->parent = parent;
    this->action = Point(0,0);
    this->path_cost = path_cost;
}

Node::Node(const Point& state, double path_cost){
    this->state = state;
    this->parent = NULL;
    this->action = Point(0,0);
    this->path_cost = path_cost;
}

std::ostream& operator<<(std::ostream& out, const Node& n){
    out << '<' << n.state << ',' << ' ' << n.path_cost << '>';
    return out;
}