#include "lists.h"
/**
 * check_cycle - check of a cyclic linked list
 * @list: linked list
 * Return: 1 if cyclic else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list, *temp = list;

	while (temp)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
		else if (fast == NULL)
			return (0);
		temp = temp->next;

	}
	return (2);
}
