#ifndef EXPLORED_H
#define EXPLORED_H

#include <vector>
#include "point.h"

class ExploredSet{
private:
    std::vector<std::vector<bool> > visited;

public:

    ExploredSet(int, int);

    inline bool contains(const Point& key) const{ return this->visited[key.get_x()][key.get_y()]; }

    inline void add(const Point& key){ this->visited[key.get_x()][key.get_y()] = true; }

    inline void remove(const Point& key){ this->visited[key.get_x()][key.get_y()] = false; }
   
};

#endif