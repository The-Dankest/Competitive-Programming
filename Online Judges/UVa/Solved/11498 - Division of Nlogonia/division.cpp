#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    while (n != 0) {

        int x, y;
        cin >> x >> y;

        for (; n > 0; --n) {

            int a, b;
            cin >> a >> b;

            if (a < x && b < y) {
                cout << "SO" << endl;
            } else if (a > x && b < y) {
                cout << "SE" << endl;
            } else if (a < x && b > y) {
                cout << "NO" << endl;
            } else if (a > x && b > y) {
                cout << "NE" << endl;
            } else {
                cout << "divisa" << endl;
            }

        }
        cin >> n;
    }

    return 0;
}