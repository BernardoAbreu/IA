

class Point(){
private:
    int x, y;

public:
    Point(int, int);

    inline bool operator==(const Node& other){ return this.x == other.x  && this.y == other.y; }
    inline bool operator!=(const Node& other){ return !(this == other); }

    inline Point operator+(const Point& other) { return Point(this.x + other.x, this.y + other.y); }

    friend std::ostream& operator<<(std::ostream& out, const Point& p);
}