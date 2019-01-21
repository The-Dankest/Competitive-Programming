#include <iostream>
#include <stdio.h>

using namespace std;

int main() {

    int n;
    scanf("%d\n", &n);

    int max_width = 0, max_height = 0;
    for (int i = 0; i < n; ++i) {
        int x, y, n, m;
        char c;
        scanf("%c %d %d\n", &c, &n, &m);
        x = min(n, m);
        y = max(n, m);
        if (c == '+') {
            max_width = max(x, max_width);
            max_height = max(y, max_height);
        } else {
            if (x >= max_width && y >= max_height) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }

    return 0;
}