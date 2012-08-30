from libc.stdlib cimport *
cimport pycaffeine

cdef class CafDeque:
    cdef pycaffeine.deque_t* _c_deque

    def __cinit__(self):
        self._c_deque = pycaffeine.deque_create()

    def __dealloc__(self):
        if self._c_deque is not NULL:
            pycaffeine.deque_delete_nocb(self._c_deque)
            self._c_deque = NULL

    def is_empty(self):
        cdef bint rv
        rv = pycaffeine.deque_empty_list(self._c_deque)
        return (not rv)

    def length(self):
        return pycaffeine.deque_length(self._c_deque)

    def push(self, value):
        local_value = str(value)
        cdef char* charvalue
        charvalue = local_value
        pycaffeine.deque_push(self._c_deque, charvalue)

    def pop(self):
        if self.is_empty():
            return None
        cdef caf_dequen_t* node
        node = pycaffeine.deque_pop(self._c_deque)
        cdef char* value
        value = <char*> node.data
        return value