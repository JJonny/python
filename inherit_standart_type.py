import time


class Loggable:
    def log(self, msg):
        print('{}: {}'.format(str(time.ctime()), msg))


class MList(list, Loggable):
    def append(self, p_object):
        super(MList, self).append(p_object)
        self.log('Added {}'.format(str(p_object)))


ls = MList([3,4,6])
ls.append(23)
print(ls)
