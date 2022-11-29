#include<stdio.h>
#include<stdlib.h>

int ran;

int any()
{
	srand(time(NULL));
	ran = rand() % 100 + 1;

	return ran;
}
