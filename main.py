from googletrans import Translator
from xpinyin import Pinyin
import sys

translator = Translator()
p = Pinyin()

csv_file = "data.csv"

src = 'ja'
dest = 'zh-tw'

while True:
  user_input = input(f"{src} >> ")

  if user_input == 'q':
    sys.exit()

  if user_input == 'c':
    src, dest = dest, src
    continue

  if user_input == 'rm':
    with open(csv_file, 'r') as f:
      lines = []
      for line in f:
        lines.append(line)
      lines = lines[:-1]
    with open(csv_file, 'w') as f:
      f.writelines(lines)
    continue

  translated = translator.translate(user_input, src=src, dest=dest)

  d = {}
  d[src] = user_input
  d[dest] = translated.text

  d['pron'] = p.get_pinyin(d['zh-tw'])

  text = f"{d['ja']},{d['zh-tw']},{d['pron']}"

  with open(csv_file, 'a') as f:
    f.write(text + '\n')

  print(text)



