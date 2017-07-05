def answer(fn):
    def wraper(a1, a2):
        fn(a1, a2)
    return wraper


def get_FIO(fn):
    def wrap():
        print('Your name: asda, asd ', fn.__name__)
    return wrap

@answer
def name(first, last):
    print('my name is', first, last, )


@get_FIO
def nn():
    return 'a'

print(nn, (nn))

