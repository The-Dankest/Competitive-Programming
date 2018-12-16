#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>

using namespace std;

int main() {

    int n, m;
    while (cin >> n >> m) {
        vector<vector<int>> island (n, vector<int> (m));
        for (int y = 0; y < n; ++y) {
            for (int x = 0; x < m; ++x) {
                char c;
                cin >> c;
                island[y][x] = (int)c;
            }
        }
        // replace clouds with land if they touch land by doing a dank breadth first search
        int count = 0;
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        int nx, ny;
        queue<pair<int, int>> q;
        for (int y = 0; y < n; ++y) {
            for (int x = 0; x < m; ++x) {
                if (island[y][x] == 'L') {
                    bool inc = true;
                    for (int i = 0; i < 4; ++i) {
                        ny = y + dy[i];
                        nx = x + dx[i];
                        if (ny >= 0 && ny < n && nx >= 0 && nx < m && island[ny][nx] >= 97) {
                            inc = false;
                        }
                    }
                    if (inc) {
                        ++count;
                    }
                    island[y][x] = count + 96;
                    q.push(pair<int, int> (y, x));
                    while (q.size() > 0) {
                        pair<int, int> p = q.front();
                        q.pop();
                        for (int i = 0; i < 4; ++i) {
                            ny = p.first + dy[i];
                            nx = p.second + dx[i];
                            if (ny >= 0 && ny < n && nx >= 0 && nx < m && (island[ny][nx] == 'C' || island[ny][nx] == 'L')) {
                                q.push(pair<int, int> (ny, nx));
                                island[ny][nx] = count + 96;
                            }
                        }
                    }
                }
            }
        }
        printf("%d\n", count);
    }

    return 0;
}