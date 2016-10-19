#coding:utf-8

import argparse
import os.path
import shutil

#Function.py内の関数にアクセス
from Function import *

#引数や-hのオプションを定義
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_ファイルコピー',description='オプションと引数の説明',
                                epilog='以上')
    parser.add_argument('-v','--version', action='version', version='%(prog)s version')
    parser.add_argument('CopyFolder',type=str, help='コピー元のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('SendFolder',type=str, help='コピー先のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('CSVFile',type=str, help='探すJsonファイルのリストを格納したCSVファイルを指定, 型：%(type)s，String')


#csvオブジェクトからJsonファイル名を取得・コピー
def copyJsonFile(csvReader, copyfolder, sendfolder):
    #print type(csvReader)
    for row in csvReader:
        #print row[0]
        fpCName = '{path}{fname}'.format(path=copyfolder,fname=row[0])
        fpSName = '{path}{fname}'.format(path=sendfolder,fname=row[0])
        if not os.path.isfile(fpCName):
            print '\'{}\' is not exist.'.format(fpCName)
        else:
            shutil.copyfile(fpCName, fpSName)
    return 0

# エラーチェック用変数
eCheck = True

if __name__ == '__main__':
    # 引数格納
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

    #CSVファイルの内容を読み込む（Jsonファイル名リスト）
    readList = readCsvFile(csvfile)
    copyJsonFile(readList, copyfolder, sendfolder)
    print 'a'




