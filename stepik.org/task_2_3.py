class multifilter:
    c = 0
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        pass

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        pass
        
    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        pass
        
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge        
        
    def __iter__(self):
        # возвращает итератор по результирующей последовательности 
        return self
    
    def __next__(self):
        for f in self.funcs:            
            for i in self.iterable:                       
                if f(i):
                    return i
        else:
            raise StopIteration


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

answer = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
print(1, list(multifilter(a, mul2)))
#assert (list(multifilter(a, mul2)), answer)