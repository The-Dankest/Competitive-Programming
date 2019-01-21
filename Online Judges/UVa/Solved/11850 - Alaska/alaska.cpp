#include <queue>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    while (n) {
        priority_queue<int, vector<int>, greater<int>> locations;
        string output = "POSSIBLE";
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            locations.push(x);
        }
        int last = 0;
        locations.push(0);
        while (!locations.empty()) {
            locations.pop();
            if (locations.top() - last > 200) {
                output = "IMPOSSIBLE";
            }
            last = locations.top();
        }
        if ((1422 - last) * 2 > 200) {
            output = "IMPOSSIBLE";
        } 
        cout << output << endl;
        cin >> n;
    }

    return 0;
}