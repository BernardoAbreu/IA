
class Node(){
private:
    Point state;
    Node *parent;
    Point action;
    double path_cost;

public:
    Node(state, path_cost, parent=NULL, action=NULL);

    inline bool operator< (const Node& other){ return this.path_cost < other.path_cost; }
    inline bool operator> (const Node& other){ return other < this; }
    inline bool operator<=(const Node& other){ return !(this > other); }
    inline bool operator>=(const Node& other){ return !(this < other); }

    inline bool operator==(const Node& other){ this.state == other.state }
    inline bool operator!=(const Node& other){ return !(this == other); }


    friend std::ostream& operator<<(std::ostream& out, const Node& n);
}