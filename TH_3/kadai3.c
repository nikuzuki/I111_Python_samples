// 課題3
// 0番地の数字を足しても昇順を保つ関数を作る

#include <stdio.h>

void print_array(int *array, int len){
  for(int i = 0; i < len; i++){
    printf("%d ", array[i]);
  }
  printf("\n");
}


int* arrangement(int *data, int len, int x){
  data[0] = data[0] + x;
  int tmp = 0;
  for(int i = 0; i < (len-1); i++){
    if(data[i] > data[i+1]){
      tmp = data[i];
      data[i] = data[i+1];
      data[i+1] = tmp;
    }
  }
  return data;
}

int main(void){
  int data[9] = {3, 9, 12, 25, 29, 33, 37, 65, 87};
  int len = sizeof(data) / sizeof(data[0]);
  print_array(data, len);
  int *result = arrangement(data, len, 40);
  print_array(result, len);
}
