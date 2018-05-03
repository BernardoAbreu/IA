#ifndef UTIL_H
#define UTIL_H

#include <stdlib.h>
#include <list>
#include <algorithm>
#include "node.h"
#include "problem.h"

std::list<Node> solution(Node *node);

Node child_node(const Problem& problem, Node *parent, Point action);

double manhattan_distance(Point node, Point goal);

double octile_distance(Point node, Point goal);

#endif