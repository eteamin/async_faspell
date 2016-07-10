#author: Amin Etesamian
#date: 26/12/1394 - 22:46 pm



1. introduction

here is a persian spell checker written in python. in order to use it, first create an instance of SpellChecker class by providing it with a dictionary. then using the
Correct method, you are given a dictionary containg the checked word, it's status(which is wrong) and suggestions for the purpose of correction. for example:

>>>my_spell_checker = SpellChecker(my_dictionary_file)
>>>print(my_spell_checker.correct(the_word_to_be_corrected))
would give such result:

{[
'word': the_word_to_be_corrected,
'ud': false,
'suggestions': [suggestion[0], suggestion[1], ...]
]}


2. installation
simply open your terminal an type: pip(desired version) install persian_spell_checker(desired version).

in case of any bug encounter, please contact eteamin@yahoo.com
