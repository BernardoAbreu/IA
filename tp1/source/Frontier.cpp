
class Frontier{
private:
	std::vector<std::vector<bool>> visited;

public:
	Frontier(pair<int, int> dimension);

    void insert(const Node& item);

    Node& remove();

    bool is_empty();

    inline bool contains(const Point& key){ return this.visited[key.first][key.second]; }

    void replace(const Point& state);
}
