#coding: utf-8

import Tkinter

from Tkinter import Frame, Button, Label, Entry, Text, Radiobutton
import const

def init():
    for name, dic in [('targetscan', const.targetscan_dict), 
            ('miRanda', const.miRand_dict), 
            ('picTar', const.picTar_dict)]:
        f = open('data/%s.txt' % name)
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            if not len(line) == 4:
                continue
            microRNA, mRNAname, score = line[2].strip(), line[0].strip(), line[3].strip()
            if dic.get(microRNA) == None:
                dic[microRNA] = []
            dic[microRNA].append((mRNAname, score))

def get_result(in_put, select, mlb):
    mlb.delete(0, mlb.size())
    for name, dic in [('targetscan', const.targetscan_dict), 
            ('miRanda', const.miRand_dict), 
            ('picTar', const.picTar_dict)]:
        if not select.get() == name:
            continue
        result = dic.get(in_put.get())
        if result:
            for r in result:
                mlb.insert(Tkinter.END, r)

if __name__ == '__main__':
    test()
