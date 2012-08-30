
cdef extern from "lib/caffeine/caf/caf_data_deque.h":
    cdef struct caf_deque_s:
        pass

    ctypedef caf_deque_s deque_t

    cdef struct caf_deque_node_s:
        caf_deque_node_s* prev
        caf_deque_node_s* next
        void* data

    ctypedef caf_deque_node_s caf_dequen_t

    deque_t* deque_create ()
    int deque_delete_nocb (deque_t* lst)
    bint deque_empty_list (deque_t* lst)
    int deque_length (deque_t* lst)
    deque_t* deque_push (deque_t* lst, void* data)
    caf_dequen_t* deque_pop (deque_t* lst)
    caf_dequen_t* deque_search_node (deque_t* lst, void* data)
    void* deque_search (deque_t* lst, void* data, int (*srch)(void* ndata, void* data))
    void* deque_get (deque_t* lst, int pos)
    int deque_set (deque_t* lst, int pos, void* data)