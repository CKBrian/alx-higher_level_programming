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

	if (list == NULL || fast->next == NULL)
		return (0);
	while (temp)
	{
		fast = fast->next->next;
		temp = temp->next;
		if (fast == NULL)
			return (0);
		if (fast == temp)
			return (1);

	}
	return (0);
}
