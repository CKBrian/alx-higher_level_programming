#include <Python.h>
/**
 * print_python_list_info - prints the size and data type of
 * elements in a python list object
 *
 * @p: python list object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, AllocSize, i;
	PyObject *member;

	if (!PyList_Check(p))
		return;
	size = PyList_Size(p);
	AllocSize = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", AllocSize);

	for (i = 0; i < size; i++)
	{
		member = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(member)->tp_name);
	}
}
