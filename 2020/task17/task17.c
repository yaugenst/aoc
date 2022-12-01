#include<stdio.h>

const short input[8][8] = {
    {1, 0, 0, 0, 1, 0, 0, 0},
    {1, 0, 0, 1, 0, 0, 0, 1},
    {0, 0, 1, 1, 1, 0, 0, 1},
    {0, 1, 0, 0, 1, 1, 0, 0},
    {1, 1, 1, 1, 0, 0, 0, 1},
    {1, 1, 1, 1, 1, 1, 0, 0},
    {0, 0, 0, 1, 0, 0, 1, 0},
    {1, 1, 0, 1, 0, 1, 0, 1}
};

int main()
{
    short o, s, i, j, k, x, y, z, n;
    char a0[15][22][22] = {{0}};
    char a1[15][22][22] = {{0}};
    char (*cur)[22][22] = a0;
    char (*next)[22][22] = a1;
    char (*tmp)[22][22];
    for (i = 7; i <= 14; i++) {
        for (j = 7; j <= 14; j++) {
            a0[7][i][j] = input[i-7][j-7];
            a1[7][i][j] = input[i-7][j-7];
        }
    }

    for (s = 0; s < 6; s++) {
        for (i = 1; i < 14; i++) {
            for (j = 1; j < 21; j++) {
                for (k = 1; k < 21; k++) {
                    n = 0;
                    for (x = -1; x <= 1; x++) {
                        for (y = -1; y <= 1; y++) {
                            for (z = -1; z <= 1; z++) {
                                if ((x == 0) & (y == 0) & (z == 0)) {
                                    continue;
                                }
                                n += cur[i+x][j+y][k+z];
                            }
                        }
                    }
                    if (cur[i][j][k] == 0) {
                        next[i][j][k] = n == 3;
                    }
                    else if (cur[i][j][k] == 1) {
                        next[i][j][k] = (n == 2 | n == 3);
                    }
                }
            }
        }
        tmp = cur;
        cur = next;
        next = tmp;
    }

    o = 0;
    for (i = 1; i < 14; i++) {
        for (j = 1; j <= 21; j++) {
            for (k = 1; k <= 21; k++) {
                o += cur[i][j][k];
            }
        }
    }
    printf("%d", o);

    return 0;
}
