class LexSort:
    def __init__(self):
        self.ord = ''

    def _cmp(self, x, y):
        if len(x) == 0 and len(y) > 0:
            return -1
        elif len(x) > 0 and len(y) == 0:
            return 1
        elif len(x) == 0 and len(y) == 0:
            return 0
        else:
            if self.ord.index(x[0]) < self.ord.index(y[0]):
                return -1
            elif self.ord.index(x[0]) > self.ord.index(y[0]):
                return 1
            else:
                return self._cmp(x[1:], y[1:])

    def sort(self, l, ord):
        self.ord = ord
        # sort in-place
        l.sort(cmp=self._cmp)
        return l

