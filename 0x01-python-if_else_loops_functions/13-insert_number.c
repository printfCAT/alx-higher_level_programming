#include <stdlib.h>
#include "lists.h"
/**
* insert_node - inserts a number into a sorted linked list
* @head: head of node
* @number: data to be inserted into node
*
* Return: new node. NULL if unsuccessful
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (new_node->n < *head->n || !*head)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (*head->next)
	{
		if (new_node->n <= (*head->next)->n)
		{
			new_node->next = *head->next;
			*head->next = new_node;
			return (new_node);
		}
		*head = *head->next;
	}
	new_node->next = NULL;
	*head->next = new_node;
	return (new_node);
}
