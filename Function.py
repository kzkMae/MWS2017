#coding:utf-8
#他のプログラムでも共通で使用する関数を格納

import sys
import os.path
import csv
import glob

#エラー終了
def errorEnd(checkErrorNum):
    if not checkErrorNum:
        print '終了します'
        sys.exit()
    return 0


#フォルダの有無をチェック
def isDirCheck(folderName):
    isdirTF = os.path.isdir(folderName)
    if not isdirTF:
        print '\'{}\' is not exist.'.format(folderName)
    return isdirTF


#ファイルの有無をチェック
def isFileCheck(fileName):
    isfileTF = os.path.isfile(fileName)
    if not isfileTF:
        print '\'{}\' is not exist.'.format(fileName)
    return isfileTF


#CSVファイルの読み出し
def readCsvFile(csvFile):
    readList = []
    with open(csvFile, 'rb') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            readList.append(row)
    return readList


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
