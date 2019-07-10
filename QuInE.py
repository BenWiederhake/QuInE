#!/usr/bin/env python3
# A QuInE iS a pROgRam thAt CAN OUtpUt ITS Own SoUrcE coDe, And AVOiDS trIvial MEanS.  THiS pROgRam iS a QuInE wITH a twiST.  if yOu HAvEN'T aLREadY rECOGnIZeD ThE twiST, I caNnot help yOu.

import random

# thINgs thAt REallY CAN'T cHAnGE.
KeyWOrdS = ['def', 'dict', 'else', 'extend', 'for', 'format', 'if', 'in',  'import', 'join', 'lower', 'n', 'print', 'python3', 'random',  'repr', 'return', 'seed', 'upper', '#!/usr/bin/env']
# THiS iS wheRE ThE quINE-MAgiC hAPpENS!
mAgic = "#!/usr/bin/env python3\n# A QuInE iS a pROgRam thAt CAN OUtpUt ITS Own SoUrcE coDe, And AVOiDS trIvial MEanS.  THiS pROgRam iS a QuInE wITH a twiST.  if yOu HAvEN'T aLREadY rECOGnIZeD ThE twiST, I caNnot help yOu.\n\nimport random\n\n# thINgs thAt REallY CAN'T cHAnGE.\nKeyWOrdS = ['def', 'dict', 'else', 'extend', 'for', 'format', 'if', 'in',  'import', 'join', 'lower', 'n', 'print', 'python3', 'random',  'repr', 'return', 'seed', 'upper', '#!/usr/bin/env']\n# THiS iS wheRE ThE quINE-MAgiC hAPpENS!\nmAgic = {}\nseed = repr(random.random())\n\n\ndef TWisT_wOrD(WORD):\n    if WORD in KeyWOrdS:\n        return WORD\n    # tHe SAme VARIABLE/FunCtioN/WHateVEr namE nEeds To sTay CoNsistenT bETWEeN defINItiOn And uses.  SO mAkE surE thAt durInG a SiNGLe Execution OF thIs pROgRam, OnLy oNE Case-FliP iS pRODUcEd.\n    random.seed(seed + WORD)\n    random.random()\n    random.random()\n    NeW_woRd = ''.join(C.upper() if random.random() < 0.5 else C.lower() for C in WORD)\n    return NeW_woRd\n\n\ndef twiST(The_stR):\n    woRds, cURr_wORd = [], []\n    for C in The_stR:\n        if C in '.,:()[] \\\\\\n\\'':\n            woRds.extend([''.join(cURr_wORd), C])\n            cURr_wORd = []\n        else:\n            cURr_wORd.extend(C)\n    # WE don'T CARE aBoUt EMpTy 'woRds'.  THiS CAN hAppeN on '\\n\\n' And SImiLAR.\n    return ''.join(TWisT_wOrD(WORD) for WORD in woRds + [''.join(cURr_wORd)])\n\n\ntwISTED_mAGiC = twiST(mAgic)\nprint(twISTED_mAGiC.format(repr(twISTED_mAGiC))[:-1])\n"
seed = repr(random.random())


def TWisT_wOrD(WORD):
    if WORD in KeyWOrdS:
        return WORD
    # tHe SAme VARIABLE/FunCtioN/WHateVEr namE nEeds To sTay CoNsistenT bETWEeN defINItiOn And uses.  SO mAkE surE thAt durInG a SiNGLe Execution OF thIs pROgRam, OnLy oNE Case-FliP iS pRODUcEd.
    random.seed(seed + WORD)
    random.random()
    random.random()
    NeW_woRd = ''.join(C.upper() if random.random() < 0.5 else C.lower() for C in WORD)
    return NeW_woRd


def twiST(The_stR):
    woRds, cURr_wORd = [], []
    for C in The_stR:
        if C in '.,:()[] \\\n\'':
            woRds.extend([''.join(cURr_wORd), C])
            cURr_wORd = []
        else:
            cURr_wORd.extend(C)
    # WE don'T CARE aBoUt EMpTy 'woRds'.  THiS CAN hAppeN on '\n\n' And SImiLAR.
    return ''.join(TWisT_wOrD(WORD) for WORD in woRds + [''.join(cURr_wORd)])


twISTED_mAGiC = twiST(mAgic)
print(twISTED_mAGiC.format(repr(twISTED_mAGiC))[:-1])
