#include <stdio.h>
#include <stdlib.h>

int climbing(int *number) {
    if (*number == 1) {
        return 1;
    }
    *number = *number - 1;
    climbing(number);
    return 1;
}


int *used[45];
int climbStairs(int n) {
    if(n==0){return 1;}
    if(n==1){return 1;}
    int fst=1, scd=1, ans;
    for(int i=2; i<=n; i++){
        ans=fst+scd;
        fst=scd; scd=ans;
        printf("%d\t%d\t%d\n", fst, scd, ans);
    }
    return ans; 
}

int main() {
    printf("%d\n", climbStairs(3));
    exit(0);
}