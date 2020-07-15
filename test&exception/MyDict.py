class MyDict(dict):
    def __init__(self, **kwargs):
        super(MyDict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("No attribute '%s' in MyDict" % key)

    def __setattr__(self, key, value):
        self[key] = value
        print(self[key])
