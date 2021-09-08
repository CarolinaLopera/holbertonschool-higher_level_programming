#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		free(new);
		return (NULL);
	}

	while (head != NULL)
	{
		if ((*head)->n > number)
		{
			new->n = number;
			new->next = *head;
			(*head) = new;
			return (new);
		}
		*head = (*head)->next;
	}
	return (NULL);
}
