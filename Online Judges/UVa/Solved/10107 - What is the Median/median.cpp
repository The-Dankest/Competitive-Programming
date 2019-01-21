#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int main() {
    
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> big;

    int i;
    cin >> i;
    while (cin) {
        if (big.empty()) {
            big.push(i);
        } else {
            if (big.size() == small.size()) {
                big.push(i);
            } else {
                small.push(i);
            }
            int x = big.top(), y = small.top();
            if (y > x) {
                big.pop();
                small.pop();
                big.push(y);
                small.push(x);
                x = big.top();
                y = small.top();       
            }
            if (big.size() == small.size()) {
                i = (x + y) / 2;
            } else {
                i = (x < y) ? y : x;
            }
        }

        cout << i << endl;
        cin >> i;
    }

}