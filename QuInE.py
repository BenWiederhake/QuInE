#!/usr/bin/env python3

# A QuInE iS a pROgRam thAt CAN OUtpUt ITS Own SoUrcE coDe, And AVOiDS
# trIvial MEanS.  THiS pROgRam iS a QuInE wITH a twiST.
# if yOu HAvEN'T aLREadY rECOGnIZeD ThE twiST, I caNnot help yOu.

import random

# thINgs thAt REallY CAN'T cHAnGE.
KeyWOrdS = [
    'append', 'def', 'dict', 'else', 'for', 'format', 'if', 'in',
    'import', 'join', 'lower', 'n', 'print', 'python3', 'random',
    'repr', 'return', 'upper', '#!/usr/bin/env',
]

# THiS iS wheRE ThE quINE-MAgiC hAPpENS!
mAgic = '#!/usr/bin/env python3\n\n# A QuInE iS a pROgRam thAt CAN OUtpUt ITS Own SoUrcE coDe, And AVOiDS\n# trIvial MEanS.  THiS pROgRam iS a QuInE wITH a twiST.\n# if yOu HAvEN\'T aLREadY rECOGnIZeD ThE twiST, I caNnot help yOu.\n\nimport random\n\n# thINgs thAt REallY CAN\'T cHAnGE.\nKeyWOrdS = [\n    \'append\', \'def\', \'dict\', \'else\', \'for\', \'format\', \'if\', \'in\',\n    \'import\', \'join\', \'lower\', \'n\', \'print\', \'python3\', \'random\',\n    \'repr\', \'return\', \'upper\', \'#!/usr/bin/env\',\n]\n\n# THiS iS wheRE ThE quINE-MAgiC hAPpENS!\nmAgic = {}\n\n# tHe SAme VARIABLE/FunCtioN/WHateVEr namE nEeds To sTay CoNsistenT bETWEeN\n# defINItiOn And uses.  SO mAkE surE thAt durInG a SiNGLe Execution OF thIs\n# pROgRam, OnLy oNE Case-FliP iS pRODUcEd.\ntWIstS = dict()\n\n\ndef TWisT_wOrD(WORD):\n    if WORD in KeyWOrdS:\n        return WORD\n    if WORD in tWIstS:\n        NeW_woRd = tWIstS[WORD]\n    else:\n        NeW_woRd = \'\'.join(C.upper() if random.random() < 0.5 else C.lower() for C in WORD)\n        tWIstS[WORD] = NeW_woRd\n    return NeW_woRd\n\n\ndef twiST(The_stR):\n    woRds = []\n    cURr_wORd = []\n    for C in The_stR:\n        if C in \'.,:()[] \\\\\\n\\\'\':\n            woRds.append(\'\'.join(cURr_wORd))\n            cURr_wORd = []\n            woRds.append(C)\n        else:\n            cURr_wORd.append(C)\n    woRds.append(\'\'.join(cURr_wORd))\n    # WE don\'T CARE aBoUt EMpTy \'woRds\'.\n    # THiS CAN hAppeN on \'\\n\\n\' And SImiLAR.\n    return \'\'.join(TWisT_wOrD(WORD) for WORD in woRds)\n\n\n# bUilDS a QuInE FroM a "MagIC" StRiNG.  NOte thAt sKippInG ThE `tWIsT`\n# iNVOCation WOUld COnVeRT thIs iNTO juST a reGUlar QuInE.\n# (wiTh deAd coDe.)\ndef QUIne_frOM(mAgiC):\n    return mAgiC.format(repr(mAgiC))\n\n\ndef rUn():\n    twISTED_mAGiC = twiST(mAgic)\n    TWisTEd_QuiNe = QUIne_frOM(twISTED_mAGiC)\n    print(TWisTEd_QuiNe[:-1])\n\n\nrUn()\n'

# tHe SAme VARIABLE/FunCtioN/WHateVEr namE nEeds To sTay CoNsistenT bETWEeN
# defINItiOn And uses.  SO mAkE surE thAt durInG a SiNGLe Execution OF thIs
# pROgRam, OnLy oNE Case-FliP iS pRODUcEd.
tWIstS = dict()


def TWisT_wOrD(WORD):
    if WORD in KeyWOrdS:
        return WORD
    if WORD in tWIstS:
        NeW_woRd = tWIstS[WORD]
    else:
        NeW_woRd = ''.join(C.upper() if random.random() < 0.5 else C.lower() for C in WORD)
        tWIstS[WORD] = NeW_woRd
    return NeW_woRd


def twiST(The_stR):
    woRds = []
    cURr_wORd = []
    for C in The_stR:
        if C in '.,:()[] \\\n\'':
            woRds.append(''.join(cURr_wORd))
            cURr_wORd = []
            woRds.append(C)
        else:
            cURr_wORd.append(C)
    woRds.append(''.join(cURr_wORd))
    # WE don'T CARE aBoUt EMpTy 'woRds'.
    # THiS CAN hAppeN on '\n\n' And SImiLAR.
    return ''.join(TWisT_wOrD(WORD) for WORD in woRds)


# bUilDS a QuInE FroM a "MagIC" StRiNG.  NOte thAt sKippInG ThE `tWIsT`
# iNVOCation WOUld COnVeRT thIs iNTO juST a reGUlar QuInE.
# (wiTh deAd coDe.)
def QUIne_frOM(mAgiC):
    return mAgiC.format(repr(mAgiC))


def rUn():
    twISTED_mAGiC = twiST(mAgic)
    TWisTEd_QuiNe = QUIne_frOM(twISTED_mAGiC)
    print(TWisTEd_QuiNe[:-1])


rUn()
