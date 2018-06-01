// ハッシュ法の動くプログラム

#include <stdio.h>

int m = 10;
int htb[10];

int hash(int x){
  return x % m;
}

void add(int x){
  int j = hash(x);
  while(htb[j] != 0)  j = (j + 1) % m;
  htb[j] = x;
}

int find(int x){
  int j = hash(x);
  while(htb[j] != 0){
    if(htb[j] == x) return j;
    j = (j + 1) % m;
  }
  return -1;
}

int main(void){
  // htbの中身を0に初期化
  for(int i = 0; i < m; i++)  htb[i] = 0;

  // ハッシュテーブルにデータを入れる
  add(3); add(23);  add(4); add(19);  add(9);

  // ハッシュテーブルの中身を確認する
  for(int i = 0; i < m; i++)  printf("%d ", htb[i]);
  printf("\n");

  // 検索してみる
  printf("4 is at %d\n", find(4));
  printf("29 is at %d\n", find(29));
  return 0;
}
