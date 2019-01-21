#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;
    for (; n > 0; --n) {

        vector<int> trains;

        int l;
        cin >> l;
        
        for (; l > 0; --l) {
            int x;
            cin >> x;
            trains.push_back(x);
        }

        // find number of swaps
        int swaps = 0;

        if (trains.size() < 2) {
            cout << "Optimal train swapping takes "<< swaps << " swaps." << endl;
            continue;
        }

        bool has_swapped = true;
        while (has_swapped == true) {
            has_swapped = false;
            for (int i = 0; i < trains.size() - 1; ++i) {
                if (trains[i] > trains[i + 1]) {
                    ++swaps;
                    swap(trains[i], trains[i + 1]);
                    has_swapped = true;
                }
            }
        }

        cout << "Optimal train swapping takes "<< swaps << " swaps." << endl;
    }

    return 0;
}