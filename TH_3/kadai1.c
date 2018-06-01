// 課題1
// 逐次探索法
// 中央値 求めていません！ごめんなさい！

#include <stdio.h>

// 関数find
int find(int target, int len, int *data){

  for(int i = 0; i < len; i++){
    if(data[i] == target){
      return i;
    }
  }
  return -1;
}

int main(void){
  int data[9] = {37, 12, 25, 9, 87, 33, 65, 3, 29};
  int len = sizeof(data) / sizeof(data[0]);
  int target = 87;
  int result = find(target, len, data);
  if(result == -1){
    printf("not found\n");
  }else{
    printf("%d is at index %d\n", target, result);
  }

  // 平均値を求める
  double sum = 0;
  for(int i = 0; i < len; i++){
    sum = sum + data[i];
  }
  printf("average : %lf\n", sum/(double)len);

  // 最大値/最小値を求める
  int max_value = data[0];
  int min_value = data[0];
  int max_index = 0;
  int min_index = 0;
  for(int i = 1; i < len; i++){
    if(max_value < data[i]){
      max_value = data[i];
      max_index = i;
    }
    if(min_value > data[i]){
      min_value = data[i];
      min_index = i;
    }
  }
  printf("maximum data is %d at address %d\n", max_value, max_index);
  printf("minimum data is %d at address %d\n", min_value, min_index);

  return 0;
}
