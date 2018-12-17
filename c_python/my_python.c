#include <Python.h>
static Py_object*
spam_system(Py_object *self, Py_object *args)
{

    const char *command;
    int sts;
    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}