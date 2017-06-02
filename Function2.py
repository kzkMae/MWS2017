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
    #存在するnetwork.jsonファイルのリストを取得
    networkjsonlist = isJsonFile(directory=directory,folders=folders,name='network')
    if networkjsonlist is None: #存在するかを確認
        print "network.jsonが１つも存在しません"
        return
    for fileA in networkjsonlist:
        #print os.path.basename(fileA)
        specimenaname = os.path.dirname(fileA)
        networkjson = NetworkJsonFile(name='network.json',cfolder=specimenaname)
        #test
        networkjson.getKey()
        if networkjson.hasKey('udp'):
            #print(networkjson.jkey)
            networkjson.getUDP(networkjson.jdata)
            #print(networkjson.udp)
            print specimenaname
            print os.path.basename(os.path.dirname(fileA))
            #print networkjson.udpdatalist.__len__()
            csvwriter = RWCsvFile('udpdata')
            csvwriter.createPDCSV(where=specimenaname,data=networkjson.udpdatalist)


    print 'a'








