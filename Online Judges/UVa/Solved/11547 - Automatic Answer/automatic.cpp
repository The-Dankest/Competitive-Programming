#include <iostream>
#include <algorithm>

using namespace std;

int main() {

    int t;
    cin >> t;
    for (; t > 0; --t) {
        long long n;
        cin >> n;
        n = (((((((n * 567) / 9) + 7492) * 235) / 47) - 498) / 10) % 10;
        n = max(n, -1 * n);
        cout << n << endl;
    }
    return 0;
}