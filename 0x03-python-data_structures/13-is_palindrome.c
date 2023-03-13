#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* is_palindrome - looks for a palindrome in a singly linked list
* @head: head of the node
*
* Return: 1 if node found. 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *curr = *head;

	if (!*head)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;
	while (slow)
	{
		if (curr->n != slow->n)
			return (0);
		curr = curr->next;
		slow = slow->next;
	}
	return (1);
}
