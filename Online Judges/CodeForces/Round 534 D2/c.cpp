#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string str;
    cin >> str;
    bool grid[16][16] = {false};
    for (int i = 0; i < str.length(); ++i) {
        if (str[i] == '0') {
            bool stay = true;
            for (int row = 0; row < 3 && stay; ++row) {
                for (int col = 0; col < 4 && stay; ++col) {
                    if (grid[row][col] == false && grid[row + 1][col] == false) {
                        cout << row + 1 << " " << col + 1 << endl;
                        grid[row][col] = true;
                        grid[row + 1][col] = true;
                        if (grid[row][0] == true && grid[row][1] == true && grid[row][2] == true && grid[row][3] == true) {
                            grid[row][0] = grid[row][1] = grid[row][2] = grid[row][3] = false;
                        }
                        ++row;
                        if (grid[row][0] == true && grid[row][1] == true && grid[row][2] == true && grid[row][3] == true) {
                            grid[row][0] = grid[row][1] = grid[row][2] = grid[row][3] = false;
                        }
                        --row;
                        if (grid[0][col] == true && grid[1][col] == true && grid[2][col] == true && grid[3][col] == true) {
                            grid[0][col] = grid[1][col] = grid[2][col] = grid[3][col] = false;
                        }
                        stay = false;
                    }
                }
            }
        } else {
            bool stay = true;
            for (int row = 0; row < 4 && stay; ++row) {
                for (int col = 0; col < 3 && stay; ++col) {
                    if (grid[row][col] == false && grid[row][col + 1] == false) {
                        cout << row + 1 << " " << col + 1 << endl;
                        grid[row][col] = true;
                        grid[row][col + 1] = true;
                        if (grid[0][col] == true && grid[1][col] == true && grid[2][col] == true && grid[3][col] == true) {
                            grid[0][col] = grid[1][col] = grid[2][col] = grid[3][col] = false;
                        }
                        ++col;
                        if (grid[0][col] == true && grid[1][col] == true && grid[2][col] == true && grid[3][col] == true) {
                            grid[0][col] = grid[1][col] = grid[2][col] = grid[3][col] = false;
                        }
                        --col;
                        if (grid[row][0] == true && grid[row][1] == true && grid[row][2] == true && grid[row][3] == true) {
                            grid[row][0] = grid[row][1] = grid[row][2] = grid[row][3] = false;
                        }
                        stay = false;
                    }
                }
            }
        }
    } 

    return 0;
}