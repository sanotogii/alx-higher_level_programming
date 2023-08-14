#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print info of python list
 * @p: pointer
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, all;
	PyObject *element;

	all = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
        printf("[*] Allocated = %ld\n", all);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
	
}
