#! python3
# bulletPointAdder.py - クリップボードのテキストの各行に「*」を挿入し、箇条書きにする

import pyperclip

# クリップボードの行を分割して、「*」を挿入する
lines = pyperclip.paste().split('\n')
for i in range(len(lines)) :
    lines[i] = '* ' + lines[i]
result = '\n'.join(lines)

# クリップボードにコピー
pyperclip.copy(result)
