#coding:utf-8
#各Jsonファイル解析のためのメソッド

import os.path

from Function import *

#存在するJsonファイルのリストを取得（ない場合はNone）
def isJsonFile(directory, folders, name):
    echecker = FFBasicError()
    jsonlist = []
    for folder in folders:
        datafolder = "{ufolder}/{filename}/".format(ufolder=directory,filename=folder)
        if not echecker.boolDirCheck(datafolder):
            print 'c'
            continue
        jsonname = "{folder}{name}.json".format(folder=datafolder,name=name)
        if not echecker.boolFileCheck(jsonname):
            continue
        jsonlist.append(jsonname)
    if jsonlist.__len__() > 0:
        return jsonlist
    else:
        return None


def readNetworkJson(directory, folders):
    networkjsonlist = isJsonFile(directory=directory,folders=folders,name='network')
    #print networkjsonlist
    if networkjsonlist is None:
        print "network.jsonが１つも存在しません"
        return
    for fileA in networkjsonlist:
        print fileA
        print os.path.basename(fileA)
        print os.path.dirname(fileA)


    print 'a'








