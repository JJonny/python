class multifilter:
    def __iter__(self):         
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            for ff in self.funcs:    
                if ff(i):
                    self.pos += 1
                else:
                    self.neg += 1
        
            if self.judge(self.pos, self.neg):        
                yield i
        
    def judge_any(pos, neg):
        return pos >= 1

    def judge_half(pos, neg):
        return pos >= neg    

    def judge_all(pos, neg):
        return neg == 0
    
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable                
        self.funcs = funcs
        self.judge = judge
        self.pos = 0
        self.neg = 0    
        
            
def mul2(x):    
    return x % 2 == 0

def mul3(x):    
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0
    
a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

C:\Users\Baranouski_AG\AppData\Local\Programs\Python\Python35-32\Scripts\;C:\Users\Baranouski_AG\AppData\Local\Programs\Python\Python35-32\;C:\Program Files\Microsoft Visual Studio\Common\Tools\WinNT;C:\Program Files\Microsoft Visual Studio\Common\MSDev98\Bin;C:\Program Files\Microsoft Visual Studio\Common\Tools;C:\Program Files\Microsoft Visual Studio\VC98\bin;C:\Program Files (x86)\Microsoft Visual Studio\Common\Tools\WinNT;C:\Program Files (x86)\Microsoft Visual Studio\Common\MSDev98\Bin;C:\Program Files (x86)\Microsoft Visual Studio\Common\Tools;C:\Program Files (x86)\Microsoft Visual Studio\VC98\bin;c:\program files (x86)\devstudio\sharedide\bin\ide;c:\program files (x86)\devstudio\sharedide\bin;c:\program files (x86)\devstudio\vc\bin;c:\SQL11\DLL;c:\SQL11\BIN