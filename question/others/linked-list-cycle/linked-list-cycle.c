#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 *
 *
 */

struct ListNode
{
    int val;
    struct ListNode *next;
};
int ListLength = 0;

struct ListNode *create(int val)
{
    struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
    node->next = NULL;
    node->val = val;
    // printf("Created with value: %d\n", node->val);
    return node;
}
struct ListNode *insert(struct ListNode *node, int val)
{
    if (!node)
    {
        ListLength++;
        return create(val);
    }
    while (node->next != NULL)
    {
        node = node->next;
    }
    node->next = create(val);
    ListLength++;
    // printf("Inserted with value: %d\n", node->val);
    return node->next;
}

void *print(struct ListNode *node)
{
    while (node != NULL)
    {
        printf("%d ", node->val);
        node = node->next;
    }
    printf("\n");
}

void freeall(struct ListNode *node)
{
    struct ListNode *temp;
    while (node != NULL)
    {
        temp = node;
        node = node->next;
        // printf("Freed with value: %d\n", temp->val);
        free(temp);
        ListLength--;
    }
}

bool hasCycle(struct ListNode *head)
{
    struct ListNode *fast = head;
    struct ListNode *slow = head;
    while (!slow)
    {
        while (!fast)
        {
            printf("%d\t%d\n", slow->val, fast->val);
            if (slow == fast)
                return true;
            fast = fast->next;
        }
        slow = slow->next;
    }
    return false;
}

int main()
{
    struct ListNode *node = NULL;
    struct ListNode *last = NULL;
    // int size = 4;
    // int values[size] = {3, 2, 0, -4};

    int size = 2;
    int values[] = {1, 2};

    // int size = 1;
    // int values[] = {1};

    for (int i = 0; i < size; i++)
    {
        if (!node)
        {
            node = insert(node, values[i]);
            last = node;
        }
        else
        {
            last = insert(last, values[i]);
        }
    }
    // printf("\tLength of list is %d\n", ListLength);

    printf("Status: %d\n", hasCycle(node));

    // printf("\tLength of list is %d\n", ListLength);
    // node = create(12);
    // node->next = create(13);
    // node->next->next = create(156);
    // last = node->next->next;
    // if (!last)
    //     last = create(15);

    print(node);
    freeall(node);
    // printf("\tLength of list is %d\n", ListLength);

    exit(0);
}