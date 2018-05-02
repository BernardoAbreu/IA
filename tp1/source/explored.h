
class ExploredSet(){
private:
    vector<vector<bool>> visited;

public:

    ExploredSet(std::pair<int, int>&);

    inline bool contains(std::pair<int, int>& key){ return this.visited[key.first][key.second]; }

    inline void add(std::pair<int, int>& key){ this.visited[key.first][key.second] = true; }

    inline void remove(std::pair<int, int>& key){ this.visited[key.first][key.second] = false; }
}
