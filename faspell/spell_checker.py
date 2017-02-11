#!/usr/local/bin/env python3.5
# -*- coding: utf-8 -*-
import re
import asyncio
import collections
import time

from helpers import AsyncRange, AsyncListOfTupleIteration, AsyncListIteration


class SpellChecker(object):

    def __init__(self, database, word):
        self.all_words = database
        self.word = word.lower()
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

    async def correct(self):
        return await self.assert_known([self.word]) or \
               await self.assert_known(await self.delete()) or \
               await self.assert_known(await self.transpose()) or \
               await self.assert_known(await self.replace()) or \
               await self.assert_known(await self.insert())
