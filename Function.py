#coding:utf-8
#他のプログラムでも共通で使用する関数を格納

import sys
import os.path
import csv
import glob
import shutil
import json
import pandas as pd




# #フォルダ内の特定の拡張子の相対パスとファイル名を取得
# def getFilePathName(path, fetc):
#     searchName = '{fpath}*{fileEtc}'.format(fpath=path,fileEtc=fetc)
#     return glob.glob(searchName)

#ファイル・フォルダの有無検知クラス
class FFBasicError:
    def __init__(self):
        self._eCheck = True
    def _errorEnd(self):
        # チェック用
        print '終了します'
        sys.exit()
    def boolDirCheck(self,folderName):
        #True or False
        self._eCheck = os.path.isdir(folderName)
        if not self._eCheck:
            print "'{}' is not exist.".format(folderName)
        return self._eCheck
    def isDirCheck(self,folderName):
        # フォルダの有無をチェック
        self._eCheck = os.path.isdir(folderName)
        if not self._eCheck:
            print "'{}' is not exist.".format(folderName)
            self._errorEnd()
    def boolFileCheck(self,fileName):
        # ファイルの有無をチェック
        self._eCheck = os.path.isfile(fileName)
        if not self._eCheck:
            print "'{}' is not exist.".format(fileName)
        return self._eCheck
    def isFileCheck(self,fileName):
        # ファイルの有無をチェック
        self._eCheck = os.path.isfile(fileName)
        if not self._eCheck:
            print "'{}' is not exist.".format(fileName)
            self._errorEnd()

# CSV操作用のクラス
class RWCsvFile:
    def __init__(self, csvfile):
        self._csvfile = csvfile
    def _readCSVFile(self):
        #CSVファイルの中身をリスト化
        self._readList = []
        with open(self._csvfile, 'rb') as f:
            csvReader = csv.reader(f)
            for row in csvReader:
                self._readList.append(row)
    def getList(self):
        #リストを返却
        self._readCSVFile()
        return self._readList
    def createCSV(self,where='./',data=None):
        self.where = '{}/'.format(where)
        self._writeCSV(data)
    def _writeCSV(self,writelist):
        with open("{path}/{filename}.csv".format(path=self.where,filename=self._csvfile),'wb') as f:
            csvWrite = csv.writer(f)
            if writelist.__len__() == 1:
                csvWrite.writerow(writelist)
            elif writelist.__len__() > 1:
                csvWrite.writerows(writelist)
    def createPDCSV(self, where='./', data=None):
        self.where = '{}/'.format(where)
        self._writeCSVdataframe(data)
    def _writeCSVdataframe(self,writelist):
        writepd = pd.DataFrame(writelist)
        writepd.to_csv("{path}/{filename}.csv".format(path=self.where,filename=self._csvfile),
                       header=False,index=False,sep=",")




# フォルダリストを格納するクラス
class FolderLists:
    def __init__(self, dir):
        self.dir = dir
        self._fflist = os.listdir(dir)
    def getFolderList(self):
        self._folders = [f for f in self._fflist if os.path.isdir(os.path.join(self.dir,f))]
        return  self._folders
    def getFileList(self):
        self._files = [f for f in self._fflist if os.path.isfile(os.path.join(self.dir,f))]
        return self._files

