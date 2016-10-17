#coding:utf-8

import argparse
import os.path
import json

#自作の関数をインポート
from FindFile import errorEnd
from FindFile import isDirCheck
from FindFile import isFileCheck
from FindFile import readCsvFile


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
        fpCName = "{}{}".format(copyFolder,row[0])
        #print fpCName
        if not os.path.isfile(fpCName):
            print '\'{}\' is not exist.'.format(fpCName)
        else:
            #Jsonファイル名と同じフォルダを作成
            jName, ext = os.path.splitext(row[0])
            dpSName = '{}{}'.format(sendFolder,jName)
            #print dpSName
            if not(os.path.isdir(dpSName)):
                os.mkdir(dpSName)

            with open(fpCName, 'r') as f:
                jsonData = json.load(f)
                jsonCreateKeyFile(jsonData,dpSName)
                #print type(jsonData.keys())
    return 0


#エラーチェック用変数
eCheck = 0

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

    # コピー元フォルダを格納
    copyfolder = arguMain.CopyFolder
    eCheck = isDirCheck(copyfolder)
    errorEnd(eCheck)

    # 宛先フォルダを格納
    sendfolder = arguMain.SendFolder
    eCheck = isDirCheck(sendfolder)
    errorEnd(eCheck)

    # CSVファイルを指定
    csvfile = arguMain.CSVFile
    eCheck = isFileCheck(csvfile)
    errorEnd(eCheck)

    # CSVファイルの内容を読み込む（Jsonファイル名リスト）
    readList = readCsvFile(csvfile)
    #Jsonファイル内のキーごとにファイルを分割
    jsonFileDivision(readList,copyfolder, sendfolder)




