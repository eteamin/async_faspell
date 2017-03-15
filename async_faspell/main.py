#!/usr/local/bin/env python3.5
# -*- coding: utf-8 -*-


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


class SpellChecker(object):

    def __init__(self, database):
        self.all_words = database
        self.alphabet = ['آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص',
                         'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

    async def delete(self):
        deletes = []
        async for a, b in AsyncListOfTupleIteration(await self.split()):
            if b:
                deletes.append(a + b[1:])
        return deletes

    async def transpose(self):
        transposes = []
        async for a, b in AsyncListOfTupleIteration(await self.split()):
            if len(b) > 1:
                transposes.append(a + b[1] + b[0] + b[2:])
        return transposes

    async def replace(self):
        replaces = []
        async for a, b in AsyncListOfTupleIteration(await self.split()):
            async for c in AsyncListIteration(self.alphabet):
                if b:
                    replaces.append(a + c + b[1:])
        return replaces

    async def insert(self):
        inserts = []
        async for a, b in AsyncListOfTupleIteration(await self.split()):
            async for c in AsyncListOfTupleIteration(self.alphabet):
                inserts.append(a + c + b)
        return inserts

    async def split(self):
        splits = []
        async for i in AsyncRange(len(self.word) + 1):
            splits.append((self.word[:i], self.word[i:]))
        return splits

    async def assert_known(self, words):
        known_words = []
        async for word in AsyncListOfTupleIteration(words):
            if word in self.all_words:
                known_words.append(word)
        return known_words

    async def correct(self, word):
        self.word = word
        return await self.assert_known([self.word]) or \
            await self.assert_known(await self.delete()) or \
            await self.assert_known(await self.transpose()) or \
            await self.assert_known(await self.replace()) or \
            await self.assert_known(await self.insert())
