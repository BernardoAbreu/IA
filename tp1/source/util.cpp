#include "util.h"
#include <iostream>
std::list<Node> solution(Node *node){
    std::list<Node> path;
    Node *aux = node;
    // std::cout << *aux << ' ' << *(aux->get_parent()) << std::endl;
    while(aux != NULL){
        path.push_front(*aux);
        aux = aux->get_parent();
        // std::cout << aux->action << std::endl;
        // std::cout << "Parent: " << *aux << std::endl;
    }
    return path;
}


Node child_node(const Problem& problem, Node *parent, Point action){
    return Node(problem.result(parent->get_state(), action),
                parent->get_path_cost() + problem.step_cost(parent->get_state(), action),
                action,
                parent);
}


double manhattan_distance(Point node, Point goal){
    return abs(node.get_x() - goal.get_x()) + abs(node.get_y() - goal.get_y());
}


double octile_distance(Point node, Point goal){
    double dx = abs(node.get_x() - goal.get_x());
    double dy = abs(node.get_y() - goal.get_y());
    return std::max(dx, dy) + 0.5 * std::min(dx, dy);
}
