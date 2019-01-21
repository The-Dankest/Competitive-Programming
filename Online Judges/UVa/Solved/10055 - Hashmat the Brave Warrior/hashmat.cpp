#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    unsigned long a, b;
    while (cin >> a >> b) {
        unsigned long c = max(a, b) - min(a, b);
        cout << c << endl;
    }
    return 0;
}