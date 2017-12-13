class mycls1:
    def __init__(self, data):
        self.data = data

    def __add__(self, val):
        print("__add__ of mycls1")
        self.data = self.data + val

    def __radd__(self, val):
        print("__radd__ of mycls1")
        self.data = self.data + val

    def __repr__(self):
        print("__repr__ of mycls1")
        return str(self.data)

    def __str__(self):
        print("__str__ of mycls1")
        return str(self.data)

    def __unicode__(self):
        print("__unicode__ of mycls1")
        return unicode(self.data)
