import requests

class Crawler(object):
    count = 0

    def __inin__(self,url):
        self.q = [url]
        self.seen = set()
        self.dom = f''