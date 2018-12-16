#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {

    vector<vector<unsigned long long>> mat (1000000, vector<unsigned long long> (1000000, 1));
    for (int y = 1; y < 1000000; ++y) {
        for (int x = 1; x < 1000000; ++x) {
            mat[y][x] = (mat[y][x - 1] + mat[y -1][x]) % 1000000007;
        }
    }

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {

        int m, n;
        scanf("%d %d", &m, &n);
        printf("%llu\n", mat[m - 1][n - 1]);

    }

    return 0;
}