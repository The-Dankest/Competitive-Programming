#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {

    int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2};
    int dy[] = {-1, 1, -2, 2, -2, 2, -1, 1};

    int width, height, start_x, start_y, end_x, end_y, num_obs;
    cin >> width, height, start_x, start_y, end_x, end_y, num_obs;
    while (width != 0) {

        vector<vector<int>> grid (height + 4, vector<int> (width + 4, 0));
        
        
        cin >> width, height, start_x, start_y, end_x, end_y, num_obs;
    }
    return 0;
}