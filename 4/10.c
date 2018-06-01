// 2分探索法
#include <stdio.h>

int find(int x, int len, int *s){
  printf("find %d\n", x);
  int left = 0;
  int right = len - 1;
  do{
    int mid = (left+right)/2;
    printf("[%d, %d] mid = %d\n", left, right, mid);
    if(x == s[mid]) return mid;
    if(x < s[mid])  right = mid - 1;
    else left = mid + 1;
  }while(left <= right);

  return -1;

}

int main(void){
  int data[9] = {2, 5, 6, 19, 33, 54, 67, 72, 78};
  int len = sizeof(data) / sizeof(data[0]);
  printf("result = %d\n", find(75, len, data));
  printf("result = %d\n", find(5, len, data));

}
