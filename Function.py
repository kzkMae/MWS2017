#coding:utf-8
#他のプログラムでも共通で使用する関数を格納

import sys
import os.path
import csv
import glob
import shutil
import json



# #CSVファイルにリストを書き出し
# def writeCsvFilebyList(fileName, writeList):
#     if not fileName.endswith('.csv'):
#         fileName = '{}.csv'.format(fileName)
#     with open(fileName, 'wb') as fcsv:
#         csvWrite = csv.writer(fcsv)
#         for row in writeList:
#             csvWrite.writerow(row)
#     return 0


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

class NetworkJsonFile(OperateJsonFile):
    def test(self):
        print 'a'