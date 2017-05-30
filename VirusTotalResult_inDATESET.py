#coding:utf-8

import argparse
import json
import os.path


#自作の関数をインポート


#関数定義
from Function import *


#エラーチェック用変数
eCheck = 0

#定数
STRING_NONE = 'None'
STRING_UNKNOWN = 'Unknown'

#Jsonファイル内のVirusTota検知結果を取得(未完成)
def getVTfileinDataset(vtData):
    return 0

#Dataset内のファイルにアクセスする
def getJsonDatainDataset(fileList):
    scankey = 'scans'
    vtkey = 'virustotal'
    returnResultList = [['FileName', 'Result']]
    for filename in fileList:
        eachResultList = [os.path.basename(filename)]
        if isFileCheck(filename):
            with open(filename, 'r') as fj:
                jsonData = json.load(fj)
                if jsonData.has_key(vtkey):
                    eachResultList.append(getVTfileinDataset(jsonData[vtkey]))
                else:
                    eachResultList.append(STRING_UNKNOWN)
        else:
            eachResultList.append(STRING_UNKNOWN)
        returnResultList.append(eachResultList)
    return returnResultList


#Main
if __name__ == '__main__':
    # 引数や-hのオプションを定義
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_Dataset全体からVirustotal結果を取得',description='オプションと引数の説明',
                                epilog='以上')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s version')
    parser.add_argument('DataSetPath', type=str, help='Datasetのパスを指定, 型：%(type)s，String')
    parser.add_argument('WriteCSVFile', type=str, help='Virustotalの検知結果名を書き込むCSVファイルを指定, 型：%(type)s，String')
    parser.add_argument('AntiVender', type=str, help='取得するアンチマルウェアベンダーを指定, 型：%(type)s，String')

    # 引数格納
    arguMain = parser.parse_args()

    # Datasetのパスを格納
    datasetPath = arguMain.DataSetPath
    eCheck = isDirCheck(datasetPath)
    errorEnd(eCheck)

    # 取得する結果のベンダー名
    antiVender = arguMain.AntiVender

    # 書き込む用のCSVファイルを格納＆書き換え
    writeCSVFile = arguMain.WriteCSVFile
    writeCSVFile = writeCSVFile.replace('.csv', '_inDataset_{}.csv'.format(antiVender))
    while isFileCheck(writeCSVFile):
        writeCSVFile = writeCSVFile.replace('.csv', '_A.csv')

    #「.json」拡張子の相対パス付ファイル名を取得
    datasetList = getFilePathName(datasetPath, '.json')

    # Dataset内のVirusTotalの検知結果を取得
    writeList = getJsonDatainDataset(datasetList)
    for i in writeList:
        print i
    print "a"





