#include <stdio.h>
#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

struct Point { ll x, y; };

Point v[100000];

bool compare_xy(Point p, Point q) {
    if (p.y != q.y) return p.y < q.y;
    else return p.x < q.x;
}

ll orientation(Point p, Point q, Point r) {
    return (q.y - p.y)*(r.x - q.x) - (q.x - p.x)*(r.y - q.y);
}

bool compare_radius(Point p, Point q) {
    Point fix = v[0];
    ll val = orientation(fix, p, q);
    if (val) return val > 0;
    else return compare_xy(p,q);
}


int main() {
    stack<Point> s;
    int M;

    scanf("%d", &M);
    for (int i=0; i<M; i++) 
        scanf("%lld%lld", &v[i].x, &v[i].y);

    sort(v, v+M, compare_xy);
    sort(v+1, v+M, compare_radius);

    s.push(v[0]);
    s.push(v[1]);

    Point first, second;
    for (int i=2; i<M; i++) {
        while (s.size() >= 2) {
            second = s.top();
            s.pop();
            first = s.top();
            if(orientation(first, second, v[i]) > 0) {
                s.push(second);
                break;
            }
        }
        s.push(v[i]);
    }

    printf("%d\n", s.size());

    return 0;
}