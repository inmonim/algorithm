#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    size_t cap = (size_t)n * 12 + 1;
    char *out = (char *)malloc(cap);
    if (!out) {
        return 0;
    }
    size_t pos = 0;
    
    for (int i=0; i<n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        pos += (size_t)snprintf(out + pos, cap - pos, "%d\n", a+b);
    }

    fwrite(out, 1, pos, stdout);
    free(out);
    return 0;
}
