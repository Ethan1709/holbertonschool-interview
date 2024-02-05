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
    listint_t *current;
    int i = 1;
    int j, k, l;

    current = *head;

    while (current->next != NULL)
    {
        current = current->next;
        i += 1;
    }

    int newArray[i];
    current = *head;

    for (j = 0; j < i; j++)
    {
        newArray[j] = current->n;

        if (current->next != NULL)
        {
            current = current->next;
        }
    }

    for (int k = 0; k < i; k++)
    {
        printf("%d ", newArray[k]);
    }
    
    for (k = 0, l = i - 1; k < l; k++, l--)
    {
        if (newArray[k] != newArray[l])
        return 0;
    }
    
    return 1;

}
