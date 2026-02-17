#include <stdio.h>

int main()
{
  short x, y;
  scanf("%hd", &x);scanf("%hd", &y);
  short ans;
  if (x > 0) {
    ans = 1;
  } else {
    ans = 2;
  }
  if (y < 0) {
    if (ans == 2) {
      ans += 1;
    } else {
      ans = 4;
    }
  }
  printf("%hd", ans);
  return 0;
}
