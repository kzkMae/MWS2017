#coding:utf-8

import argparse
import sys
import os.path
import csv

#引数や-hのオプションを定義
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_ファイルコピー',description='オプションと引数の説明',
                                epilog='以上')
    parser.add_argument('-v','--version', action='version', version='%(prog)s version')
    parser.add_argument('CopyFolder',type=str, help='コピー元のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('SendFolder',type=str, help='コピー先のフォルダを指定, 型：%(type)s，String')
    parser.add_argument('CSVFile',type=str, help='探すJsonファイルのリストを格納したCSVファイルを指定, 型：%(type)s，String')

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
        print '\'{}\'というディレクトリは存在しません'.format(folderName)
    return isdirTF

#ファイルの有無をチェック
def isFileCheck(fileName):
    isfileTF = os.path.isfile(fileName)
    if not isfileTF:
        print '\'{}\'というファイルは存在しません'.format(fileName)
    return isfileTF


#CSVファイルの読み出し


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
    print 'a'




