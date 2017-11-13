# api

### 首先调用

`http://fanyi.baidu.com/sug?kw=被翻译的词语`

    返回

    ```
    {
        "errno":1,
        "data":[]
    }
    ```

### 再调用

`http://fanyi.baidu.com/langdetect?query=被翻译的词语`

    返回

    ```
    {
        "error":0,
        "msg":"success",
        "lan":"en"
    }
    ```

    从lan项可以获取翻译词语的语言种类

### 最后

`http://fanyi.baidu.com/v2transapi? + 以下表单数据`

    ```
    {
        'from': 'zh', 
        'to': 'en', 
        'query': '我是请求', 
        'transtype': 'realtime'
    }
    ```

    返回

    ```
    {
        'trans_result': 
        {
            'from': 'zh', 
            'to': 'en', 
            'domain': 'all', 
            'type': 2, 
            'status': 0, 
            'data': //结果
            [
                {
                    'dst': "I'm asking", 
                    'prefixWrap': 0, 
                    'src': '我是请求', 
                    'relation': [], 
                    'result': 
                    [
                        [0, "I'm asking", ['0|12'], [], ['0|12'], ['0|10']], 
                        ... //多个释义
                    ]
                }
            ], 
            'keywords':  //同义词，可能有
            [
                {
                    'means': ['request', 'ask', 'demand', 'beg', 'ask for'], 
                    'word': '请求'
                }
            ]
        },
        'liju_result': //例句
        {
            'double': //包含多条例句
            [
                [ //一条例句
                    [
                        ['我', 'xxx', 'xxx', int, ' '], //原句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['是', 'xxx', 'xxx', int],
                        ...
                    ],
                    [
                        ['I', 'xxx', 'xxx', int, ' '], //翻译句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['am', 'xxx', 'xxx', int],
                        ...
                    ],
                    ['provided by ...', int]  //句子来源
                ],
                [ //一条例句
                    [
                        ['我', 'xxx', 'xxx', int, ' '], //原句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['是', 'xxx', 'xxx', int],
                        ...
                    ],
                    [
                        ['I', 'xxx', 'xxx', int, ' '], //翻译句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['am', 'xxx', 'xxx', int],
                        ...
                    ],
                    ['provided by ...', int]  //句子来源
                ],
                [ //一条例句
                    [
                        ['我', 'xxx', 'xxx', int, ' '], //原句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['是', 'xxx', 'xxx', int],
                        ...
                    ],
                    [
                        ['I', 'xxx', 'xxx', int, ' '], //翻译句，可能四项也可能五项，五项最后一项是分隔符，比如英文句子中间的空格
                        ['am', 'xxx', 'xxx', int],
                        ...
                    ],
                    ['provided by ...', int]  //句子来源
                ],
                ...
            ]
            'tag': [],
            'single': ''
        }
    }
    ```
