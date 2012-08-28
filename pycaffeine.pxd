
cdef extern from "lib/caffeine/caf/caf_data_deque.h":
    cdef struct caf_deque_s:
        pass

    ctypedef caf_deque_s deque_t

    deque_t* deque_create ()
    int deque_delete_nocb (deque_t* lst)