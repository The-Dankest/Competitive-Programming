#include <iostream>
#include <algorithm>

using namespace std;

int main() {

    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        unsigned long a, b, c, sum;
        cin >> a >> b >> c;
        sum = a + b + c;
        sum = sum - max(a, max(b, c)) - min(a, min(b, c));
        cout << "Case " << i << ": " << sum << endl;
    }

    return 0;
}