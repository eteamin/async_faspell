from os import path

from aiohttp.web import Application, run_app, Response

import faspell
from faspell.spell_checker import SpellChecker

database = path.abspath(path.join(path.dirname(faspell.__file__), '..', 'database', 'words.txt'))
words = None

async def correct(request):
    params = await request.post()
    word = params.get('word')
    s = SpellChecker(words, word)
    resp = await s.correct()
    return Response(text=str(resp))


def make_app():
    # Routes
    app = Application()
    app.router.add_route('POST', '/apiv1/correct', correct)
    global words
    with open(database, 'r') as all_words:
        words = all_words.read()
    return app

run_app(make_app())