// 課題2
// 昇順逐次探索法
// 中央値 求めていません！ごめんなさい！
#include <stdio.h>

// find関数
int find(int target, int len, int *data){
  data[len - 1] = target + 1;
  int i = 0;
  while(data[i] < target){
    i++;
  }
  if(target == data[i]){
    return i;
  }else{
    return -1;
  }
}

int main(void){
  int data[10] = {3, 9, 12, 25, 29, 33, 37, 65, 87, -1};
  int len = sizeof(data) / sizeof(data[0]);
  int target = 17;
  int result = find(target, len, data);
  if(result == -1){
    printf("not found\n");
  }else{
    printf("%d is at index %d\n", target, result);
  }

  // 平均値を求める
  double sum = 0;
  for(int i = 0; i < (len-1); i++){
    sum = sum + data[i];
  }
  printf("average : %lf\n", sum / (len-1));

  // 最大値/中央値を求める
  printf("maximum data is %d at address %d\n", data[len-2], len-2);
  printf("minimum data is %d at address %d\n", data[0], 0);
}
