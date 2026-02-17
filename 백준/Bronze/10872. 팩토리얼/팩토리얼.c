#include <stdio.h>

int main()
{
  short n;
  scanf("%hd", &n);
  long long ans = 1;

  for (short i=2; i <= n; i++) {
    ans *= i;
  }
  printf("%lld", ans);
  return 0;
}
