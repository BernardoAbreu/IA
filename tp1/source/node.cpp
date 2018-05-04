#include "node.h"
#include <iostream>
Node::Node(const Point& state, double path_cost, const Point& action, Node* parent){
    this->state = state;

    if(parent == NULL){
        this->parent = NULL;
    }
    else{
        this->parent = new Node();
        *(this->parent) = *(parent);
    }

    this->action = action;
    // std::cout << action << ' ' << this->action << std::endl;
    this->path_cost = path_cost;
    // std::cout << state << ' ' << *(this->parent) << std::endl;
}

Node::Node(const Point& state, double path_cost){
    this->state = state;
    this->parent = NULL;
    this->action = Point(0,0);
    this->path_cost = path_cost;
}


Node::Node(){
    this->state = Point(0, 0);
    this->parent = NULL;
    this->action = Point(0,0);
    this->path_cost = 0.0;
}

Node::~Node(){
    if(this->parent != NULL){
        delete this->parent;
    }
}

Node::Node(const Node& n){
    this->state = n.state;
    // std::cout << "Hellooo" << std::endl;

    if(n.parent == NULL){
        this->parent = NULL;
    }
    else{
        // std::cout << *(n.parent) << std::endl;
        // std::cout << "K" << std::endl;
        this->parent = new Node();
        *(this->parent) = *(n.parent);
    }
    this->action = n.action;
    this->path_cost = n.path_cost;
}

Node& Node::operator=( const Node& rhs ){
    if(this == &rhs){
        return *this;
    }

    if(this->parent != NULL){
        delete this->parent;
    }

    this->state = rhs.state;
    if(rhs.parent == NULL){
        this->parent = NULL;
    }
    else{
        this->parent = new Node();
        *(this->parent) = *(rhs.parent);
    }
    this->action = rhs.action;
    this->path_cost = rhs.path_cost;
    return *this;
}

std::ostream& operator<<(std::ostream& out, const Node& n){
    out << '<' << n.state << ',' << ' ' << n.path_cost << '>';
    return out;
}