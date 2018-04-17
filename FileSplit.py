# -*- coding: utf-8 -*-
import os


def filesplit(sourcefile, targetfolder):
    """切分文件函数"""
    if not os.path.isfile(sourcefile):  # 判断文件是否存在
        print (sourcefile, 'does not exist')
        return
    if not os.path.isdir(targetfolder):  # 切分后的文件存放的文件夹
        os.mkdir(targetfolder)
    tempdata = []
    number = 100  # 每个小文件存放100行数据
    filenum = 1  # 小文件编号
    with open(sourcefile, 'r') as srcfile:
        dataline = srcfile.readline().strip()
        while dataline:
            for i in range(number):
                tempdata.append(dataline)
                dataline = srcfile.readline()
                if not dataline:
                    break
            desfile = os.path.join(targetfolder, sourcefile[0:-4] + str(filenum) + '.txt')
            with open(desfile, 'a') as f:
                f.writelines(tempdata)
            tempdata = []
            filenum += 1


if __name__ == '__main__':
    sourcefile = 'test.txt'
    targetfolder = 'test'
    filesplit(sourcefile, targetfolder)
