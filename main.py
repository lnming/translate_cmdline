#! /usr/bin/python

import api
from os import system
from sys import argv

t = api.Translater()

#t.tran(*argv[1:])

def fprint(*args, **kargs):
    print('>>>', end = ' ')
    print(*args, **kargs)

def finput(*args, **kargs):
    print('>>> ', end = ' ')
    return input(*args, **kargs)

def show(tran):
    fprint('翻译结果：' + tran.quick)
    if(tran.liju == None):
        return 
    else:
        try:
            fprint('进入例句显示模式，按q键回车退出：')
            for x in range(len(tran.liju)):
                key = finput()
                if(key == 'q'):
                    break
                if(key == '\x0c'): #Ctrl-L
                    system('clear')
                fprint(' [{}]原句：{}'.format(x, tran.liju[x][0]))
                fprint('    译句：' + tran.liju[x][1])
                fprint('    来源：' + tran.liju[x][2])
        except KeyboardInterrupt:
            print()
            return


while(1):
    try:
        info = [x for x in finput('输入词条及语言，用空格隔开：').split(' ') if x != '']
        if(info == ['q']): #退出 
            break
        if(info == []): #没有输入
            continue
        t.tran(*info) # 翻译
        show(t)
    except RuntimeError as e:
        fprint(info[0] + ': ')
        fprint(e)
    except KeyboardInterrupt:
        print()
        continue
    except EOFError:
        exit()

