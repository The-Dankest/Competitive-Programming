#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {

    int turns = 0;
    stack<char> s;
    string str;
    cin >> str;
    for (int i = 0; i < str.length(); ++i) {
        if (s.size() == 0) {
            s.push(str[i]);
        } else if (s.top() == str[i]) {
            turns += 1;
            s.pop();
        } else {
            s.push(str[i]);
        }
    }

    if (turns % 2 != 0) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}