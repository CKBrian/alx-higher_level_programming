#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head node
 * Return: 1 if palinndrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *top = *head;
	int i, j, k, *list;

	for (i = 0; top != NULL; i++)
		top = top->next;
	list = malloc(sizeof(int) * i);
	if (list == NULL)
		return (0);

	top = *head;
	for (j = 0; j < i; j++)
	{
		list[j] = top->n;
		top = top->next;
	}
	k = i - 1;
	for (j = 0; j < i / 2; j++)
	{
		if (list[j] != list[k])
		{
			free(list);
			return (0);
		}
		k--;
	}
	free(list);
	return (1);
}
