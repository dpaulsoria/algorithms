from datetime import datetime as dt

def execution_time(function):
    def wrapper(*args, **kwargs):
        initial_time = dt.now()
        x = function(*args, **kwargs)
        final_time = dt.now()
        time_elapsed = final_time - initial_time
        print("t:"+str(time_elapsed.total_seconds())+":seconds")
        return x
    return wrapper

class Sequence:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x