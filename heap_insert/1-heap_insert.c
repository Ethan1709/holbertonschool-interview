#include <stdlib.h>
#include <stdio.h>
#include "binary_trees.h"

/**
 * binary_tree_node - creates a binary tree
 * @root: the root ptr
 * @value: value of each node
 *
 * Return: the new node
 */

heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new_node;
    heap_t *new_node2;

    new_node = *root;
    new_node2 = *root;

	new_node = malloc(sizeof(heap_t));
	if (new_node == NULL)
		return (NULL);

    new_node->n = value;
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->parent = NULL;
    
    if (*root == NULL)
    {
        *root = new_node;
        return new_node;
    }

    if (new_node2->n < value)
    {
        *root = new_node;
        new_node->left = new_node2;
        new_node->right = NULL;
        return new_node;
    }

    if (new_node2->n > value)
    {
        new_node2->right = new_node;
        new_node->parent = new_node2;
        new_node->right = NULL;
        new_node->left = NULL;
        return new_node;
    }

    return new_node;
}
