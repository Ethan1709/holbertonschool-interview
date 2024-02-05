#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if the linked list is a palindrome
 * @head: double pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp = *head;
    int *newArray;
    int i = 0;
    int j = 0;
    int k;

    if (head == NULL)
        return 1;

    while (temp)
    {
        temp = temp->next;
        i++;
    }

    newArray = malloc(i * sizeof(listint_t));
    if (newArray == NULL)
        free(newArray);

    i = 0;

    while (*head)
    {
        newArray[i] = (*head)->n;
        *head = (*head)->next;
        i++;
    }

    for (j = 0, k = i - 1; j < k; j++, k--)
    {
        if (newArray[j] != newArray[k])
            return 0;
    }

    return 1;
}
