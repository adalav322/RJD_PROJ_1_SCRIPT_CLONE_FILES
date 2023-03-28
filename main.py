import os
import shutil

inpath = os.getcwd() + '\inputFiles'
outpath = os.getcwd() + '\outputFiles'

"""
create input directory and files
"""
for i in range(10):
    os.makedirs(f'inputFiles\Directory{i}')
    open(f'testfile{i}.txt','w')
    shutil.move(f'testfile{i}.txt', f'inputFiles\Directory{i}')

"""
create output directory and files
"""
for i in range(3):
    os.makedirs(f'outputFiles\Directory{i}')



for rootdirO, dirsO, filesO, in os.walk(outpath):
    for dir in dirsO:
        for rootdir, dirs, files, in os.walk(inpath):
            for file in files:
                if file in next(os.walk(rootdirO + '\\' + dir))[2]:
                    pass
                else:shutil.copy(rootdir + '\\' + file,rootdirO + '\\' + dir)

