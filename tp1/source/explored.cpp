#include "explored.h"

ExploredSet::ExploredSet(int height, int width){
    this->visited.resize(height);
    for(int i = 0; i < height; i++){
        this->visited[i].resize(width, false);
        // for(int j = 0; j < width; j++){
        //  this->visited[i].push_back(false);
        // }
    }
}