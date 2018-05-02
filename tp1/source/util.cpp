
#include <stdlib.h>
#include "node.h"

void solution(Node *node, std::list<&Node>& path){
    Node *aux = node;

    while(aux != NULL){
        path.push_front(*aux)
        aux = aux->get_parent();
    }
}


Node child_node(const Problem& problem, Node *parent, Point action){
    return Node(problem.result(parent.state, action),
                parent.path_cost + problem.step_cost(parent.state, action),
                parent,
                action);
}


double manhattan_distance(Point node, Point goal){
    return abs(node.x - goal.x) + abs(node.y - goal.y);
}


double octile_distance(Point node, Point goal){
    double dx = abs(node.x - goal.x);
    double dy = abs(node.y - goal.y);
    return max(dx, dy) + 0.5 * min(dx, dy);
}
