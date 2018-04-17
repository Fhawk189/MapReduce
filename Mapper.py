# -*- coding: utf-8 -*-
import os
import re
import threading


def map(sourcefile):
    """分割后的小文件进行筛选函数"""
    if not os.path.exists(sourcefile):
        print (sourcefile, 'does not exist')
        return
    pattern = re.compile(r'[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}')
    result = {}
    with open(sourcefile, 'r') as srcfile:
        for dataline in srcfile:
            r = pattern.findall(dataline)
            if r:
                t = result.get(r[0], 0)
                t += 1
                result[r[0]] = t
    desfile = os.path.join(sourcefile[0:-4] + '_map.txt')  # 小文件筛选后的结果
    with open(desfile, 'a') as fp:
        for k, v in result.items():
            fp.write(k + ':' + str(v) + '\n')


if __name__ == '__main__':
    desfolder = 'test'
    files = os.listdir(desfolder)

    def run(i):
        map(desfolder + '\\' + files[i])
    filenumber = len(files)
    for i in range(filenumber):
        t = threading.Thread(target=run, args=(i,))
        t.start()
