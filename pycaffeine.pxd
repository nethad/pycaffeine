
cdef extern from "lib/caffeine/caf/caf_data_deque.h":
    cdef struct caf_deque_s:
        pass

#    ctypedef caf_deque_s deque_t

    caf_deque_s* deque_create (void)
    int deque_delete_nocb (caf_deque_s* lst)