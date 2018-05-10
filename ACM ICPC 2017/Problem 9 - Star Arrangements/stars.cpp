#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int n;
    while (cin >> n) {
        cout << n << ":" << endl;
        for (int i = 1; i <= (n / 2); ++i) {
            int row1 = i + 1, row2 = i;
            if (fmod(n, (row1 + row2)) == 0.0f || fmod((n - row1), (row1 + row2)) == 0.0f)
                cout << " " << row1 << "," << row2 << endl;
            if (fmod(n, row1) == 0.0f)
                cout << " " << row1 << "," << row1 << endl;
        }
    }

    return 0;
}