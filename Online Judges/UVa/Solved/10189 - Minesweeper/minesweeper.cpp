#include <iostream>

using namespace std;

int main() {

    int n = 0, w, h;

    int dx[] = {-1, 0, 1, -1, 1, -1, 0, 1};
    int dy[] = {-1, -1, -1, 0, 0, 1, 1, 1};

    cin >> h >> w;
    while (true) {
        ++n;
        char board[102][102] = {0};

        // get the board and store it
        for (int y = 1; y <= h; ++y) {
            for (int x = 1; x <= w; ++x) {
                char c;
                cin >> c;
                if (c == '*') {
                    board[x][y] = '*';
                }
            }
        }

        // iterate through and update every cell thats not * with the number of * surrounding it
        for (int y = 1; y <= h; ++y) {
            for (int x = 1; x <= w; ++x) {
                if (board[x][y] != '*') {
                    int count = 0;
                    for (int i = 0; i < 8; ++i) {
                        if (board[x + dx[i]][y + dy[i]] == '*') {
                            ++count;
                        }
                    }
                    board[x][y] = '0' + count;
                }
            }
        }

        // print the board
        cout << "Field #" << n << ":" << endl;
        for (int y = 1; y <= h; ++y) {
            for (int x = 1; x <= w; ++x) {
                cout << board[x][y];
            }
            cout << endl;
        }
        cin >> h >> w;
        if (h != 0 && w != 0) {
            cout << endl;
        } else {   
            return 0;
        }
            
    }

}