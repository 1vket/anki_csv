from googletrans import Translator
from xpinyin import Pinyin
import sys
import re

translator = Translator()
p = Pinyin()

if len(sys.argv) < 2:
  tsv_file = input("tsv file >> ")
else:
  tsv_file = sys.argv[1]

S = set()
with open(tsv_file, 'r') as f:
  for line in f:
    S.add(line.split('\t')[0])

mode = ('en', 'ja', 'zh-tw')

src = 'en'

while True:
  user_input = input(f"{src} >> ")

  if user_input == 'q':
    sys.exit()

  if user_input == 'c':
    while True:
      src = input("select: en ja zh-tw >> ")
      if src in mode:
        break
    continue

  if user_input == 'rm':
    with open(tsv_file, 'r') as f:
      lines = []
      for line in f:
        lines.append(line)
      lines = lines[:-1]
    with open(tsv_file, 'w') as f:
      f.writelines(lines)
    continue

  d = {}
  d[src] = user_input

  for dest in mode:
    if dest == src:
      continue
    
    translated = translator.translate(user_input, src=src, dest=dest)
    d[dest] = translated.text

  d['pin'] = p.get_pinyin(d['zh-tw'])

  text = f"{d['en']}\t{d['ja']}\t{d['zh-tw']}\t{d['pin']}"

  with open(tsv_file, 'a') as f:
    if d['en'] in S:
      print('did not add: Already exists')
    elif re.search(r'[a-z]',d['ja']):
      print('did not add: Translation failed')
    elif re.search(r'[a-z]',d['zh-tw']):
      print('did not add: Translation failed')
    else:
      f.write(text + '\n')

  print(text)



