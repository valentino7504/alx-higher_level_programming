#include "lists.h"
/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: the head of the list
 * @number: the number value of the new node
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *previous_node = NULL, *current_node = NULL;

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (head == NULL || *head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	if (new_node->n < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	previous_node = *head;
	current_node = (*head)->next;
	while (current_node != NULL)
	{
		if (new_node->n <= current_node->n)
		{
			new_node->next = current_node;
			previous_node->next = new_node;
			return (new_node);
		}
		previous_node = previous_node->next;
		current_node = current_node->next;
	}
	new_node->next = current_node;
	previous_node->next = new_node;
	return (new_node);
}
