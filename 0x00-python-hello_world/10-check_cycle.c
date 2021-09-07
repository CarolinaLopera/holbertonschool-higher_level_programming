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
	listint_t *aux = list;

	while (list != NULL)
	{
		while (aux != NULL)
		{
			aux = aux->next;
			if ((aux) == (list))
				return (1);
		}
		list = list->next;
	}

	return (0);
}
