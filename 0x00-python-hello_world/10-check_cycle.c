#include <stdlib.h>
#include "lists.h"
/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: first node in the linked list
*
* Return: 0 if no cycle found. 1 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return ('\0');
	slow = malloc(sizeof(listint_t));
	fast = malloc(sizeof(listint_t));
	if (!slow || !fast)
		return ('\0');
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	free(slow);
	free(fast);

	return (0);
}
