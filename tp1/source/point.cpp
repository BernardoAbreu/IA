#include "point.h"


Point::Point(){
    this->x = 0;
    this->y = 0;
}

Point::Point(int x, int y){
    this->x = x;
    this->y = y;
}

std::ostream& operator<<(std::ostream& out, const Point& p){
    out << p.x << ',' << ' ' << p.y;
    return out;
}