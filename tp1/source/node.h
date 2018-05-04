#ifndef NODE_H
#define NODE_H

#include "point.h"


class Node{
private:
    Point state;
    Node *parent;
    double path_cost;

public:
    Point action;

    // default constructor
    Node();

    // destructor
    ~Node();

    // constructors
    Node(const Point& state, double path_cost);
    Node(const Point& state, double path_cost, const Point& action, Node* parent);

    // copy constructor
    Node(const Node&);

    // copy assignment
    Node& operator=( const Node&);

    inline Point get_state() const { return this->state; }
    inline Node* get_parent() const { return this->parent; }
    inline double get_path_cost() const { return this->path_cost; }
    inline bool operator< (const Node& other){ return this->path_cost < other.path_cost; }
    inline bool operator> (const Node& other){ return this->path_cost > other.path_cost; }
    inline bool operator<=(const Node& other){ return this->path_cost <= other.path_cost; }
    inline bool operator>=(const Node& other){ return this->path_cost >= other.path_cost; }

    inline bool operator==(const Node& other){ return this->state == other.state; }
    inline bool operator!=(const Node& other){ return this->state != other.state; }


    friend std::ostream& operator<<(std::ostream& out, const Node& n);
};

#endif