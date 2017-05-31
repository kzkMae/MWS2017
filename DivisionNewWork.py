#coding:utf-8

import argparse
import os.path
import json

#自作の関数をインポート
from Function import *
from Function import *

#関数定義
#CSVファイルへの書き込み
# def writeCSVfileNW(dir, filename, nwData):
#     print 0
#
# #NW情報を分割して書き込む
# def networkDivision(dirname, filename='network.json'):
#     filename = '{path}/{name}'.format(path=dirname,name=filename)
#     #print filename
#     if not os.path.isfile(filename):
#         print '\'{name}\' is not exist.'.format(name=filename)
#     else:
#         #print 'file exit'
#         #networkデータを読み込む
#         with open(filename,'r') as f:
#             jsonNWData = json.load(f)
#             #print jsonNWData.keys()
#             #キー情報を取得
#             for i in jsonNWData.keys():
#                 #print i, len(jsonNWData[i])
#                 if not(len(jsonNWData[i]) == 0):
#                     #UDPの場合
#                     if i == 'udp':
#                         #print True
#                         writeUdpData = []
#
#                         for j in jsonNWData[i]:
#                             newudpData = [j['time']]
#                             newudpData.extend(['{ip}:{port}'.format(ip=j['src'],port=j['sport'])])
#                             newudpData.extend(['{ip}:{port}'.format(ip=j['dst'],port=j['dport'])])
#                             newudpData.extend([j['offset']])
#                             writeUdpData.append(newudpData)
#                         print writeUdpData
#                         #ファイルへの書き込み




if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='MWS課題，動的解析用プログラム_NW解析用', description='オプションと引数の説明',
                                     epilog='以上')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s version')
    #parser.add_argument('WorkingFolder', type=str, help='データセットがあるフォルダを指定, 型：%(type)s，String')

    # 引数格納
    arguMain = parser.parse_args()

    #フォルダのリストを取得(クラス化の最中)
    files = os.listdir('./')
    folders = [f for f in files if os.path.isdir(os.path.join('./',f))]
    print folders
    print 'a'

    #作業しているフォルダを格納
    # workingfolder = arguMain.WorkingFolder
    # eCheck = isDirCheck(workingfolder)
    # errorEnd(eCheck)
    #
    #
    #
    # #フォルダのリストを取得
    # files = os.listdir(workingfolder)
    # files_dir = [f for f in files if os.path.isdir(os.path.join(workingfolder,f))]
    # #print(files_dir)
    #
    # for i in files_dir:
    #     #検体名と同じディレクトリ名のパスを生成
    #     dirname = "{path}/{name}".format(path=workingfolder,name=i)
    #     #print(dirname)
    #     #print os.path.isdir(dirname)
    #     networkDivision(dirname=dirname)