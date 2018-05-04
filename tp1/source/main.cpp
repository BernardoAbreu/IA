// C++ program to search if a target node is reachable from
// a source with given max depth.
#include<bits/stdc++.h>
#include "point.h"
#include "node.h"
#include "problem.h"
#include "util.h"
#include "explored.h"

using namespace std;


class IDS{

private:
    bool limit_reached;
    double limit;
    int expanded_states;

    std::vector<std::vector<double> > explored;
    std::vector<std::vector<bool> > frontier_hash;
    std::stack<Node> frontier;

public:

    IDS(){
        this->expanded_states = 0;
    }

    int get_expanded_states() { return this->expanded_states; };

    void init_explored(int height, int width){
        this->explored = std::vector<std::vector<double> >(height);
        for(int i = 0; i < height; i++){
            this->explored[i].resize(width, -1.0);
        }

    }

    void init_frontier(int height, int width){
        this->frontier = std::stack<Node>();
        this->frontier_hash = std::vector<std::vector<bool> >(height);
        for(int i = 0; i < height; i++){
            this->frontier_hash[i].resize(width, false);
        }
    }

    void insert_frontier(const Node& node){
        this->frontier.push(node);
        Point state = node.get_state();
        this->frontier_hash[state.get_x()][state.get_y()] = true;
    }

    Node remove_frontier(){
        Node node = this->frontier.top();
        this->frontier.pop();
        Point state = node.get_state();
        this->frontier_hash[state.get_x()][state.get_y()] = false;
        return node;
    }

    bool in_frontier(const Point& state){
        return this->frontier_hash[state.get_x()][state.get_y()];
    }

    bool frontier_is_empty(){
        return this->frontier.empty();
    }

    void add_explored(const Node& node){
        Point state = node.get_state();
        int x = state.get_x();
        int y = state.get_y();
        if(this->explored[x][y] != -1.0){
            this->explored[x][y] = std::min(node.get_path_cost(), this->explored[x][y]);
        }
        else{
            this->explored[x][y] = node.get_path_cost();
        }
    }

    bool in_explored(const Point& p){
        return this->explored[p.get_x()][p.get_y()] >= 0;
    }

    void update_frontier(const Node& child){
        Point state = child.get_state();
        int x = state.get_x();
        int y = state.get_y();
        // cout << 1 << endl;
        if(child.get_path_cost() > this->limit){
            this->limit_reached = true;
        }
        else if((this->explored[x][y] > child.get_path_cost()) || !(this->in_explored(state) || this->in_frontier(state))){
            this->insert_frontier(child);
        }
    }


    void print(std::stack<Node> &s){
        if(s.empty()){
            cout << endl;
            return;
        }
        Node x= s.top();
        s.pop();
        print(s);
        s.push(x);
        cout << x << ' ';
    }

    std::list<Node> _run(const Problem& problem){
        this->init_explored(problem.get_heigth(), problem.get_width());
        this->init_frontier(problem.get_heigth(), problem.get_width());
        this->insert_frontier(Node(problem.get_initial(), 0.0));

        std::list<Node> result;

        while(true){
            if(this->frontier_is_empty()){
                // cout << "No" << endl;
                return result;
            }

            Node node = this->remove_frontier();
            this->expanded_states++;

            if (problem.goal_test(node.get_state())){
                return solution(&node);
            }

            this->add_explored(node);


            for (auto action : problem.get_actions(node.get_state())){
                Node child = child_node(problem, &node, action);
                this->update_frontier(child);
            }
        }

    }

    std::list<Node> run(const Problem& problem){
        // Repeatedly depth-limit search till the
        // maximum depth.
        this->limit = 0;

        std::list<Node> result;
        while(true){
            this->limit_reached = false;
            cout << "depth: " << this->limit << endl;
            result = this->_run(problem);
            if(!result.empty() || !limit_reached){
                return result;
            }
            this->limit += 0.5;
        }
    }

};



vector<std::vector<char> > read_file_to_vector(string input_file){
    string line;

    std::vector<std::vector<char> > v;
    int height, width;
    ifstream myfile(input_file.c_str());
    std::stringstream ss;
    if (myfile.is_open()){
        getline(myfile, line);  // First line
        getline(myfile, line, ' '); // height
        getline(myfile, line);
        std::istringstream(line) >> height;
        getline(myfile, line, ' '); // width
        getline(myfile, line);
        std::istringstream(line) >> width;
        getline(myfile, line);  // First line
        v = std::vector<std::vector<char> >(height);
        for(int i=0; getline(myfile, line); i++){
            std::vector<char> v2(width);
            for(int j = 0; j < width; j++){
                v2[j] = line[j];
            }
            v[i] = v2;
        }

        myfile.close();
    }
    else{
        cout << "Unable to open file"; 
    }
    return v;
}


int main(){
    // std::vector<std::vector<char> > map_matrix = read_file_to_vector("../maps/map1.map");
    std::vector<std::vector<char> > map_matrix = read_file_to_vector("../maps/map2.map");
    // std::vector<std::vector<char> > map_matrix = read_file_to_vector("../map4.map");
    // for(int i = 0; i < map_matrix.size(); i++){
    //     for(int j = 0; j < map_matrix[i].size(); j++){
    //         cout << map_matrix[i][j];
    //     }
    //     cout << endl;
    // }

    // Point initial_point = Point(2, 2);
    // Point goal_point = Point(2, 4);
    Point initial_point = Point(21, 133);
    Point goal_point = Point(70, 34);
    // Point initial_point = Point(66, 62);
    // Point goal_point = Point(62, 19);
    cout << initial_point << ' ' << goal_point << endl;

    Problem prob = Problem(map_matrix, initial_point, goal_point);

    std::list<Node> v;
    IDS ids = IDS();
    v = ids.run(prob);

    if(!v.empty()){
        cout << v.front() << endl << v.back() << endl << endl;
        for(auto n : v){
            cout << n << ' ';
        }
        cout << endl;
    }
    else{
        cout << '<' << initial_point << ", 0>" << endl
             << '<' << goal_point << ", inf>" << endl;
    }
    cout << "Expanded states: " << ids.get_expanded_states() << endl;

    return 0;
}