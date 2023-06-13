#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the head of the linked list
 * Return: 0 if palindrome, 1 if it is not a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	int *stack, length = 0, i = 0;

	while (current_node != NULL)
	{
		length++;
		current_node = current_node->next;
	}
	stack = malloc(sizeof(int) * length);
	if (length == 0 || stack == NULL)
		return (1);
	current_node = *head;
	while (current_node != NULL)
	{
		stack[i] = current_node->n;
		current_node = current_node->next;
		i++;
	}
	current_node = *head;
	for (i = (length - 1); i >= 0; i--)
	{
		if (stack[i] != current_node->n)
		{
			free(stack);
			return (0);
		}
		current_node = current_node->next;
	}
	free(stack);
	return (1);
}
