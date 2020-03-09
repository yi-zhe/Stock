class StockModel:
    def __init__(self, name, code, start, to):
        self.name = name
        self.code = code
        self.start = start
        self.to = to
        self.low = None
        self.openP = None
        self.close = None
        self.is_leak = False
        self.v0618 = (self.to - self.start) * 0.618 + self.start
        self.v1 = self.to
        self.v1618 = (self.to - self.start) * 0.618 + self.to
        if self.start > 10000:
            self.diff = 100
        else:
            self.diff = 1

    def calc(self):
        if abs(self.openP - self.v0618) <= self.diff \
                or abs(self.openP - self.v1) <= self.diff \
                or abs(self.openP - self.v1618) <= self.diff \
                or abs(self.close - self.v0618) <= self.diff \
                or abs(self.close - self.v1) <= self.diff \
                or abs(self.close - self.v1618) <= self.diff \
                or abs(self.low - self.v0618) <= self.diff \
                or abs(self.low - self.v1) <= self.diff \
                or abs(self.low - self.v1618) <= self.diff:
            self.is_leak = True
