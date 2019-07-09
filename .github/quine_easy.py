#!/usr/bin/env python3

# A quine is a program that can output its own source code, and avoids
# trivial means.  This program is a quine with a twist.
# If you haven't already recognized the twist, I cannot help you.

import random

# Things that really can't change.
KEYWORDS = [
    'append', 'def', 'dict', 'else', 'for', 'format', 'if', 'in',
    'import', 'join', 'lower', 'n', 'or', 'print', 'python3', 'random',
    'repr', 'return', 'upper', '#!/usr/bin/env',
]

# This is where the quine-magic happens!
MAGIC = '#!/usr/bin/env python3\n\n# A quine is a program that can output its own source code, and avoids\n# trivial means.  This program is a quine with a twist.\n# If you haven\'t already recognized the twist, I cannot help you.\n\nimport random\n\n# Things that really can\'t change.\nKEYWORDS = [\n    \'append\', \'def\', \'dict\', \'else\', \'for\', \'format\', \'if\', \'in\',\n    \'import\', \'join\', \'lower\', \'n\', \'or\', \'print\', \'python3\', \'random\',\n    \'repr\', \'return\', \'upper\', \'#!/usr/bin/env\',\n]\n\n# This is where the quine-magic happens!\nMAGIC = {}\n\n# The same variable/function/whatever name needs to stay consistent between\n# definition and uses.  So make sure that during a single execution of this\n# program, only one case-flip is produced.\nTWISTS = dict()\n\n\ndef twist_word(word):\n    if word in KEYWORDS:\n        return word\n    if word in TWISTS:\n        new_word = TWISTS[word]\n    else:\n        new_word = \'\'.join(c.upper() if random.random() < 0.5 else c.lower() for c in word)\n        TWISTS[word] = new_word\n    return new_word\n\n\ndef twist(the_str):\n    words = []\n    curr_word = []\n    for c in the_str:\n        if c in \'.,:()[] \\\\\\n\\\'\':\n            words.append(\'\'.join(curr_word))\n            curr_word = []\n            words.append(c)\n        else:\n            curr_word.append(c)\n    words.append(\'\'.join(curr_word))\n    # We don\'t care about empty \'words\'.\n    # This can happen on \'\\n\\n\' and similar.\n    return \'\'.join(twist_word(word) for word in words)\n\n\n# Builds a quine from a "magic" string.  Note that skipping the `twist`\n# invocation would convert this into just a regular quine.\n# (With dead code.)\ndef quine_from(magic):\n    return magic.format(repr(magic))\n\n\ndef run():\n    twisted_magic = twist(MAGIC)\n    twisted_quine = quine_from(twisted_magic)\n    print(twisted_quine[:-1])\n\n\nrun()\n'

# The same variable/function/whatever name needs to stay consistent between
# definition and uses.  So make sure that during a single execution of this
# program, only one case-flip is produced.
TWISTS = dict()


def twist_word(word):
    if word in KEYWORDS:
        return word
    if word in TWISTS:
        new_word = TWISTS[word]
    else:
        random.seed('1337' + word)
        random.random()
        random.random()
        new_word = ''.join(c.upper() if random.random() < 0.5 else c.lower() for c in word)
        TWISTS[word] = new_word
    return new_word


def twist(the_str):
    words = []
    curr_word = []
    for c in the_str:
        if c in '.,:()[] \\\n\'':
            words.append(''.join(curr_word))
            curr_word = []
            words.append(c)
        else:
            curr_word.append(c)
    words.append(''.join(curr_word))
    # We don't care about empty 'words'.
    # This can happen on '\n\n' and similar.
    return ''.join(twist_word(word) for word in words)


# Builds a quine from a "magic" string.  Note that skipping the `twist`
# invocation would convert this into just a regular quine.
# (With dead code.)
def quine_from(magic):
    return magic.format(repr(magic))


def run():
    twisted_magic = twist(MAGIC)
    twisted_quine = quine_from(twisted_magic)
    print(twisted_quine[:-1])


run()
