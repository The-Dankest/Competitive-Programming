#include <cstdio>
#include <iostream>

using namespace std;

int main() {

    int n;
    scanf("%d", &n);
    while (n != 2) {
        int board[20][5][5];
        for (int i = 0; i < 5; ++i) {
            for (int y = 0; y < 5; ++y) {
                scanf("%d %d %d %d %d", &board[i][y][0], &board[i][y][1], &board[i][y][2], &board[i][y][3], &board[i][y][4]);
            }
        }
        int call = 1;
        while (call != 0) {
            scanf("%d", &call);
            for (int i = 0; i < n; ++i) {
                for (int x = 0; x < 5; ++x) {
                    for (int y = 0; y < 5; ++y) {
                        if (board[n][x][y] == call) {
                            board[n][x][y] = 0;
                            // check for bingo!
                            if (board[n][0][1] == 0 && board[n][0][2] == 0 && board[n][0][3] == 0 && board[n][0][4] == 0 && board[n][0][0] == 0) {
                                printf("Card %d wins with a horizontal bingo!\n", n);
                            } else if (board[n][1][1] == 0 && board[n][1][2] == 0 && board[n][1][3] == 0 && board[n][1][4] == 0 && board[n][1][0] == 0) {
                                printf("Card %d wins with a horizontal bingo!\n", n);
                            } else if (board[n][2][1] == 0 && board[n][2][2] == 0 && board[n][2][3] == 0 && board[n][2][4] == 0 && board[n][2][0] == 0) {
                                printf("Card %d wins with a horizontal bingo!\n", n);
                            } else if (board[n][3][1] == 0 && board[n][3][2] == 0 && board[n][3][3] == 0 && board[n][3][4] == 0 && board[n][3][0] == 0) {
                                printf("Card %d wins with a horizontal bingo!\n", n);
                            } else if (board[n][4][1] == 0 && board[n][4][2] == 0 && board[n][4][3] == 0 && board[n][4][4] == 0 && board[n][4][0] == 0) {
                                printf("Card %d wins with a horizontal bingo!\n", n);
                            } else if (board[n][0][0] == 0 && board[n][1][0] == 0 && board[n][2][0] == 0 && board[n][3][0] == 0 && board[n][4][0] == 0) {
                                printf("Card %d wins with a vertical bingo!\n", n);
                            } else if (board[n][0][1] == 0 && board[n][1][1] == 0 && board[n][2][1] == 0 && board[n][3][1] == 0 && board[n][4][1] == 0) {
                                printf("Card %d wins with a vertical bingo!\n", n);
                            } else if (board[n][0][2] == 0 && board[n][1][2] == 0 && board[n][2][2] == 0 && board[n][3][2] == 0 && board[n][4][2] == 0) {
                                printf("Card %d wins with a vertical bingo!\n", n);
                            } else if (board[n][0][3] == 0 && board[n][1][3] == 0 && board[n][2][3] == 0 && board[n][3][3] == 0 && board[n][4][3] == 0) {
                                printf("Card %d wins with a vertical bingo!\n", n);
                            } else if (board[n][0][4] == 0 && board[n][1][4] == 0 && board[n][2][4] == 0 && board[n][3][4] == 0 && board[n][4][4] == 0) {
                                printf("Card %d wins with a vertical bingo!\n", n);
                            } else if (board[n][0][0] == 0 && board[n][1][1] == 0 && board[n][2][2] == 0 && board[n][3][3] == 0 && board[n][4][4] == 0) {
                                printf("Card %d wins with a diagonal bingo!\n", n);
                            } else if (board[n][0][4] == 0 && board[n][1][3] == 0 && board[n][2][2] == 0 && board[n][3][1] == 0 && board[n][4][0] == 0) {
                                printf("Card %d wins with a diagonal bingo!\n", n);
                            }
                        }
                    }
                }
            }

        }
        printf("No winner!");
        scanf("%d", &n);
    }
    return 0;
}