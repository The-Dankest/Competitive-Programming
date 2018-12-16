#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main() {

    int n, k;
    cin >> n >> k;

    int** grid[100][100];

    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            int j = 0;
            if (y < k) {
                cin >> j;
            }
            grid[x][y] = j;
        }
    }


    return 0;
}
