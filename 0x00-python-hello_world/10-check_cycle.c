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
	listint_t *fast;

	if (list == NULL)
		return (0);
	fast = list->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
