#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    int n;
    while (cin >> n) {
        int last, current;
        cin >> last;
        if (n == 1) {
            cout << "Jolly" << endl;
            continue;
        }
        vector<int> differences;
        bool jolly = true;
        for (int i = 0; i < n - 1; ++i) {
            cin >> current;
            differences.push_back(abs(last - current));
            last = current;
        }
        sort(differences.begin(), differences.end());
        int diff = 1;
        for (int i = 0;i < differences.size(); ++i) {
            if (differences[i] != diff++) {
                jolly = false;
                break;
            }
        }
        if (jolly) {
            cout << "Jolly" << endl;
        } else {
            cout << "Not jolly" << endl;
        }
    }
    
    return 0;
}