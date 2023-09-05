#include "lists.h"
/**
 * insert_node - inserts a new node to a linked list
 * @head: head node
 * @number: number to insert to new node
 * Return: new node otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp = *head;

	/*Allocate memory to newnode and initialize it*/
	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	while (temp->next)
	{
		temp = temp->next;
		if (temp->n == 4)
			break;
	}
	newnode->next = temp->next;
	temp->next = newnode;

	return (temp);
}
