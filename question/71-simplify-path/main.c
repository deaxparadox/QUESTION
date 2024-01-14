#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// return array of array
char **separate_by_slash(char *path) { 
}

char *remove_period(char *path, int string_len) {
    char chars[string_len];
}

char* simplifyPath(char* path) {
    printf("%15s\t", path);
    char c_hold, slash = '/', period = '.';
    int period_counter = 0;
    size_t string_len = (int) strlen(path);
    char *path_period_check = remove_period(path, string_len);
    // for (int i=0; i<string_len; i++) {
    //     if (i == 0) {
    //         c_hold = path[i];
    //         continue;
    //     }
    //     if (i == 1) {
    //         return path;
    //     }
    //     if ((path[i] == c_hold) && (path[i] == slash)) {
    //         //  if the consecutive char are slash
    //     }
    //     if ((path[i] == c_hold) && (path[i] == period)) {
    //         //  if the consecutive char are period
    //     }
    // }
    return path;
}
int main() {
    char *paths[3] = {"/home/", "/../", "/home//foo/"};
    for (int i=0; i<3; i++) {
        printf("\tResultant path: %s\n", simplifyPath(paths[i]));
    }
    exit(0);
}