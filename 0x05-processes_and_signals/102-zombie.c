#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - creates infinite while loop
 *
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 *
 * Return: pid
 */

int main(void)
{
	pid_t p;
	int i = 0;

	while (i < 5)
	{
		p = fork();
		if (p > 0)
		{
			printf("Zombie process created, PID: %d\n", p);
			sleep(2);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
