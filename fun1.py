from os import walk


def get_file_names(bin_path):
    with open('d:/snm.txt', 'w') as out_file:
        for d, dirs, files in walk(bin_path):
            print('_')
            for f in files:
                print(f)
                # out_file.write(f + '\n')


def insert_I_file_names(forms_ini_path):
    with open(forms_ini_path) as out_file:
        for line in out_file:
            if '.rtf' in line:
                print(line)

def fun_catcher():
    from msvcrt import getch

    while True:
        l = getch()
        c = ord(getch())
        if c == 13:
            break
        print(c, ' ', l)

ss = '\\\\BSComp800\\SUPPORT\\!VERASSEMBLING_2017\\VER_SEP_ORACLE\\!NEW_VER_IBAN\\BIN\\'
# ss = 'd:\\11_FormsSpecUpdates_backup\\003\\PARITET\\FORMS\\RTF'

# fun_catcher()
# get_file_names(ss)

deps = 0


def before():
    global deps
    deps += 1
    print('bef', deps)
    print(after(deps))


def after(val):
    global deps
    deps += 1
    print('aft', deps)
    if deps < 10:
        before()
    return val


print(before())
