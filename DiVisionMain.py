#coding:utf-8

import argparse
import os.path
import json

#自作の関数をインポート
from Function import *
from Function2 import *
#関数定義



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_解析用', description='オプションと引数の説明',
                                     epilog='以上')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s version')
    #parser.add_argument('WorkingFolder', type=str, help='データセットがあるフォルダを指定, 型：%(type)s，String')
    parser.add_argument('directory', nargs='?',metavar='dir', default='./',help='分割したファイルが存在するディレクトリを指定.\nデフォルトはワーキングdirectory' )


    # 引数格納
    arguMain = parser.parse_args()

    pwd = arguMain.directory

    echecker = FFBasicError()
    echecker.isDirCheck(folderName=pwd)

    #フォルダのリストを取得
    folders = FolderLists(pwd)
    #NetworkJsonの処理
    readNetworkJson(directory=pwd,folders=folders.getFolderList())

    #作業しているフォルダを格納
    # for i in files_dir:
    #     #検体名と同じディレクトリ名のパスを生成
    #     dirname = "{path}/{name}".format(path=workingfolder,name=i)
    #     #print(dirname)
    #     #print os.path.isdir(dirname)
    #     networkDivision(dirname=dirname)