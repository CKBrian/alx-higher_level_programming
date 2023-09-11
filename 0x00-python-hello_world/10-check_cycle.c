#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check of a cyclic linked list
 * @list: linked list
 * Return: 1 if cyclic else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *temp = list;

	while (temp != NULL && fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = temp->next;
		if (fast == temp)
			return (1);

	}
	return (0);
}
