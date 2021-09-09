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
	listint_t *current, *head_cpy = *head;
	(void)head_cpy;

	if (new == NULL)
	{
		free(new);
		return (NULL);
	}

	if (head == NULL)
	{
		head = new;
		new->next = NULL;
		new->n = number;
	}

	while (head != NULL)
	{
		if ((*head)->next->n > number)
		{
			current = (*head)->next;
			new->n = number;
			new->next = current;
			(*head)->next = new;
			(*head) = head_cpy;
			return (new);
		}
		*head = (*head)->next;
	}
	*head = head_cpy;
	return (NULL);
}
