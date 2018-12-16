#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {

    int n, ng, nmg;
    cin >> n;

    for (int i = 0; i < n; ++i) {

        cin >> ng >> nmg;

        priority_queue<int, vector<int>, greater<int>> g;
        priority_queue<int, vector<int>, greater<int>> mg;

        for (int j = 0; j < ng; ++j) {
            int x;
            cin >> x;
            g.push(x);
        }
        for (int j = 0; j < nmg; ++j) {
            int x;
            cin >> x;
            mg.push(x);
        }

        while (g.size() > 0 && mg.size() > 0) {
            if (g.top() < mg.top()) {
                g.pop();
            } else {
                mg.pop();
            }
        }

        if (g.size() == 0) {
            cout << "MechaGodzilla" << endl;
        } else {
            cout << "Godzilla" << endl;
        }
    }

    return 0;
}