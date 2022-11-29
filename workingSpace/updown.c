#include<stdio.h>
#include<stdlib.h>

int ran;
int count = 0;

int any()
{
	srand(time(NULL));
	ran = rand() % 100 + 1;

	return ran;
}

int main(void)
{
	int num;
	ran = any();
	//printf("%d", ran);
	
	while(1){
		num = 0;

		printf("숫자 하나를 적으세요. = ");
		scanf_s("%d", &num);

		if (ran > num) {
			if (count != 5) {
				printf("up!\n");
			}

		}
		else if (ran == num) {
			printf("딩동댕~ 정답!\n");
				break;
		}
		else if (ran < num) {
			if (count != 5) {
				printf("down!\n");
			}
			
		}
		count += 1;
		if (count == 6) {
			printf("\n정답은 %d 였습니다~ 메롱 ㅋㅋㄹㅃㅃ", ran);
				break;
		}
	}
	return 0;
}
