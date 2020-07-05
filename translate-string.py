# -*- coding: utf-8 -*-

# requires a string to work. can also be a multi line string.

from googletrans import Translator, LANGUAGES
from random import choice

trans = Translator()

language_list = []
for lang in LANGUAGES : language_list.append(lang)

times_to_translate = 100
times_left = times_to_translate
translation = "INSERT TEXT TO TRANSLATE HERE"
print (translation)

for i in range (times_left) :
    translation = trans.translate(translation, dest=choice(language_list)).text
    print (f"translated {i}/{times_to_translate} times")
print("-------------------------------------------------")
translation = trans.translate(translation,dest="en").text
print (translation)
