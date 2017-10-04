#© Teshan Shanuka J

import os, shutil

##main_folder_name = "soak test"
##try:
##    os.chdir(main_folder_name)
##except FileNotFoundError:
##    print(main_folder_name + 'Not found!')
##    input("press enter to exit")
##    exit()

for dirname, dirnames, filenames in os.walk('.'):
    if len(dirname) != 17 or 'HG1-' not in dirname or ',HG2-' not in dirname:
        print('skipping '+dirname[2:])
        continue
    os.chdir(dirname[2:])
    with open(filenames[0]) as f:
        print('Processing '+dirname[2:])
        fn1,fn2 = dirname[2:].split(',')
        f1, f2 = open(fn1+'.txt', 'w'), open(fn2+'.txt', 'w')
        for line in f:
            if not line:
                continue
            t, tmp1, tmp2 = line.split(',')
            f1.write(t+ ','+ tmp1 +'\n')
            f2.write(t+ ','+ tmp2 +'\n')
    f1.close()
    f2.close()

    os.chdir('..')
    try:
        os.mkdir(fn1)
    except FileExistsError:
        print(fn1+' folder already exists')
        input("press enter to exit")
        exit()
    shutil.move(os.path.join(dirname[2:],fn1+'.txt'), fn1)
    shutil.move(os.path.join(fn1,fn1+'.txt'), os.path.join(fn1,filenames[0]))

    try:
        os.mkdir(fn2)
    except FileExistsError:
        print(fn2+' folder already exists')
        input("press enter to exit")
        exit()
    shutil.move(os.path.join(dirname[2:],fn2+'.txt'), fn2)
    shutil.move(os.path.join(fn2,fn2+'.txt'), os.path.join(fn2,filenames[0]))

input("\nAll done pig :D!")
