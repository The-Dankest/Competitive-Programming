#include <iostream>
#include <cstring>

using namespace std;

int main() {

    string s;
    while (getline(cin, s)) {
        for (int i = 0; i < s.length(); ++i) {
            putchar(s[i] - 7);
        }
        putchar('\n');
    }

    return 0;
}