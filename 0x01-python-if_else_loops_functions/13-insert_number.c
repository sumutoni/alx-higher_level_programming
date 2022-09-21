#include "lists.h"

/**
 * insert_node - inserts number in a sorted list
 * @head: head of list
 * @number: number to insert
 *
 * Returns: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *cur, *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!head || *head == NULL)
	{
		*head = node;
		return (node);
	}
	if ((*head)->n <= number && (*head)->next == NULL)
	{
		(*head)->next = node;
		return (node);
	}
	if ((*head)->n > number)
	{
		node->next = head;
		*head = node;
		return (node);
	}
	cur = *head;
	prev = NULL;
	while (cur)
	{
		if (curr->n < number)
		{
			prev->next = node;
			node->next = cur;
			return (node);
		}
		prev = cur;
		cur = cur->next;
	}
	prev->next = node;
	return (node);
}
