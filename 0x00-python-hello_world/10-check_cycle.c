#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *s_ptr = list, *f_ptr = list;
	while(s_ptr && f_ptr && f_ptr-> next)
	{
		s_ptr = s_ptr -> next;
		f_ptr = f_ptr -> next -> next;
		if (s_ptr == f_ptr)
		{
			return (1);
		}
	}
	return (0);
}
