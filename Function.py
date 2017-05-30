#coding:utf-8
#他のプログラムでも共通で使用する関数を格納

import sys
import os.path
import csv
import glob
import shutil



#CSVファイルにリストを書き出し
def writeCsvFilebyList(fileName, writeList):
    if not fileName.endswith('.csv'):
        fileName = '{}.csv'.format(fileName)
    with open(fileName, 'wb') as fcsv:
        csvWrite = csv.writer(fcsv)
        for row in writeList:
            csvWrite.writerow(row)
    return 0


#フォルダ内の特定の拡張子の相対パスとファイル名を取得
def getFilePathName(path, fetc):
    searchName = '{fpath}*{fileEtc}'.format(fpath=path,fileEtc=fetc)
    return glob.glob(searchName)

#ファイル・フォルダの有無検知クラス
class FFBasicError:
    def __init__(self):
        self._eCheck = True
    def _errorEnd(self):
        # チェック用
        print '終了します'
        sys.exit()
    def isDirCheck(self,folderName):
        # フォルダの有無をチェック
        self._eCheck = os.path.isdir(folderName)
        if not self._eCheck:
            print "'{}' is not exist.".format(folderName)
            self._errorEnd()
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


#クラス定義
class OperateJsonFile:
    def __init__(self,name,cfolder,sfolder):
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
    #Jsonファイルをコピー
    def copyJsonFile(self):
        if self._getIsFile():
            shutil.copyfile(self._fpCName,self._dpSName)
    #Jsonファイルを分割するメソッド
    def divisionJsonFile(self):
        if self._getIsFile():
            #Jsonファイル名と同じフォルダを作成
            jName, ext = os.path.split(self.sfolder)

