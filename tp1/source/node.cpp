#include "node.h"

Node::Node(Point state, double path_cost, Node *parent=NULL, Point action=NULL){
    this.state = state;
    this.parent = parent;
    this.action = action;
    this.path_cost = path_cost;
}

std::ostream& operator<<(std::ostream& out, const Node& n){
    out << '<' << this.state << ', ' << self.path_cost << '>';
    return out;
}