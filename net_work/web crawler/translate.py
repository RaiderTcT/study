import requests
import json
import time
# Request URL: https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=6&tsel=3&kc=0&tk=321673.157973&q=%E6%97%B6%E9%97%B4
# Request Method: GET
# Status Code: 200
# Remote Address: 203.208.43.79:443
# Referrer Policy: no-referrer-when-downgrade
# 谷歌翻译为get请求，直接拼接url q后边为待翻译的内容
# tk 根据不同的翻译 用js计算出
# client: t
# sl: zh-CN
# tl: en
# hl: zh-CN
# dt: at
# dt: bd
# dt: ex
# dt: ld
# dt: md
# dt: qca
# dt: rw
# dt: rm
# dt: ss
# dt: t
# ie: UTF-8
# oe: UTF-8
# ssel: 6
# tsel: 3
# kc: 0
# tk: 321673.157973
# q: 时间
import execjs


class Py4Js():

    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
        
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
    
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)


def translate(content, tk):
    params = {'tk': tk, 'q': content}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&ssel=6&tsel=3&kc=0'
    # 代理
    # '类型'： '代理ip：端口号'
    proxies= {
        "http":"http://115.153.167.165:9000",
    }
    r = requests.get(url, params=params, headers=headers, proxies=proxies)

    # for text in r.json():
    #     print(text)
    print(r.json()[0][0][0])


def main():
    js = Py4Js()
    while 1:
        content = input('输入待翻译内容：')
        if content == 'q!':
            break
        # content = "天下第一"
        tk = js.getTk(content)
        translate(content, tk)
        # 延迟提交
        # time.sleep(3)


if __name__ == "__main__":
    main()
