#include "lists.h"
/**
 * check_cycle - checks if a singky linked list is cyclic
 * @list: the head of the list to be checked
 * Return: 0 if not cyclic, or 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *slower_node = list, *faster_node = list->next->next;

	while (faster_node->next != NULL && faster_node != NULL)
	{
		slower_node = slower_node->next;
		if (faster_node == slower_node || faster_node == slower_node->next)
			return (1);
	}
	return (0);
}
