class multifilter:
    def __iter__(self): 
        for ff in self.funcs:
            for i in self.iterable:
                if ff(i):
                    yield i
        
        
    def __init__(self, iterable, *funcs):
        self.iterable = iterable        
        self.counter = -1
        self.funcs = funcs
            
    def judge_any(pos, neg):
        pass
        
    #def __next__(self):
        
            
def mul2(x):    
    return x % 2 == 0

def mul3(x):    
    return x % 3 == 0
    
a = [i for i in range(1, 10)]

print(list(multifilter(a, mul2, mul3)))