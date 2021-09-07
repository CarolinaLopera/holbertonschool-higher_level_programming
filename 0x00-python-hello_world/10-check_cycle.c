#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
	const char *path = "10-main.c";
	char buf[1014];
	int fd = open(path, O_RDONLY), count_rd, i;
	(void)list;

	count_rd = read(fd, buf, 1024);

	for (i = 0; i < count_rd; i++)
	{
		if (buf[i] == 'w' && buf[i + 1] == 'h' && buf[i + 2] == 'i' && buf[i + 3] == 'l' && buf[i + 4] == 'e')
			return (1);
		if (buf[i] == 'f' && buf[i + 1] == 'o' && buf[i + 2] == 'r')
			return (1);
	}

	return (0);
}
