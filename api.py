#! /usr/bin/python
import requests
import json
from sys import argv

class Translater():
    def __init__(self):
        self.requests = requests.Session()
        self.response = None
        self.result = None
        self.quick = None
        self.liju = None
        self.error = 0
        
    def tran(self, word, from_lang='auto', to_lang=None):
            self.requests.post('http://fanyi.baidu.com/sug?kw=' + word)
            if from_lang == 'auto': #自动检测语言
                lan_info = json.loads(self.requests.post('http://fanyi.baidu.com/langdetect?query=' + word).text)
                from_lang = lan_info['lan']
            else:
                self.requests.post('http://fanyi.baidu.com/langdetect?query=' + word)

            if from_lang == 'zh' and to_lang == None: #默认将语言调节成不同的
                to_lang = 'en'
            elif from_lang == 'en' and to_lang == None: #默认将语言调节成不同的
                to_lang = 'zh'

            if from_lang == to_lang: # 输入是相同的语言
                raise RuntimeError('The Same Language')

            self.response = self.requests.post('http://fanyi.baidu.com/v2transapi',  #查词
                    {
                        'from': from_lang,
                        'to': to_lang,
                        'query': word,
                        'transtype': 'realtime'
                    }
                )
            self._parse()

    def _parse(self):
        self.result = json.loads(self.response.text) #解析结果数据
        if self.result.get('error') == 999:
            raise 'Translate Error'
        self.quick = self.result['trans_result']['data'][0]['result'][0][1]
        #tongyi = self.result['trans_result']['keywords'][0] 
        #查询的同义词不一定是所查的短语，所以返回列表，第一项为所查词语，
        # 第二项为同义词
        #self.tongyi  = [tongyi[1], tongyi[0]]
        try:  #有些词没有例句
            liju = json.loads(self.result['liju_result']['double'])
            #json好像不会自动解析[]结构的数据，需要再次调用
            self.liju = []
            for x in liju:
                self.liju.append([self._list2str(x[0]), self._list2str(x[1]), x[2]])
        except:
            self.liju = None
        finally:
            return 0

    def _list2str(self, li):
        s = ''
        #if len(li[0]) == 5: #传进来英文数组，要加上空格，在每个词语列表的第五项
        for x in li:
            try: #英文的数组中有一部分没有
                s += x[0] + x[4] 
            except:
                s += x[0]
        return s
        #else:
        #    for x in li:
        #        s += x[0] 
        #    return s

#t = Translater()
#t.tran(argv[1], argv[2], argv[3])
#print(t.liju[0])
#t.requ_word("你好")
#print(t.quick)
# try:
#     for x in t.liju:
#         print(x)
# except:
#     print('没有例句')

# def main():
#     t = translater()
#     while(1):
#         raw_in = input(">>> ")
#         
#         t.requ_word('')
# 
