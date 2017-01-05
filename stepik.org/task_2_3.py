class multifilter:
    def __iter__(self):        
        return self
        
    def __init__(self, iterable, *funcs):
        self.iterable = iterable        
        self.counter = -1
        self.funcs = funcs
            
    def judge_any(pos, neg):
        pass
        
    def __next__(self):
        for ff in self.funcs:
            if self.counter == len(self.iterable)-1:
                raise StopIteration
            else:
                self.counter += 1
                return_value = ff(self.iterable[self.counter])
                if return_value != None:
                    return return_value
                else:
                    continue
            
def mul2(x):
    if x % 2 == 0:
        return x
    
a = [i for i in range(1, 10)]

print(list(multifilter(a, mul2)))