#include "explored.h"

Explored::Explored(std::pair<int, int>& dimension){
	for(int i = 0; i < dimension.first; i++){
		for(int j = 0; j < dimension.second; j++){
			this.visited.push_back(0);
		}
	}
}