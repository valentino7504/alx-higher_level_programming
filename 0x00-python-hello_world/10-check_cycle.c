#include "lists.h"
/**
 * check_cycle - checks if a singky linked list is cyclic
 * @list: the head of the list to be checked
 * Return: 0 if not cyclic, or 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_node = list;
	listint_t *fast_node = NULL;

	if (slow_node == NULL || slow_node->next == NULL)
		return (0);
	fast_node = (slow_node->next)->next;
	while (fast_node != NULL && fast_node->next != NULL)
	{
		if (fast_node == slow_node || fast_node == slow_node->next)
			return (1);
		slow_node = slow_node->next;
		fast_node = (fast_node->next)->next;
	}
	return (0);
}
