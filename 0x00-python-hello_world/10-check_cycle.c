#include "lists.h"

/**
 * check_cycle - checks if there is a loop in a linked list
 * @list: head of the list
 *
 * Return: 0 if no loop and 1 if there's a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *second, *third, *current;
	int loop = 0;

	third = NULL;
	second = NULL;
	if (!list || list->next == NULL)
		return (0);
	current = list;
	second = list->next;
	if (second->next != NULL)
	{
		if (second->next->n == current->n)
			return (1);
		third = second->next;
	}
	while (current)
	{
		if (second->next->n == current->n)
			return (1);
		if (third)
		{
			if (third->next->n == current->n || third->next->n == second->n)
			{
				loop = 1;
				return (loop);
			}
		}
		current = second;
		second = third;
		third = third->next;
	}
	return (loop);
}