#クラス定義
class OperateJsonFile:
    def __init__(self,name,cfolder="./",sfolder="./"):
        self.name = name
        self._fpCName = '{cfolder}/{name}'.format(cfolder=cfolder,name=name)
        self._dpSName = '{sfolder}/{name}'.format(sfolder=sfolder,name=name)
        self.cfolder = cfolder
        self.sfolder = sfolder
    #ファイルがあるかの確認
    def _getIsFile(self):
        if os.path.isfile(self._fpCName):
            return True
        else:
            print "'{jsonfilename}' is not exist.".format(jsonfilename=self._fpCName)
            return False
    #ファイルの中身の読出し
    def readJsonFile(self):
        jsondata = None
        if self._getIsFile():
            with open(self._fpCName,'r') as f:
                jsondata = json.load(f)
        return jsondata
    #Jsonファイルをコピー
    def copyJsonFile(self):
        if self._getIsFile():
            shutil.copyfile(self._fpCName,self._dpSName)
    #キー毎のファイル作成
    def createKeyNameFile(self,jdata):
        for key in jdata.keys():
            jdata_key = jdata[key]
            newKeyFName = "{folder}/{name}.json".format(folder=self.dpSFName,name=key)
            if not os.path.isfile(newKeyFName):
                with open(newKeyFName, 'w') as f:
                    json.dump(jdata_key, f, indent=4)
        self._writeKeyList(keylist=jdata.keys(),folder=self.dpSFName,name=self.name)
    #Jsonファイルを分割するメソッド
    def divisionJsonFile(self):
        if self._getIsFile():
            #Jsonファイル名と同じフォルダを作成
            jName, ext = os.path.splitext(self.name)
            self.dpSFName = '{sfolder}/{jname}'.format(sfolder=self.sfolder,jname=jName)
            if not os.path.isdir(self.dpSFName):
                os.mkdir(self.dpSFName)
            #jsonファイルの読み込み
            jsondata = self.readJsonFile()
            if jsondata is None:
                print "'{}' is None".format(self.name)
            else:
                #分割処理メソッドへ（今後の）
                self.createKeyNameFile(jsondata)
    #キーリストをファイル化
    def _writeKeyList(self,keylist,folder,name):
        filename = "{}/keys_{}.csv".format(folder,name)
        with open(filename,'wb') as f:
            csvWrite = csv.writer(f)
            for row in keylist:
                csvWrite.writerow([row])
        #print 'a'
    def getKey(self):
        self.jdata = self.readJsonFile()
        self.jkey = self.jdata.keys()
    def hasKey(self,keyname):
        return self.jdata.has_key(keyname)

#Network専用のクラス（OperateJsonFileを継承）
class NetworkJsonFile(OperateJsonFile):
    def getUDP(self):
        self.udp = self.jdata["udp"]
        self._analyzeUDP()
    #UDP情報を整理リスト化
    def _analyzeUDP(self):
        self.udpdatalist = []
        for data in self.udp:
            #print data
            src = '{source}:{sport}'.format(source=data['src'],sport=data['sport'])
            dst = '{dst}:{dport}'.format(dst=data['dst'],dport=data['dport'])
            offset = data['offset']
            udptime = data['time']
            udpdata = [udptime,src,dst,offset]
            self.udpdatalist.append(udpdata)
        #print udpdatalist
        self.udpdatalist.sort()
    def getTCP(self):
        self.tcp = self.jdata["tcp"]
        self._analyzeTCP()
    # TCP情報を整理リスト化
    def _analyzeTCP(self):
        self.tcpdatalist = []
        for data in self.tcp:
            src = '{source}:{sport}'.format(source=data['src'],sport=data['sport'])
            dst = '{dst}:{dport}'.format(dst=data['dst'],dport=data['dport'])
            offset = data['offset']
            tcptime = data['time']
            tcpdata = [tcptime,src,dst,offset]
            self.tcpdatalist.append(tcpdata)
        self.tcpdatalist.sort()
    #host情報整理
    def getHost(self):
        hosts = self.jdata["hosts"]
        hosts.sort()
        return hosts
    #Http情報の整理リスト化
    def getHttp(self):
        self.http = self.jdata["http"]
        self._analyzeHttp()
    def _analyzeHttp(self):
        self.httpdatalist = []
        for data in self.http:
            #print data
            #hdata = data['data']
            #print hdata
            httpdata = [data['count'], data['method'], data['version'], data['host'],
                        data['path'], data['uri']]
            self.httpdatalist.append(httpdata)
        self.httpdatalist.sort(reverse=True)
    #ドメインとIPアドレスの対応
    def getDomain(self):
        domains = self.jdata['domains']
        domaindatalist = []
        for data in domains:
            domaindata =[data['domain'],data['ip']]
            #print domaindata
            domaindatalist.append(domaindata)
        #print 'c'
        domaindatalist.sort()
        return domaindatalist
    #DNS情報を整理リスト化
    def getDNS(self):
        self.dns = self.jdata['dns']
        self._analyzeDNS()
    def _analyzeDNS(self):
        self.dnsdatalist = []
        for data in self.dns:
            dnsdata = [data['request'], '','',data['type']]
            if data['answers'].__len__() == 0:
                dnsdata[1] = 'None'
                dnsdata[2] ='None'
                #print dnsdata
                self.dnsdatalist.append(dnsdata)
            else:
                for ansdata in data['answers']:
                    dnsdata[1] = ansdata['data']
                    dnsdata[2] = ansdata['type']
                    #print dnsdata
                    self.dnsdatalist.append(dnsdata)
            #for ansdata in data['answers']:
        #print 'c'
    # ICMP情報を整理
    def getICMP(self):
        #print 'icmp '
        icmplists = []
        icmpdata = self.jdata["icmp"]
        for a in icmpdata:
            icmplist = [a['src'], a['dst'], a['type'], a['data']]
            icmplists.append(icmplist)
        icmplists.sort()
        return icmplists
    def getHttpEx(self):
        self._analyzeHttpEx(datas='a')
        print 'c'
    def _analyzeHttpEx(self,datas):#作成途中
        print 'd'
    #そのほかにtls,icmp,smtp,mitm,dead_hosts,irc,https_exを作成予定

