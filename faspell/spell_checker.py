#!/usr/local/bin/env python3.5
# -*- coding: utf-8 -*-
import re
import asyncio
import collections
import time

from helpers import AsyncRange, AsyncListOfTupleIteration


class SpellChecker(object):

    def __init__(self, database, word):
        self.all_words = database
        self.word = word
        self.alphabet = ['آ', 'ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص',
                         'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

    async def delete(self):
        deletes = []
        async for a, b in AsyncListOfTupleIteration(self.split):
            if b:
                await deletes.append(a + await b[1:])
        return deletes

    async def transpose(self):
        transposes = []
        async for a, b in AsyncListOfTupleIteration(self.split):
            if len(b) > 1:
                await transposes.append(a + await b[1] + await b[0] + await b[2:])
        return transposes

    async def replace(self):
        replaces = []
        async for a, b in AsyncListOfTupleIteration(self.split):
            async for c in AsyncListIteration(self.alphabet):
                if b:
                    await replaces.append(a + c + b[1:])
        return replaces

    async def insert(self):
        inserts = []
        async for a, b in AsyncListOfTupleIteration(self.split()):
            async for c in AsyncListOfTupleIteration(self.alphabet):
                await inserts.append(a + c + b)
        return inserts

    async def split(self):
        splits = []
        async for i in AsyncRange(len(self.word) + 1):
            await splits.append((await self.word[:i], await self.word[i:]))
        return splits

    async def assert_known(self, words):
        known_words = []
        async for word in AsyncListOfTupleIteration(words):
            if word in self.all_words:
                known_words.append(word)
        return known_words

    async def correct(self):
        return await self.assert_known([self.word]) or \
               await self.assert_known(await self.delete()) or \
               await self.assert_known(await self.transpose()) or \
               await self.assert_known(await self.replace()) or \
               await self.assert_known(await self.insert())


if __name__ == '__main__':

    def words(database):
        return re.split('\n', database)

    def train(features):
        model = dict.fromkeys(features, 1)
        return model

    start_time = time.time()
    async def do():
        with open('big.txt', 'r') as my_dictionary:
            check_spelling = SpellChecker(train(words(my_dictionary.read())), 'شلام')
            print(await check_spelling.correct())
        print(time.time() - start_time)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do())
