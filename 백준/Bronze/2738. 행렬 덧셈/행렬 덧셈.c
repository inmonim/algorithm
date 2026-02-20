#include <stdio.h>

int main()
{
  int n, m;
  scanf("%d %d", &n, &m);

  int arr1[n][m];
  int arr2[n][m];

  for (int i=0; i<2; i++) {
    for (int ii=0; ii<n; ii++) {
      for (int iii=0; iii<m; iii++) {
        if (i == 0) {
          scanf("%d", &arr1[ii][iii]);
        } else {
          scanf("%d", &arr2[ii][iii]);
        }
      }
    }
  }

  for (int i=0; i<n; i++) {
    for (int ii=0; ii<m; ii++) {
      int x = arr1[i][ii]+arr2[i][ii];
      printf("%d ", x);
      if (ii == m-1) {
        printf("\n");
      }
    }
  }
  return 0;
}
