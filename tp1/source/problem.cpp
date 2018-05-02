#include "problem.h"


Problem::Problem(const vector<vector<char>>& area_map, const Point& initial_state, const Point& goal_state){
    this.map = area_map;
    this.dimensions = pair<int, int>(area_map.size(), area_map[0].size());
    this.initial = initial_state;
    this.goal = goal_state;
}


bool Problem::available(const Point& state, int x, int y){
    int new_x = state.x + x;
    int new_y = state.y + y;

    // Check out of bounds
    if(new_x < 0 || new_x >= this.dimensions.first || new_y < 0 || new_y >= this.dimensions.second) return false;

    // Check if new position is blocked
    if(this.map[new_x][new_y] == '@') return false;

    // Check diagonals
    if (x != 0 && y != 0 (this.map[state.x][new_y] == '@' || this.map[new_x][state.y] == '@')) return false;

    return true;
}

void Problem::get_actions(Point& state, vector<Point>& actions){
    for(int i = 0; i < 8; i++){
        if(this.available(state, directions[0], directions[1])){
            actions.push_back(Point(directions[0], directions[1]));
        }
    }
}
