#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main() {

    int dy[4] = {-1, 1, 0, 0};
    int dx[4] = {0, 0, -1, 1};

    int n, r, c;
    cin >> n;
    string hill_name;

    for (; n > 0; --n) {
        cin >> hill_name >> r >> c;

        int hill[102][102] = {0};
        int dist[102][102] = {0};

        priority_queue<pair<int, pair<int, int> > , vector<pair<int, pair<int, int> > >, greater<pair<int, pair<int, int> > > > next_dist;

        int longest_dist = 0;

        for (int y = 1; y <= r; ++y) {
            for (int x = 1; x <= c; ++x) {
                int h;
                cin >> h;
                pair<int, pair<int, int> > p;
                p.first = h;
                p.second.first = x;
                p.second.second = y;
                next_dist.push(p);
                hill[x][y] = h;
            }
        }

        while (!next_dist.empty()) {
            pair<int, pair<int, int> > p = next_dist.top();
            next_dist.pop();
            int x = p.second.first, y = p.second.second;
            int max_around = 0;
            for (int i = 0; i < 4; ++i) {
                if (hill[x][y] > hill[x + dx[i]][y + dy[i]]) {
                    max_around = max(max_around, dist[x + dx[i]][y + dy[i]]);
                }
            }
            dist[x][y] = max_around + 1;
            longest_dist = max(longest_dist, dist[x][y]);
        }

        // print output
        cout << hill_name << ": " << longest_dist << endl;
    }

}