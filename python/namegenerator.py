import random

Liq = ["y", "l", "l", "r"]
UnStop = ["p", "t", "k", "c", "j"]
VoStops = ["b", "d", "g", "c", "j"]
UnFricative = ["s", "s", "f", "h"]
VoFricative = ["m", "n", "ñ", "z", "z", "v"]
VoSib = ["z", "z"]
UnSib = ["s", "s"]
ShortVowel = ["a", "e", "i", "o", "u", "y"]
LongVowel = ["á", "é", "í", "ó", "ú", "ý"]
Consonants = Liq + UnStop + VoStops + UnFricative + VoFricative

with open("NameListKachik.txt", "w") as f:
    f.write('')
for x in range(0,100):
    #define boolean tags
    endsWithVowel=False
    name=''
    weight = 0
    
    #generate syllabes
    roll = random.randint(1,100)
    if roll >= 88:
        syllables = 4
        syllyweight = 15
        weight+=20
    elif roll >= 55:
        syllables = 3
        syllyweight = 5
        weight+=10
    elif roll >= 5:
        syllables = 2
        syllyweight = 2
        weight+=4
    else:
        syllables = 1
        syllyweight = 0
        
    #now, assemble the word from the syllables
    for syl in range(0,syllables):
        deltaWeight = 0
        
        #ONSET
        roll = random.randint(1,100) + syllyweight + weight
        
        if roll >= 75 and endsWithVowel==False: #-
            name+=''
            deltaWeight += -10
        elif roll >= 35: #C
            name+=random.choice(Consonants)
        elif roll >= 25: #PF
            if (random.randint(0,1) == 1):
                name+=random.choice(UnStop)
                name+=random.choice(UnFricative)
            else:
                name+=random.choice(VoStops)
                name+=random.choice(VoFricative)
            deltaWeight += 5
        elif roll >= 20: #SPF
            if (random.randint(0,1) == 1):
                name+=random.choice(UnSib)
                name+=random.choice(UnStop)
                name+=random.choice(UnFricative)
            else:
                name+=random.choice(VoSib)
                name+=random.choice(VoStops)
                name+=random.choice(VoFricative)
            deltaWeight += 15
        elif roll >= 10: #PL
            name+=random.choice(VoStops)
            name+=random.choice(Liq)
            deltaWeight += 5
        elif roll >= 5: #SPL
            if (random.randint(0,1) == 1):
                name+=random.choice(VoSib)
            else:
                name+=random.choice(UnSib)
            name+=random.choice(VoStops)
            name+=random.choice(Liq)
            deltaWeight += 15
        else: #PFL
            name+=random.choice(VoStops)
            name+=random.choice(VoFricative)
            name+=random.choice(Liq)
            deltaWeight += 15
            
        #VOWEL
        roll = random.randint(1,100) + syllyweight + weight
        
        if (roll >= 50): #v
            name+=random.choice(ShortVowel)
        else: #vv
            name+=random.choice(LongVowel)
            deltaWeight += 5
            
        #CODA
        roll = random.randint(1,100) + syllyweight + weight
        
        if roll >= 60: #-
            name+=''
            endsWithVowel=True
            deltaWeight += -5
        elif roll >= 30: #C
            name+=random.choice(Consonants)
            endsWithVowel=False
        elif roll >= 20: #LP
            name+=random.choice(Liq)
            if (random.randint(0,1) == 1):
                name+=random.choice(UnStop)
            else:
                name+=random.choice(VoStops)
            endsWithVowel=False
            deltaWeight += 5
        elif roll >= 10: #FP
            if (random.randint(0,1) == 1):
                name+=random.choice(UnFricative)
                name+=random.choice(UnStop)
            else:
                name+=random.choice(VoFricative)
                name+=random.choice(VoStops)
            endsWithVowel=False
            deltaWeight += 5
        else: #LPF
            name+=random.choice(Liq)
            if (random.randint(0,1) == 1):
                name+=random.choice(UnFricative)
                name+=random.choice(UnStop)
            else:
                name+=random.choice(VoFricative)
                name+=random.choice(VoStops)
            endsWithVowel=False
            deltaWeight += 10
    
    print(name)
    weight+=deltaWeight
    #finally, write to file
    with open("NameListKachik.txt", "a") as f:
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
    
'''Fashran - OLVC based on finno-ugric and turkic languages
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
    
'''Jasuan - SFAVCF - based on english kinda
    Sonorants: s, z, sh, zh
    Approximants: l, w, j, r
    Stop-Fricatives: p, b, t, d, k, g, m, n, ng, f, v, th, sh, zh, s, z, h
    Consonants: p, b, t, d, k, g, m, n, ng, f, v, th, sh, zh, s, z, h, l, w, j, r
    Vowels: a, e, i, o, u, y
    Dithongs: ai, ao, ay, oi, ea, ua, ia
    Structures:
    ONSET:
        - - 30
        F - 30
        SF - 15
        FA - 15
        SFA - 10
    CODA:
        - - 25
        C - 25
        F - 25
        CF - 25
    VOWEL:
        Single = 75
        Dithong = 25 (rises to 50 if no coda)
'''

'''Kachik - CCCVCCC based on slavic languages
    Consonants: p, b, t, d, k, g, m, n, ñ, c, c', j, j', s, z, s', z', h, v, f, y, l, l', r
    Liquids: y, l, l', r
    Unvoiced Stops: p, t, k, c, j
    Voiced Stops: b, d, g, c', j'
    Unvoiced Fricatives: s, s', f, h
    Voiced Fricatives: m, n, ñ, z, z', v
    Short Vowels: a, e, i, o, u, y
    Long Vowels: á, é, í, ó, ú, ý
    Structures:
    ONSET:
        - - 25
        C - 40
        PF - 10
        SPF - 5
        PL - 10
        SPL - 5
        PFL - 5
    CODA:
        - - 40
        C - 30
        LP - 10
        FP - 10
        LPF - 10
'''