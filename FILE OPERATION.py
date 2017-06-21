import os;
flag = os.access('temp.txt',os.R_OK);
if(flag):
    f = file('temp.txt').read()
    for word in f.split():
        print(word);
else:
    print('FILE NOT FOUND');