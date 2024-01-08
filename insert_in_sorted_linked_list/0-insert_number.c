#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode;
    listint_t *newnode2;

    newnode = *head;
    newnode2 = *head;

    newnode = malloc(sizeof(listint_t));
    if (newnode == NULL)
		return (NULL);

    newnode->n = number;

    if (*head == NULL)
    {
        *head = newnode;
        return (newnode);
    }

    if (newnode2->n > number)
    {
        *head = newnode;
        newnode->next = newnode2;
        return (newnode);
    }

    while (newnode2->next->n < number)
    {
        newnode2 = newnode2->next;
    }
    newnode->next = newnode2->next;
    newnode2->next = newnode;
    return (newnode);
}
