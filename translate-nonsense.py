# -*- coding: utf-8 -*-

from googletrans import Translator, LANGUAGES
from random import choice
from urllib.request import urlopen

trans = Translator()

language_list = []
for lang in LANGUAGES : language_list.append(lang)

times_to_translate = 100
times_left = times_to_translate
web_file = urlopen("https://pastebin.com/raw/QVN9GXMx")
translation = web_file.read()
translation = translation.decode().split("\r\n")
translation = "\n".join(translation)
print (translation)

for i in range (times_left) :
    translation = trans.translate(translation, dest=choice(language_list)).text
    print (f"translated {i}/{times_to_translate} times")
print("-------------------------------------------------")
translation = trans.translate(translation,dest="en").text
print (translation)