#include <stdio.h>

int main() {
    long long n;
    scanf("%lld", &n);
    
    for (long long i=0; i<n; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
}