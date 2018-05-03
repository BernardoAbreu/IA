#include "problem.h"


Problem::Problem(const std::vector<std::vector<char>>& area_map, const Point& initial_state, const Point& goal_state){
    this->map = area_map;
    this->initial = initial_state;
    this->goal = goal_state;
}


bool available(const Point& state, int x, int y, const std::vector<std::vector<char>>& map){
    int height = map.size();
    int width = map[0].size();
    int new_x = state.get_x() + x;
    int new_y = state.get_y() + y;

    // Check out of bounds
    if(new_x < 0 || new_x >= height|| new_y < 0 || new_y >= width) return false;

    // Check if new position is blocked
    if(map[new_x][new_y] == '@') return false;

    // Check diagonals
    if (x != 0 && y != 0 && (map[state.get_x()][new_y] == '@' || map[new_x][state.get_y()] == '@')) return false;

    return true;
}


std::vector<Point> Problem::get_actions(const Point& state) const{
    std::vector<Point> actions;
    for(int i = 0; i < 8; i++){
        if(available(state, this->directions[i][0], this->directions[i][1], this->map)){
            actions.push_back(Point(this->directions[i][0], this->directions[i][1]));
        }
    }
    return actions;
}
