#include "lists.h"

/**
 * len - returns size of list
 * @head: head of list
 *
 * Return: number of elements
 */
int len(listint_t *head)
{
	int count = 0;
	listint_t *cur;

	if (!head)
		return (0);
	cur = head;
	while (cur)
	{
		count++;
		cur = cur->next;
	}
	return (count);
}
/**
 * pal_even - checks if list is palindrome with even elements
 * @head: head of list
 *
 * Return: 1 if yes, 0 if not
 */
int pal_even(listint_t *head)
{
	listint_t *curr;
	int idx = 0, *value, i;

	value = malloc(sizeof(int));
	curr = malloc(sizeof(listint_t *));
	curr = head;
	while (curr->next)
	{
		value[idx] = curr->n;
		idx++;
		if (idx == len(head) / 2)
			break;
		curr = curr->next;
	}
	for (i = (len(head) / 2) - 1; i >= 0; i--)
	{
		curr = curr->next;
		if (curr)
		{
			if (curr->n != value[i])
				return (0);
		}
	}
	free(value);
	return (1);
}
/**
 * pal_odd - checks if list is odd with odd # of elements
 * @head: head of list
 *
 * Return: 1 if yes, 0 if not
 */
int pal_odd(listint_t *head)
{
	int *value, i, idx = 0;
	listint_t *curr;

	if (head->next == NULL)
		return (1);
	value = malloc(sizeof(int) * (len(head) / 2));
	curr = malloc(sizeof(listint_t *));
	curr = head;
	while (curr->next)
	{
		value[idx] = curr->n;
		idx++;
		if (idx == len(head) / 2)
			break;
		curr = curr->next;
	}
	for (i = (len(head) / 2) - 2; i >= 0; i--)
	{
		curr = curr->next;
		if (curr)
		{
			if (curr->n != value[i])
				return (0);
		}
	}
	free(value);
	return (1);
}
/**
 * is_palindrome - checks if list is palindrome
 * @head: pointer to the head of list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{

	if (!head || *head == NULL)
		return (0);
	if (len(*head) % 2 == 0)
		return (pal_even(*head));
	return (pal_odd(*head));
}
