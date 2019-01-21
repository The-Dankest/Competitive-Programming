#include <iostream>

using namespace std;

long long f91(long long n) {
    if (n > 100) { return n - 10; }
    return f91(f91(n + 11));
}

int main() {

    long long n;
    cin >> n;
    while (n != 0) {
        cout << "f91(" << n << ") = " << f91(n) << endl;
        cin >> n;
    }

    return 0;
}