#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>
#include <math.h>

int get_sum(int n)
{
    int rem, sum = 0;
    while (n > 0)
    {
        rem = n % 10;
        n = n / 10;
        sum = sum + rem * rem;
    }
    return sum;
}

bool isHappy(int n)
{
    int ns[20], i=0;
    bool status = true;
    bool w_loop = true;
    while (w_loop)
    {
        n = get_sum(n);
        // printf("%d\t", n);
        if (n == 1) {
            break;
        }
        for (int j=0; j<i; j++) {
            if (ns[j] == n) {
                status = false;
                w_loop = false;
                break;
            }
        }
        if (!w_loop) continue;
        ns[i] = n;
        i++;
    }
    // printf("\n");
    return status;
}

int main()
{
    int n = 30;

    bool status;

    status = isHappy(1111111);
    printf("%d\tStatus:\t%d\n", 1111111, status);

    // status = isHappy(19);
    // printf("%d\tStatus:\t%d\n", 19, status);

    // status = isHappy(7);
    // printf("%d\tStatus:\t%d\n", 7, status);

    // status = isHappy(3);
    // printf("%d\tStatus:\t%d\n", 3, status);

    for (int k = 0; k < n; k++)
    {
        printf("Number: %d\t", k);
        status = isHappy(k);
        printf("Status: %d\n", status);
    }
    exit(0);
}