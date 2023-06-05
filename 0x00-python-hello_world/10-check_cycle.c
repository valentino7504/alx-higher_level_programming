#include "lists.h"
/**
 * check_cycle - checks if a singky linked list is cyclic
 * @list: the head of the list to be checked
 * Return: 0 if not cyclic, or 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *next_node = list;


	while (next_node != NULL)
	{
		next_node = next_node->next;
		if (next_node == list)
			return (1);
	}
	return (0);
}
