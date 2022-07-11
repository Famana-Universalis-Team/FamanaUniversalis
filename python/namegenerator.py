import random

Obs = ["p", "t", "k", "q", "z", "s", "ç", "qh"]
Son = ["h", "f", "v", "m", "n", "l", 'v']
Liq = ["l", "f", 'r']
Coda = ["ñ", "z", "s", "h", "f", "v", "m", "n", "l", "j"]
Plos = ["p", "t", "k", "q", "'", "ç", "qy"]
FrontV = ["a", "e", "a", "e", "i", "y", "ai"]
BackV = ["o", "u", "o", "u", "ü", "ö", "ï", "ou"]

with open("NameListRavsho.txt", "w") as f:
    f.write('')
for x in range(0,100):
    #define boolean tags
    weight = 0
    endsWithVowel = False
    syllables = 0
    name = ''
    frontBased = False
    backBased = False
    #generate syllabes
    roll = random.randint(1,100)
    print(roll)
    if roll >= 88:
        syllables = 4
        syllyweight = 10
    elif roll >= 55:
        syllables = 3
        syllyweight = 5
    elif roll >= 5:
        syllables = 2
        syllyweight = 2
    else:
        syllables = 1
        syllyweight = 0
        
    #now, assemble the word from the syllables
    for syl in range(0,syllables):\
        #First, determine syllable structure.
        roll = random.randint(1,100) + weight + syllyweight
        
        if roll >= 90 and endsWithVowel==False:
            structure = 0 #v
            weight = 0
        elif roll >= 78:
            structure = 1 #ov
        elif roll >= 72:
            structure = 2 #sv
        elif roll >= 57:
            structure = 3 #olv
        elif roll >= 53 and endsWithVowel==False:
            structure = 4 #vc
        elif roll >= 49 and endsWithVowel==False:
            structure = 5 #vp
        elif roll >= 39:
            structure = 6 #ovc
            weight = 5
        elif roll >= 29:
            structure = 7 #svc
            weight = 5
        elif roll >= 22:
            structure = 8 #olvc
            weight = 5
        elif roll >= 15:
            structure = 9 #ovp
            weight = 10
        elif roll >= 5:
            structure = 10 #svp
            weight = 10
        else:
            structure = 11 #olvp
            weight = 10
        
        if structure == 0: #v
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            endsWithVowel=True
        elif structure == 1: #ov
            name+=Obs[random.randint(0,7)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            endsWithVowel=True
        elif structure == 2: #sv
            name+=Son[random.randint(0,6)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            endsWithVowel=True
        elif structure == 3: #olv
            name+=Obs[random.randint(0,7)]
            name+=Liq[random.randint(0,2)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            endsWithVowel=True
        elif structure == 4: #vc
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Coda[random.randint(0,9)]
            endsWithVowel=False
        elif structure == 5: #vp
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Plos[random.randint(0,6)]
            endsWithVowel=False
        elif structure == 6: #ovc
            name+=Obs[random.randint(0,7)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Coda[random.randint(0,9)]
            endsWithVowel=False
        elif structure == 7: #svc
            name+=Son[random.randint(0,6)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Coda[random.randint(0,9)]
            endsWithVowel=False
        elif structure == 8: #olvc
            name+=Obs[random.randint(0,7)]
            name+=Liq[random.randint(0,2)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Coda[random.randint(0,9)]
            endsWithVowel=False
        elif structure == 9: #ovp
            name+=Obs[random.randint(0,7)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Plos[random.randint(0,6)]
            endsWithVowel=False
        elif structure == 10: #svp
            name+=Son[random.randint(0,6)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Plos[random.randint(0,6)]
            endsWithVowel=False
            endsWithVowel=False
        else: #olvp
            name+=Obs[random.randint(0,7)]
            name+=Liq[random.randint(0,2)]
            if (random.randint(0,1) == 1 or frontBased == True) and backBased != True:
                name+=FrontV[random.randint(0,6)]
                frontBased = True
                backBased = False
            else:
                name+=BackV[random.randint(0,7)]
                frontBased = False
                backBased = True
            name+=Plos[random.randint(0,6)]
            endsWithVowel=False
    name = name.replace("zf", "zv")
    
    name = name.replace("pç", "ç")
    name = name.replace("tç", "ç")
    name = name.replace("kç", "ç")
    name = name.replace("qç", "ç")
    name = name.replace("'ç", "ç")
    name = name.replace("çç", "ç")
    name = name.replace("qyç", "ç")
    name = name.replace("zç", "ç")
    name = name.replace("sç", "ç")
    name = name.replace("çp", "ç")
    name = name.replace("çt", "ç")
    name = name.replace("çk", "ç")
    name = name.replace("çq", "ç")
    name = name.replace("çz", "ç")
    name = name.replace("çs", "ç")
    name = name.replace("çs", "ç")
    name = name.replace("çç", "ç")
    name = name.replace("ç'", "ç")
    
    name = name.replace("pqy", "qy")
    name = name.replace("tqy", "qy")
    name = name.replace("kqy", "qy")
    name = name.replace("qqy", "qy")
    name = name.replace("'qy", "qy")
    name = name.replace("qyç", "qy")
    name = name.replace("qyqy", "qy")
    name = name.replace("zqy", "qy")
    name = name.replace("sqy", "qy")
    name = name.replace("qyp", "qy")
    name = name.replace("qyt", "qy")
    name = name.replace("qyk", "qy")
    name = name.replace("qyq", "qy")
    name = name.replace("qyz", "qy")
    name = name.replace("qys", "qy")
    name = name.replace("çqy", "qy")
    name = name.replace("qyqy", "qy")
    name = name.replace("qy'", "qy")
    
    name = name.replace("pp", "pt")
    name = name.replace("tp", "pt")
    name = name.replace("kp", "pt")
    name = name.replace("qp", "pt")
    name = name.replace("'p", "pt")
    name = name.replace("zp", "pt")
    name = name.replace("sp", "pt")
    name = name.replace("pp", "pt")
    name = name.replace("pt", "pt")
    name = name.replace("pk", "pt")
    name = name.replace("pq", "pt")
    name = name.replace("pz", "pt")
    name = name.replace("ps", "pt")
    name = name.replace("p'", "pt")
    
    name = name.replace("tt", "tk")
    name = name.replace("kt", "tk")
    name = name.replace("qt", "tk")
    name = name.replace("'t", "tk")
    name = name.replace("zt", "tk")
    name = name.replace("st", "tk")
    name = name.replace("tt", "tk")
    name = name.replace("tk", "tk")
    name = name.replace("tq", "tk")
    name = name.replace("tz", "tk")
    name = name.replace("ts", "tk")
    name = name.replace("t'", "tk")
    
    name = name.replace("kk", "kh")
    name = name.replace("qk", "kh")
    name = name.replace("'k", "kh")
    name = name.replace("zk", "kh")
    name = name.replace("sk", "kh")
    name = name.replace("tk", "kh")
    name = name.replace("kq", "kh")
    name = name.replace("kz", "kh")
    name = name.replace("ks", "kh")
    name = name.replace("k'", "kh")
    
    name = name.replace("qq", "q'")
    name = name.replace("'q", "q'")
    name = name.replace("zq", "q'")
    name = name.replace("sq", "q'")
    name = name.replace("tq", "q'")
    name = name.replace("qq", "q'")
    name = name.replace("qz", "q'")
    name = name.replace("qs", "q'")
    name = name.replace("q'", "q'")
    
    name = name.replace("''", "'")
    name = name.replace("z'", "z")
    name = name.replace("s'", "s")
    name = name.replace("'z", "z")
    name = name.replace("'s", "s")
    name = name.replace("''", "'")
    
    name = name.replace("zz", "z")
    name = name.replace("sz", "s")
    name = name.replace("ss", "s")
    name = name.replace("zs", "z")
    
    print(name)
    #finally, write to file
    with open("NameListRavsho.txt", "a") as f:
        f.write(f'{name.title()} ')
        
        
###past here its just linguistic notes i used to generate each nameset

'''MAXAN = CVC
    Rules: presumably includes aspirated. Voice or aspirate obstruents inbetween vowels and liquids voice obstruents (mt -> md). Dont add two obstruents in a row.
    Stress is on first syllable if voiced obstruent; else on last
    Names appear to include consonants m, n, b, d, t, p, g, k, r, kh, c (/c/ i assume), q, s, z
    vowels seem to do the slavic thing where [y] is a vowel, probably the schwa or u, maybe functioning as the half-vowel /j/ from time to time
    long vowels seem to just be implied
    yo, ei, yu, ill also add ai cause its common
        Liq = ['m', 'n', 'r', 'c', 's', 'z']
        ObsVl = ['t', 'p', 'k', 'c']
        ObsVd = ['d', 'b', 'g', 'kh']
        Vow = ['a', 'e', 'i', 'o', 'u', 'y']
    syllables = 1-4 at 30%, 45%, 20%, 5% distribution
    structure is CVC, VC, CV, V at 40, 20, 20, 20
    two vowels cannot follow each other'''
    
'''XALIAN - CVL
    Words seem to include x, l, k, m, n, t, p, s, z, j, g (kh?), d, b, w, v, f
    Vowels: i, a, o, e
    Dithongs: ea, ua (wa), ei, ai
    structure is V, CV, VL, CVL at 25, 30, 20, 25'''
    
'''Fashran - OLVC
    We have free reign pretty much, so:
    Obstruent Onset: p, t, k, q, z, s, ç, qy
    Sonorant Onset: h, f, v, m, n, l, j
    Onset liquid if obstruent: l, j, f (v if z). Only if obstruent onset
    Coda: ñ (next syllable must begin with V), z, s, h, f, v, m, n, l, j
    Plosive Coda: p, t, k, q, ', ç, qy
        Plosive clusters must always be front to back -> ie. pt, tk, kq, q' are allowed but say, pq or kt aren't. Affricates don't form clusters.
    Front vowels: a, e, i, y, ÿ, ai
    Back vowels: o, u, ü, ö, î, ou
    Agreement is broken by OLV(C) structures only.
    Structures:
    V - 10
    OV - 12
    SV - 6
    OLV - 15
    VC - 4
    VP - 4
    OVC - 10
    SVC - 10
    OLVC - 7
    OVP - 7
    SVP - 10
    OLVP - 5
    '''