cimport pycaffeine

cdef class CafDeque:
    cdef pycaffeine.caf_deque_s* _c_deque

    def __cinit__(self):
        self._c_deque = pycaffeine.deque_create()

    def __dealloc__(self):
        if self._c_deque is not NULL:
            pycaffeine.deque_delete_nocb(self._c_deque)
            self._c_deque = NULL