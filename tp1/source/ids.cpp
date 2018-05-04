
void IDS::init_explored(int height, int width){
    this->explored = std::vector<std::vector<double> >(height);
    for(int i = 0; i < height; i++){
        this->explored[i].resize(width, -1.0);
    }

}

void IDS::init_frontier(int height, int width){
    this->frontier = std::stack<Node>();
    this->init_frontier_hash(height, width);
}


void IDS::add_explored(const Node& node){
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

bool IDS::in_explored(const Point& p){
    return this->explored[p.get_x()][p.get_y()] >= 0;
}

void IDS::update_frontier(const Node& child){
    Point state = child.get_state();
    int x = state.get_x();
    int y = state.get_y();

    if(child.get_path_cost() > this->limit){
        this->limit_reached = true;
    }
    else if((this->explored[x][y] > child.get_path_cost()) || !(this->in_explored(state) || this->in_frontier(state))){
        this->insert_frontier(child);
    }
}



std::list<Node> IDS::run(const Problem& problem){
    // Repeatedly depth-limit search till the
    // maximum depth.
    this->limit = 0;

    std::list<Node> result;
    while(true){
        this->limit_reached = false;
        result = this->_run(problem);
        if(!result.empty() || !limit_reached){
            return result;
        }
        this->limit += 0.5;
    }
}
