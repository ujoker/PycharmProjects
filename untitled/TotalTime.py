import time
from functools import wraps


def fn_timer(fun):
    @wraps(fun)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = fun(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (fun.func_name, str(t1 - t0))
               )
        return result
    return function_timer
