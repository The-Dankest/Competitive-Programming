#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cmath>

using namespace std;

int main() {

    int n;
    cin >> n;
    printf("%d:\n", n);
    for (int i = 2; i < n; ++i) {
        if (n % (i + i - 1) == 0 || (n - i) % (i + i - 1) == 0) {
            printf("%d,%d\n", i, i - 1);
        }
        if (n % i == 0) {
            printf("%d,%d\n", i, i);
        }
    }

    return 0;
}