# -*- coding: utf-8 -*-
import os


def redu(sourcefolder, targetfile):
    """整合小文件的筛选结果"""
    if not os.path.isdir(sourcefolder):
        print (sourcefolder, 'does not exist')
        return
    result = {}
    allfiles = [sourcefolder + '\\' + f for f in os.listdir(sourcefolder) if f.endswith('_map.txt')]
    for f in allfiles:
        with open(f, 'r') as fp:
            for line in fp:
                line = line.strip()
                if not line:
                    continue
                position = line.index(':')
                key = line[0:position]
                value = int(line[position+1:])
                result[key] = result.get(key, 0) + value
    with open(targetfile, 'w') as fp:
        for k, v in result.items():
            fp.write(k + ':' + str(v) + '\n')


if __name__ == '__main__':
    redu('test', 'test\\result.txt')