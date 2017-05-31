#coding:utf-8

import argparse
import os.path
import json

#自作の関数をインポート
from Function import *


#関数定義
#キーごとにファイルを作成
def jsonCreateKeyFile(jsondata, sendFolder):
    for key in jsondata.keys():
        jsondata_key = jsondata[key]
        newFName = "{}/{}.json".format(sendFolder,key)
        #print newFName
        if not (os.path.isfile(newFName)):
            with open(newFName,'w') as newjf:
                json.dump(jsondata_key, newjf, indent=4)
    return 0

#Jsonファイル内のキーごとに分割
def jsonFileDivision(rowsList, copyFolder, sendFolder):
    for row in rowsList:
        opjfile = OperateJsonFile(name=row[0],cfolder=copyFolder, sfolder=sendfolder)
        opjfile.divisionJsonFile()
    return 0


#引数や-hのオプションを定義
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_ファイル分割',description='オプションと引数の説明',
                                epilog='以上')
    parser.add_argument('-v','--version', action='version', version='%(prog)s version')
    parser.add_argument('CopyFolder',type=str, help='コピー元のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('SendFolder',type=str, help='コピー先のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('CSVFile',type=str, help='探すJsonファイルのリストを格納したCSVファイルを指定, 型：%(type)s，String')

    #引数格納
    arguMain = parser.parse_args()

    #エラー検知用のオブジェクト
    checker = FFBasicError()

    # コピー元フォルダを格納
    copyfolder = arguMain.CopyFolder
    checker.isDirCheck(copyfolder)

    # 宛先フォルダを格納
    sendfolder = arguMain.SendFolder
    checker.isDirCheck(sendfolder)

    # CSVファイルを指定
    csvfile = arguMain.CSVFile
    checker.isFileCheck(csvfile)

    # CSVファイルの内容を読み込む（Jsonファイル名リスト）
    readList = RWCsvFile(csvfile)
    #Jsonファイル内のキーごとにファイルを分割
    jsonFileDivision(readList.getList(),copyfolder, sendfolder)







