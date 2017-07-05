with open('forms.ini', 'rw') as etalon_file, open('forms.inii') as res_file:
    for line in file:
        if 'i' in line:
            res_file.write('{}/n'.format(line))


