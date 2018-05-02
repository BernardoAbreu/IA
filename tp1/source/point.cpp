#include "point.h"

Point::Point(int x, int y){
    this.x = x;
    this.y = y;
}

std::ostream& operator<<(std::ostream& out, const Point& n){
    out << this.x << ',' << ' ' << this.y;
    return out;
}