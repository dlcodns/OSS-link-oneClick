#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int ran;
int count = 0;

void any(int num, char *a)
{
	srand(time(NULL));  
  int temp;
  int ran;
  for (int i=0;i<num-1;i++)
  {
    ran=rand()%(num-i)+i;
    temp=a[i];
    a[i]=a[ran];
    a[ran]=temp;
  }
}

int main(void) {
  int num;
  printf("인원 수(2~8명) = ");
  scanf("%d", &num);
  if(num>8||num<2){
    printf("2~8명만 가능합니다.\n\n");
    main();
  }
  char a[num];
  printf("역할을 정해주세요.\n");
  for(int i=0;i<num;i++){
    printf("제비%d = ", i+1);
    scanf("%s", &a[i]);
    printf("\n");
  }
  
  any(num,&a);
  
  for(int i=0;i<num;i++){
    printf("제비%d 역할: %c",i+1, a[i]);
    printf("\n");
  }
  
  return 0;
}
