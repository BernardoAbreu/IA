#ifndef PROBLEM_H
#define PROBLEM_H

#include <vector>
#include "point.h"


class Problem{
private:
        std::vector<std::vector<char>> map;
        Point initial;
        Point goal;
        const int directions[8][2] = {{0, -1},
                                    {0, 1},
                                    {-1, 0},
                                    {1, 0},
                                    {-1, -1},
                                    {-1, 1},
                                    {1, -1},
                                    {1, 1},
                                   };

public:

    Problem(const std::vector<std::vector<char>>& area_map, const Point& initial_state, const Point& goal_state);

    inline Point get_initial() const { return this->initial; }

    inline bool goal_test(const Point& state) const{ return this->goal == state; }

    inline Point result(const Point& parent_state, const Point& action) const {return parent_state + action; }

    std::vector<Point> get_actions(const Point&) const;

    double step_cost(const Point& parent_state, const Point& action) const { return (action.get_x() == 0 || action.get_y() == 0)? 1 : 1.5; }
};

#endif