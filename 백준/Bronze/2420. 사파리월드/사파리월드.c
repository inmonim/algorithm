#include <stdio.h>

int main()
{
  long long a, b;
  scanf("%lld %lld", &a, &b);
  long long ans = a-b;
  if (ans < 0) ans = -ans;
  printf("%lld", ans);
  
  return 0;
}
