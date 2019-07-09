#!/usr/bin/env python3

# a QuIne Is A prOgRAm THat can OutPut ITS Own sOUrce cODE, aNd aVoids
# trIvial MEaNs.  ThiS prOgRAm Is A QuIne wiTH A TWIsT.
# if yoU havEn't ALReadY RecOgnIZed THE tWIst, i canNOT HeLp yoU.

import random

# tHiNgS THat rEalLY can't chAnGE.
KeYworDs = [
    'append', 'def', 'dict', 'else', 'for', 'format', 'if', 'in',
    'import', 'join', 'lower', 'n', 'or', 'print', 'python3', 'random',
    'repr', 'return', 'upper', '#!/usr/bin/env',
]

# ThiS Is wHERe THE quine-mAgic hAppeNS!
MAgic = '#!/usr/bin/env python3\n\n# a QuIne Is A prOgRAm THat can OutPut ITS Own sOUrce cODE, aNd aVoids\n# trIvial MEaNs.  ThiS prOgRAm Is A QuIne wiTH A TWIsT.\n# if yoU havEn\'t ALReadY RecOgnIZed THE tWIst, i canNOT HeLp yoU.\n\nimport random\n\n# tHiNgS THat rEalLY can\'t chAnGE.\nKeYworDs = [\n    \'append\', \'def\', \'dict\', \'else\', \'for\', \'format\', \'if\', \'in\',\n    \'import\', \'join\', \'lower\', \'n\', \'or\', \'print\', \'python3\', \'random\',\n    \'repr\', \'return\', \'upper\', \'#!/usr/bin/env\',\n]\n\n# ThiS Is wHERe THE quine-mAgic hAppeNS!\nMAgic = {}\n\n\n# THe saMe VArIaBLE/fUnCtioN/WhATeVeR nAMe NeEdS to sTAY cONSistENt BETWeen\n# DeFInItIon aNd UsEs.  sO mAKE sUrE THat During A SinglE EXeCUtION Of tHiS\n# pROGRam, ONLY One Case-FLip Is proDuCeD.\ntwISts = dict()\n\n\ndef tWIst_worD(WoRD):\n    if WoRD in KeYworDs:\n        return WoRD\n    if WoRD in twISts:\n        nEW_WoRD = twISts[WoRD]\n    else:\n        nEW_WoRD = \'\'.join(c.upper() if random.random() < 0.5 else c.lower() for c in WoRD)\n        twISts[WoRD] = nEW_WoRD\n    return nEW_WoRD\n\n\ndef TWIsT(THE_sTR):\n    WORds = []\n    curr_wORD = []\n    for c in THE_sTR:\n        if c in \'.:()[] \\\\\\n\\\'\':\n            WORds.append(\'\'.join(curr_wORD))\n            curr_wORD = []\n            WORds.append(c)\n        else:\n            curr_wORD.append(c)\n    WORds.append(\'\'.join(curr_wORD))\n    # wE dON\'t care AbOut emptY \'WORds\'.\n    # ThiS can HappeN on \'\\n\\n\' aNd SimiLAR.\n    return \'\'.join(tWIst_worD(WoRD) for WoRD in WORds)\n\n\n# bUilDs A QuIne fROM A "MAGIC" STRinG.  NoTe THat SKipping THE `tWiSt`\n# iNVOcaTIon wOuld COnveRT tHiS inTo jUst A RegulAR QuIne.\n# (wiTh deAD coDe.)\ndef quIne_FRoM(MaGIc):\n    return MaGIc.format(repr(MaGIc))\n\n\ndef RUn():\n    TWiSTed_MAgiC = TWIsT(MAgic)\n    TwIsTed_qUiNe = quIne_FRoM(TWiSTed_MAgiC)\n    print(TwIsTed_qUiNe)\n\n\nRUn()\n'


# THe saMe VArIaBLE/fUnCtioN/WhATeVeR nAMe NeEdS to sTAY cONSistENt BETWeen
# DeFInItIon aNd UsEs.  sO mAKE sUrE THat During A SinglE EXeCUtION Of tHiS
# pROGRam, ONLY One Case-FLip Is proDuCeD.
twISts = dict()


def tWIst_worD(WoRD):
    if WoRD in KeYworDs:
        return WoRD
    if WoRD in twISts:
        nEW_WoRD = twISts[WoRD]
    else:
        nEW_WoRD = ''.join(c.upper() if random.random() < 0.5 else c.lower() for c in WoRD)
        twISts[WoRD] = nEW_WoRD
    return nEW_WoRD


def TWIsT(THE_sTR):
    WORds = []
    curr_wORD = []
    for c in THE_sTR:
        if c in '.:()[] \\\n\'':
            WORds.append(''.join(curr_wORD))
            curr_wORD = []
            WORds.append(c)
        else:
            curr_wORD.append(c)
    WORds.append(''.join(curr_wORD))
    # wE dON't care AbOut emptY 'WORds'.
    # ThiS can HappeN on '\n\n' aNd SimiLAR.
    return ''.join(tWIst_worD(WoRD) for WoRD in WORds)


# bUilDs A QuIne fROM A "MAGIC" STRinG.  NoTe THat SKipping THE `tWiSt`
# iNVOcaTIon wOuld COnveRT tHiS inTo jUst A RegulAR QuIne.
# (wiTh deAD coDe.)
def quIne_FRoM(MaGIc):
    return MaGIc.format(repr(MaGIc))


def RUn():
    TWiSTed_MAgiC = TWIsT(MAgic)
    TwIsTed_qUiNe = quIne_FRoM(TWiSTed_MAgiC)
    print(TwIsTed_qUiNe)


RUn()

