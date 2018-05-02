class Problem{
private:
        vector<vector<char>> map;
        std::pair<int, int> dimensions;
        Point initial;
        Point goal;
        const int directions[][] = {{0, -1},
                                    {0, 1},
                                    {-1, 0},
                                    {1, 0},
                                    {-1, -1},
                                    {-1, 1},
                                    {1, -1},
                                    {1, 1},
                                   }

public:

    Problem(const vector<vector<char>>& area_map, const Point& initial_state, const Point& goal_state);

    inline bool goal_test(const Point& state){ return this.goal == state; }

    bool available(const Point& state, int x, int y);

    void get_actions(Point& state, vector<Point>& actions);

    inline Point result(const Point& parent_state, const Point& action) {return parent_state + action; }

    double step_cost(const Point& parent_state, const Point& action){ return (action.x == 0 or action.y == 0)? 1 : 1.5; }
}
