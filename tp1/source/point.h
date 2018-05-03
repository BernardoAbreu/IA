#ifndef POINT_H
#define POINT_H

#include <ostream>

class Point{
private:
    int x, y;

public:
	Point();
    Point(int, int);

    inline int get_x() const { return this->x;}
    inline int get_y() const { return this->y;}

    inline bool operator==(const Point& other) const{ return this->x == other.x  && this->y == other.y; }
    inline bool operator!=(const Point& other) const{ return this->x != other.x  && this->y != other.y;; }

    inline Point operator+(const Point& other) const{ return Point(this->x + other.x, this->y + other.y); }

    friend std::ostream& operator<<(std::ostream& out, const Point& p);
};

#endif