#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head node
 * Return: 1 if palinndrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *top = *head;
	int i, j, n, *list;

	for (i = 0; top != NULL; i++)
		top = top->next;
	list = malloc(sizeof(int) * i);

	top = *head;
	for (j = 0; j < i; j++)
	{
		list[j] = top->n;
		top = top->next;
	}
	n = i - 1;
	for (j = 0; j < i / 2; j++)
	{
		if (list[j] != list[n])
		{
			free(list);
			return (0);
		}
		n--;
	}
	free(list);
	return (1);
}
