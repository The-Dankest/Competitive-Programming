#include <iostream>

using namespace std;

int main() {
    bool toggle = true;
    char c;
    while (cin.get(c)) {
        if (c == 34) {
            toggle = !toggle;
            if (toggle == true) {
                cout << "''";
            } else {
                cout << "``";
            }
        } else {
            cout << c;
        }
    }
    return 0;
}