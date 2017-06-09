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

#network情報について整理
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
        if networkjson.hasKey('udp') and networkjson.jdata['udp'].__len__() > 0:
            #print(networkjson.jkey)
            networkjson.getUDP()
            #print(networkjson.udp)
            #print specimenaname
            #print os.path.basename(os.path.dirname(fileA))
            #print networkjson.udpdatalist.__len__()
            csvwriter = RWCsvFile('udpdata')
            csvwriter.createPDCSV(where=specimenaname,data=networkjson.udpdatalist)
        if networkjson.hasKey('tcp') and networkjson.jdata['tcp'].__len__() > 0:
            networkjson.getTCP()
            #print networkjson.tcp
            csvwriter = RWCsvFile('tcpdata')
            csvwriter.createPDCSV(where=specimenaname, data=networkjson.tcpdatalist)
        if networkjson.hasKey('hosts') and networkjson.jdata['hosts'].__len__() > 0:
            a = networkjson.getHost()
            #print hosts
            csvwriter = RWCsvFile('hostdata')
            csvwriter.createPDCSV(where=specimenaname, data=a)
        if networkjson.hasKey('http') and networkjson.jdata['http'].__len__() > 0:
            networkjson.getHttp()
            csvwriter = RWCsvFile('httpdata')
            csvwriter.createPDCSV(where=specimenaname, data=networkjson.httpdatalist)
        if networkjson.hasKey('domains') and networkjson.jdata['domains'].__len__() > 0:
            #print 'b'
            a = networkjson.getDomain()
            #print a
            csvwriter = RWCsvFile('domainlist')
            csvwriter.createPDCSV(where=specimenaname, data=a)
        if networkjson.hasKey('dns') and networkjson.jdata['dns'].__len__() > 0:
            #print 'b'
            networkjson.getDNS()
            csvwriter = RWCsvFile('dnsdata')
            csvwriter.createPDCSV(where=specimenaname, data=networkjson.dnsdatalist)
        # if networkjson.hasKey('http_ex') and networkjson.jdata['http_ex'].__len__() > 0:
        #     print 'b'
        #     networkjson.getHttpEx()
        if networkjson.hasKey('icmp') and networkjson.jdata['icmp'].__len__() > 0:
            #print 'icmp'
            icmpdata = networkjson.getICMP()
            csvwriter = RWCsvFile('icmpdata')
            csvwriter.createPDCSV(where=specimenaname, data=icmpdata)


    print 'a'

#behavior情報について整理
def readBehaviorJson(directory, folders):
    behaviorjsonlist = isJsonFile(directory=directory, folders=folders, name='behavior')
    if behaviorjsonlist is None:  # 存在するかを確認
        print "network.jsonが１つも存在しません"
        return
    for fileA in behaviorjsonlist:
        # print os.path.basename(fileA)
        specimenaname = os.path.dirname(fileA)
        behaviorjson = BehaviorJsonFile(name='behavior.json', cfolder=specimenaname)
        # test
        print specimenaname
        behaviorjson.getKey()
        # if behaviorjson.hasKey('generic') and behaviorjson.jdata['generic'].__len__() > 0:
        #     #print'b'
        #     #print(networkjson.jkey)
        #     genericdata, genericids = behaviorjson.getGeneric()
        #     #print(networkjson.udp)
        # #     print specimenaname
        # #     print os.path.basename(os.path.dirname(fileA))
        # #     #print networkjson.udpdatalist.__len__()
        #     csvwriter = RWCsvFile('genericdata')
        #     #print genericdata
        #     csvwriter.createPDCSV(where=specimenaname,data=genericdata)
        #     csvwriter = RWCsvFile('genericid')
        #     csvwriter.createPDCSV(where=specimenaname, data=genericids)
        # if behaviorjson.hasKey('apistats') and behaviorjson.jdata['apistats'].__len__() > 0:
        #     print 'b'
        #     apistatedata = behaviorjson.getAPIstate()
        #     csvwriter = RWCsvFile('apistatedata')
        #     csvwriter.createPDCSV(where=specimenaname, data=apistatedata)
        #print behaviorjson.jkey
        # if behaviorjson.hasKey('processtree') and behaviorjson.jdata['processtree'].__len__() > 0:
        #     #print 'b'
        #     procestreedata = behaviorjson.getProcessTree()
        #     csvwriter = RWCsvFile('processtreedata')
        #     csvwriter.createPDCSV(where=specimenaname, data=procestreedata)
        if behaviorjson.hasKey('processes') and behaviorjson.jdata['processes'].__len__() > 0:
            print 'b'
            behaviorjson.getProcesses()

    print 'a'







