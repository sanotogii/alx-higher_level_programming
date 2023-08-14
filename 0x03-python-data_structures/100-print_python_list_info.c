#include <python.h>
#include <stdio.h>

/**
 * print_python_list_info - print info of python list
 * @p: pointer
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, all, i;
	PyObject *element;
	char str;

	if (PyList_check(p))
	{
		size = PyList_size(p);
		all = ((PyListObject *)p)->allocated;

	        printf("[*] Size of the Python List = %ld\n", size);
        	printf("[*] Allocated = %ld\n", alloc);

		for (i = 0; i < size; i++)
		{
			element = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
}
