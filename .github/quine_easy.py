#!/usr/bin/env python3
# A quine is a program that can output its own source code, and avoids trivial means.  This program is a quine with a twist.  If you haven't already recognized the twist, I cannot help you.

import random

# Things that really can't change.
KEYWORDS = ['def', 'dict', 'else', 'extend', 'for', 'format', 'if', 'in',  'import', 'join', 'lower', 'n', 'print', 'python3', 'random',  'repr', 'return', 'seed', 'upper', '#!/usr/bin/env']
# This is where the quine-magic happens!
MAGIC = "#!/usr/bin/env python3\n# A quine is a program that can output its own source code, and avoids trivial means.  This program is a quine with a twist.  If you haven't already recognized the twist, I cannot help you.\n\nimport random\n\n# Things that really can't change.\nKEYWORDS = ['def', 'dict', 'else', 'extend', 'for', 'format', 'if', 'in',  'import', 'join', 'lower', 'n', 'print', 'python3', 'random',  'repr', 'return', 'seed', 'upper', '#!/usr/bin/env']\n# This is where the quine-magic happens!\nMAGIC = {}\nSEED = repr(random.random())\n\n\ndef twist_word(word):\n    if word in KEYWORDS:\n        return word\n    # The same variable/function/whatever name needs to stay consistent between definition and uses.  So make sure that during a single execution of this program, only one case-flip is produced.\n    random.seed(SEED + word)\n    random.random()\n    random.random()\n    new_word = ''.join(c.upper() if random.random() < 0.5 else c.lower() for c in word)\n    return new_word\n\n\ndef twist(the_str):\n    words, curr_word = [], []\n    for c in the_str:\n        if c in '.,:()[] \\\\\\n\\'':\n            words.extend([''.join(curr_word), c])\n            curr_word = []\n        else:\n            curr_word.extend(c)\n    # We don't care about empty 'words'.  This can happen on '\\n\\n' and similar.\n    return ''.join(twist_word(word) for word in words + [''.join(curr_word)])\n\n\ntwisted_magic = twist(MAGIC)\nprint(twisted_magic.format(repr(twisted_magic))[:-1])\n"
SEED = '1337'


def twist_word(word):
    if word in KEYWORDS:
        return word
    # The same variable/function/whatever name needs to stay consistent between definition and uses.  So make sure that during a single execution of this program, only one case-flip is produced.
    random.seed(SEED + word)
    random.random()
    random.random()
    new_word = ''.join(c.upper() if random.random() < 0.5 else c.lower() for c in word)
    return new_word


def twist(the_str):
    words, curr_word = [], []
    for c in the_str:
        if c in '.,:()[] \\\n\'':
            words.extend([''.join(curr_word), c])
            curr_word = []
        else:
            curr_word.extend(c)
    # We don't care about empty 'words'.  This can happen on '\n\n' and similar.
    return ''.join(twist_word(word) for word in words + [''.join(curr_word)])


twisted_magic = twist(MAGIC)
print(twisted_magic.format(repr(twisted_magic))[:-1])
