#coding:utf-8

import argparse
import os.path
import json

#自作の関数をインポート


#関数定義
from Function import *


#エラーチェック用変数
eCheck = 0

#定数
STRING_NONE = 'None'
STRING_UNKNOWN = 'Unknown'

#VirusTotalファイルにアクセス
def getVTfile(vtData, vName):
    #print vtData.keys()
    keyName1 = 'result'
    returnList = []
    if vtData.has_key(vName):
        #print vtData[vName]
        if vtData[vName].has_key(keyName1):
            #print 'a'
            if vtData[vName][keyName1] is None:
                returnList.append(STRING_NONE)
            else:
                returnList.append(vtData[vName][keyName1])
        else:
            returnList.append(STRING_UNKNOWN)
    else:
        returnList.append(STRING_UNKNOWN)
    #print returnList
    return returnList


#分割したファイル内のVirustotalファイルにアクセスし，検知結果を取得
def getVirusTotalResult(jlist, venderName):
    scankey = 'scans'
    returnResultList = [['FileName','Result']]
    for folderName in jlist:
        folder,ext = os.path.splitext(folderName[0])
        eachResultList = [folder]
        fpVTFile = './{}/virustotal.json'.format(folder)
        #print fpVTFile
        if isFileCheck(fpVTFile):
            with open(fpVTFile,'r') as fvt:
                jsonData = json.load(fvt)
                if jsonData.has_key(scankey):
                    eachResultList.extend(getVTfile(jsonData[scankey], venderName))
        else:
            eachResultList.append(STRING_UNKNOWN)
        #print eachResultList
        returnResultList.append(eachResultList)
    #print returnResultList
    return returnResultList


#Main
if __name__ == '__main__':
    # 引数や-hのオプションを定義
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_Virustotal結果を取得',description='オプションと引数の説明',
                                epilog='以上')
    parser.add_argument('-v','--version', action='version', version='%(prog)s version')
    parser.add_argument('CSVFile',type=str, help='Jsonファイルのリストを格納したCSVファイルを指定, 型：%(type)s，String')
    parser.add_argument('WriteCSVFile',type=str, help='Virustotalの検知結果名を書き込むCSVファイルを指定, 型：%(type)s，String')
    parser.add_argument('AntiVender', type=str, help='取得するアンチマルウェアベンダーを指定, 型：%(type)s，String')

    # 引数格納
    arguMain = parser.parse_args()

    #読み込むCSVファイルを格納
    csvFile = arguMain.CSVFile
    eCheck = isFileCheck(csvFile)
    errorEnd(eCheck)

    #取得する結果のベンダー名
    antiVender = arguMain.AntiVender

    # 書き込む用のCSVファイルを格納＆書き換え
    writeCSVFile = arguMain.WriteCSVFile
    writeCSVFile = writeCSVFile.replace('.csv', '_{}.csv'.format(antiVender))
    while isFileCheck(writeCSVFile):
        writeCSVFile = writeCSVFile.replace('.csv', '_A.csv')
        #print 'bb'

    #Jsonファイルリストの読み込み
    jsonList = readCsvFile(csvFile)
    #print jsonList

    #書き込むVirusTotalの検知結果
    writeList = getVirusTotalResult(jsonList, antiVender)
    #print writeList
    #CSVファイルへの書き込み
    writeCsvFilebyList(writeCSVFile, writeList)





