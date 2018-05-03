// C++ program to search if a target node is reachable from
// a source with given max depth.
#include<bits/stdc++.h>
#include "point.h"
#include "node.h"
#include "problem.h"
#include "util.h"
#include "explored.h"

using namespace std;

 
// A function to perform a Depth-Limited search
// from given source 'src'
std::list<Node> DLS(const Problem& problem, Node node, float depth, bool& limit_reached, ExploredSet& explored){
    // cout << node << endl;
    explored.add(node.get_state());
    if (problem.goal_test(node.get_state())){
        // cout << "Found"<<endl;
        return solution(&node);
    }
 
    std::list<Node> result;

    // If reached the maximum depth, stop recursing.
    if (depth == 0){
        limit_reached = true;
        return result;
    }
 
    // Recur for all the vertices adjacent to source vertex
    for (auto action : problem.get_actions(node.get_state())){
        // cout << "hello" << endl;
        Node child = child_node(problem, &node, action);
        result = DLS(problem, child, depth-0.5, limit_reached, explored);
        if(!result.empty()){
            break;
        }
    }

    explored.remove(node.get_state());
 
    return result;
}
 
// IDDFS to search if target is reachable from v.
// It uses recursive DFSUtil().
std::list<Node> IDDFS(const Problem& problem){
    // Repeatedly depth-limit search till the
    // maximum depth.
    float depth = 0;
    bool limit_reached;
    std::list<Node> result;
    while(true){
        limit_reached = false;
        cout << "depth: " << depth << endl;
        ExploredSet explored = ExploredSet(problem.get_heigth(), problem.get_width());
        result = DLS(problem, Node(problem.get_initial(), 0.0), depth, limit_reached, explored);
        if(!result.empty() || !limit_reached){
            return result;
        }
        depth += 0.5;
    }
}


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
        v.resize(height);
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
    std::vector<std::vector<char> > map_matrix = read_file_to_vector("../maps/map1.map");
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
    // cout << initial_point << ' ' << goal_point << endl;

    Problem prob = Problem(map_matrix, initial_point, goal_point);

    std::list<Node> v = IDDFS(prob);

    if(!v.empty()){
        cout << v.front() << endl << v.back() << endl << endl;
        for(auto n : v){
            cout << n << ' ';
        }    
    }
    
    cout << endl;

    return 0;
}