# behavior情報を処理
class BehaviorJsonFile(OperateJsonFile):
    #Generic情報を整理リスト化
    def getGeneric(self):
        self.generic = self.jdata['generic']
        return self._analyzeGeneric()
    def _analyzeGeneric(self):
        processdatas = []
        processid = []
        #print self.generic
        for exedata in self.generic:
            processdata = [exedata['first_seen'], exedata['process_name'],
                           exedata['pid'], exedata['ppid']]
            processid.append(processdata)
            processsummary = [exedata['first_seen'], exedata['process_name']]
            summarydatas = self._analyzeSummary(summary=exedata['summary'])
            for i in summarydatas:
                for k in i:
                    a = processsummary + k
                    processdatas.append(a)
                #print a
            #print exedata.keys() [u'ppid', u'first_seen', u'process_name', u'pid', u'summary']
            #print processdata
        return processdatas,processid
    #Generic内のSummary情報を整理リスト化
    def _analyzeSummary(self, summary):
        summarydatas = []
        #print summary.keys()
        # [u'regkey_written', u'dll_loaded', u'file_opened', u'regkey_opened', u'mutex', u'guid', u'file_read', u'regkey_read']
        #print summary.__len__()
        #summaryがない場合Return
        if summary.__len__() <= 0:
            #print 'end'
            return []
        for key in summary.keys():
            keydatas = []
            #print key
            for data in summary[key]:
                #print data
                if type(data) == list:
                    keydata = [key, data]
                else:
                    keydata = [key, data.encode('utf8')]
                #print keydata
                keydatas.append(keydata)
            #print keydatas
            summarydatas.append(keydatas)
        #print summarydatas
        #print 'e'
        return summarydatas
    # apistateの情報を整理
    def getAPIstate(self):
        apilists = []
        apistate = self.jdata['apistats']
        keys = apistate.keys()
        for key in keys:
            apistatedata = apistate[key]
            #a = apistatedata.items()
            a = apistatedata.keys()
            #print a
            for i in a:
                apilist = [i, apistatedata[i]]
                #print apilist
                apilists.append(apilist)
        #print apistatedata[key]
        #print apilists
        apilists.sort(key=lambda x: x[1],reverse=True)
        #print apilists
        #print 'c'
        return apilists
    # processtreeの情報を整理リスト化
    def getProcessTree(self):
        self.processtree = self.jdata['processtree']
        deldata, listdata =self._analyzeProcessTree(ptdatas=self.processtree)
        listdata.sort()
        return listdata
    def _analyzeProcessTree(self, ptdatas):
        processtreelists = []
        plist = []
        for ptdata in ptdatas:
            plist.append(ptdata['process_name'])
            processtreelist = [ptdata['first_seen'],ptdata['process_name'],
                               ptdata['pid'],ptdata['ppid'],ptdata['command_line'].encode('utf8')]
            #子プロセスを再帰的に処理
            if ptdata['children'].__len__() > 0:
                childlist, data = self._analyzeProcessTree(ptdatas=ptdata['children'])
                #print data
                processtreelist.append(childlist)
                #print processtreelist
                processtreelists.extend(data)
                #print processtreelists
            else:
                processtreelist.append('child:None')
                #print processtreelist
            processtreelists.append(processtreelist)
            #print 'a', processtreelists
            #processtreelist.sort()
        return plist, processtreelists
    # processの情報を整理リスト化
    def getProcesses(self):
        print'c process'
        self.process = self.jdata['processes']
        for i in self.process:
            #print 'd for'
            self._analyzeProcess(processdata=i)
    def _analyzeProcess(self, processdata):
        print 'e analyze'