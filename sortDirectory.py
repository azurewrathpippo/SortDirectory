#coding=utf-8

import os

processedPath = u'I:/Game/有单机流程的游戏'
def getSize(path, mode = 'b'):
    mode = mode.lower()
    if os.path.isfile(path):
        return os.path.getsize(path)
    sz = 0.0
    files = os.listdir(path)
    for f in files:
        curPath = path + '/' + f
        sz += getSize(curPath)

    if mode == 'kb' or mode == 'k':
        sz = sz / 1024.0

    if mode == 'mb' or mode == 'm':
        sz = sz / 1024.0 / 1024.0

    if mode == 'gb' or mode == 'g':
        sz = sz / 1024.0 / 1024.0 / 1024.0

    if mode == 'tb' or mode == 't':
        sz = sz / 1024.0 / 1024.0 / 1024.0 / 1024.0

    return sz

if __name__ == '__main__':
    FileSizeTuple = []
    dirs = os.listdir(processedPath)
    for f in dirs:
        curPath = processedPath + '/' + f
        if os.path.isdir(curPath):
            FileSizeTuple.append((f, getSize(curPath, 'g')))
    FileSizeTuple.sort(key=lambda t:t[1], reverse=True)
    for item in FileSizeTuple:
        print '%s:%.2fGb' % (item[0], item[1])
