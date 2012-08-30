from libc.stdlib cimport *
cimport pycaffeine

cdef int search_callback(void* ndata, void* data):
    strndata = str(<char*>ndata)
    strdata = str(<char*>data)
    return cmp(strndata, strdata)

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

    def __len__(self):
        return pycaffeine.deque_length(self._c_deque)

    def __contains__(self, item):
        local_value = str(item)
        cdef char* charvalue
        charvalue = local_value
        cdef void* result
        cdef int (*srch)(void*,void*)
        srch = search_callback
        result = pycaffeine.deque_search(self._c_deque, charvalue, srch)
        return (result is not NULL)

    def __getitem__(self, key):
        cdef void* result
        try:
            idx = int(key)
            result = pycaffeine.deque_get(self._c_deque, idx)
            if result is not NULL:
                return <char*>result
            else:
                raise IndexError
        except ValueError:
            raise Exception("'key' is not an integer")

    def __setitem__(self, key, value):
        cdef char* charvalue
        cdef int result
        try:
            idx = int(key)
            local_value = str(value)
            charvalue = local_value
            result = pycaffeine.deque_set(self._c_deque, idx, charvalue)
            if result is -1:
                raise Exception, "error on item insert (k, v) = (%s, %s)" % (key, value)
        except ValueError:
            raise Exception, "'key' is not an integer"

    # def __delitem__(self, key):

    


 #   def __contains__(self, item):
 #       local_value = str(item)
 #       cdef char* charvalue
 #       charvalue = local_value
 #       cdef int affected_items
 #       affected_items = deque_search_node(self._c_deque, charvalue)
 #       return (affected_items > 0)