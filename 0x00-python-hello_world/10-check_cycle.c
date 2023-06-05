#include "lists.h"
/**
 * check_cycle - checks if a singky linked list is cyclic
 * @list: the head of the list to be checked
 * Return: 0 if not cyclic, or 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *head_node = list;
	listint_t *next_node;

	if (head_node == NULL)
		return (0);
	next_node = head_node->next;
	while (next_node != NULL)
	{
		if (next_node == head_node)
			return (1);
		next_node = next_node->next;
	}
	return (0);
}
