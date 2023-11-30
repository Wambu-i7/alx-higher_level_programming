#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
	{
		printf("Memory allocation failed");
	}
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL || number < (*head) -> n)
	{
		newNode -> next = *head;
		*head = newNode;
		return (newNode);
	}
	current = *head;
	while (current -> next != NULL && current -> next -> n < number)
	{
		current = current -> next;
	}
	newNode -> next = current -> next;
	current -> next = newNode;
	return (newNode);
}
