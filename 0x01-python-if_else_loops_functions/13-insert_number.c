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
	listint_t *new_node, *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!*head || new_node->n < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (temp->next)
	{
		if (new_node->n <= (temp->next)->n)
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	new_node->next = NULL;
	temp->next = new_node;
	return (new_node);
}
