import chardet
# 编码检测, 之后转为str
# 支持编码：https://chardet.readthedocs.io/en/latest/supported-encodings.html
d = chardet.detect(b'this test?')
print(d)
print(chardet.detect('驰来北马多骄气，歌到南风尽死声'.encode('gbk')))
# >>>{'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
data = '終焉の世界から'.encode('euc-jp')
print(chardet.detect(data))
