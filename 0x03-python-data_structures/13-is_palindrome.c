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
 * pal_even - checks if list is palindrome with even # of elements
 * @value: array of integers
 * @size: size of list
 *
 * Return: 1 if yes, 0 if not
 */
int pal_even(int *value, int size)
{
	int i, j;

	for (i = 0, j = size - 1; i < size / 2, j >= size / 2; i++, j--)
	{
		if (value[i] != value[j])
		{
			free(value);
			return (0);
		}
	}
	free(value);
	return (1);
}
/**
 * pal_odd - checks if list is odd with odd # of elements
 * @value: array of integers
 * @size: size of list
 *
 * Return: 1 if yes, 0 if not
 */
int pal_odd(int *value, int size)
{
	int i, j;

	for (i = 0, j = size - 1; i <= (size / 2) - 1, j >= size / 2;
		i++, j--)
	{
		if (value[i] != value[j])
		{
			free(value);
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
	int *value, size, i;
	listint_t *cur;

	size = len(*head);
	value = malloc(sizeof(int) * size);
	if (!head || *head == NULL)
	{
		free(value);
		return (0);
	}
	if (size == 0)
	{
		free(value);
		return (1);
	}
	cur = *head;
	i = 0;
	while (cur && i < size)
	{
		value[i] = cur->n;
		i++;
		cur = cur->next;
	}
	if (size % 2 == 0)
		return (pal_even(value, size));
	return (pal_odd(value, size));
}
