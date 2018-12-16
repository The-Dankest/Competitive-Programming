#include <iostream>
#include <stdio.h>
#include <vector>
#include <stack>

using namespace std;

int main() {

    int n;
    vector<int> answer;
    stack<char> moves;
    
    cin >> n;
    for (int i = 0; i < n - 1; ++i) {
        char c;
        cin >> c;
        moves.push(c);
    }

    int current = n, num_l = 0;
    for (int i = 0; i < n - 1; ++i) {
        char c = moves.top();
        moves.pop();
        if (c == 'L') {
            ++num_l;
        } else {
            for (int j = num_l; j > 0; --j) {
                answer.push_back(current - j);
            }
            answer.push_back(current);
            current -= num_l + 1;
            num_l = 0;
        }
    }
    for (int j = num_l; j > 0; --j) {
        answer.push_back(current - j);
    }
    answer.push_back(current);

    auto ri = answer.rbegin();
    for (int i = i; i < n; ++i) {
        cout << *ri << endl;
        ++ri;
    }

    return 0;
}