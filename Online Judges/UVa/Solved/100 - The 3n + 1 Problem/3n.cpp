#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    
    int a, b, n;
    while (cin >> a >> b) {
        int max_cycle = 0, maxa = max(a, b), mina = min(a, b);
        for (int i = mina; i <= maxa; ++i) {
            n = i;
            int cycles = 1;
            while (n != 1) {
                ++cycles;
                if (n % 2) {
                    n = (n * 3) + 1;
                } else {
                    n /= 2;
                }
            }
            max_cycle = max(max_cycle, cycles);
        }
        cout << a << " " << b << " " << max_cycle << endl;
    }

    return 0;
}