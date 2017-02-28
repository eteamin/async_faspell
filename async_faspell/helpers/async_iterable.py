

class AsyncRange(object):
    def __init__(self, length):
        self.length = length
        self.i = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        index = self.i
        self.i += 1
        if self.i <= self.length:
            return index
        else:
            raise StopAsyncIteration


class AsyncListOfTupleIteration(object):
    def __init__(self, _list):
        self.list = _list
        self.i = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            item = self.list[self.i]
            self.i += 1
            return item
        except IndexError:
            raise StopAsyncIteration


class AsyncListIteration(object):
    def __init__(self, _list):
        self.list = _list
        self.i = 0

    async def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            item = self.list[self.i]
            self.i += 1
            return item
        except IndexError:
            raise StopAsyncIteration
