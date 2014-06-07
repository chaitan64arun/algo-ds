/**
 * Author : Arun(chaitan64arun@gmail.com)
 */
#include <stdio.h>
#include <stdlib.h>

struct element
{
	int value;
	element *next;
};

typedef element list_elem;
// printer fnction.
int print(list_elem *head) 
{	
	list_elem *current = head;
	while(current != NULL)
	{
		printf("%d\n", current->value);
		current = current->next;
	}

}

int main(int argc, char const *argv[])
{
	list_elem *head, *current;
	head = NULL;

	// making a list of integers from 1 to 10.
	for (int i = 0; i < 10; ++i)
		{
			current = (list_elem*) malloc(sizeof(list_elem));
			current->value = i;
			current->next = head;
			head = current;
		}
	print(head);
	return 0;
}
