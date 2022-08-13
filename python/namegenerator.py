import random

Stops = ["p", "t", "l", "b", "d", "g", "p", "t", "l", "b", "d", "g", "'"]
Sonorants = ["s", "f", "h", "m", "n", "j", "l", "w"]
ShortVowels = ["a", "e", "o", "u"]
LongVowels = ["á", "í", "ú", "ou", "au", "ia"]
Consonants = Stops+Sonorants

with open("NameListOppian.txt", "w") as f:
    f.write('')
for x in range(0,100):
    #define boolean tags
    endsWithVowel=False
    name=''
    
    #generate syllabes
    roll = random.randint(1,100)
    if roll >= 90:
        syllables = 4
    elif roll >= 55:
        syllables = 3
    elif roll >= 5:
        syllables = 2
    else:
        syllables = 1
        
    #now, assemble the word from the syllables
    for syl in range(0,syllables):
        if syl == syllables-2:
            stressedSyl = True
        else:
            stressedSyl = False
            
            
        #ONSET
        roll = random.randint(1,100)
        
        if roll >= 70 and endsWithVowel==False: #-
            name+=''
        elif roll >= 35: #C
            name+=random.choice(Consonants)
        elif roll >= 20: #PS
            name+=random.choice(Stops)
            name+=random.choice(Sonorants)
        elif roll >= 5: #SP
            name+=random.choice(Sonorants)
            name+=random.choice(Stops)
        else: #ZPS
            name+='s'
            name+=random.choice(Stops)
            name+=random.choice(Sonorants)
            
        #VOWEL
        if stressedSyl==True: #Stress
            name+=random.choice(LongVowels)
        else: #No Stress
            name+=random.choice(ShortVowels)
            
        #CODA
        roll = random.randint(0,2)
        
        if roll != 0: #-
            name+=''
            endsWithVowel = True
        else: #C
            name+=random.choice(Consonants)
        
    print(name)
    #finally, write to file
    with open("NameListOppian.txt", "a") as f:
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
    Coda: n (next syllable must begin with V), z, s, h, f, v, m, n, l, j
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
    Consonants: p, b, t, d, k, g, m, n, n, c, c', j, j', s, z, s', z', h, v, f, y, l, l', r
    Liquids: y, l, l', r
    Unvoiced Stops: p, t, k, c, j
    Voiced Stops: b, d, g, c', j'
    Unvoiced Fricatives: s, s', f, h
    Voiced Fricatives: m, n, n, z, z', v
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

'''Oppian - CCCVC based on latin
    Sibilants - s
    Stops - p, t, k, b, d, g, '
    Sonorants - s, f, h, m, n, j, l, w
    Short Vowels - a, e, o, u
    Long Vowels - á, í, ú, ou, au, ya
    
    Stress based system - stress always on panultimate syllable. Stressed syllables are long, unless the word is one syllable long.
    
    STRUCTURES:
    ONSET:
        - - 20
        C - 30
        PS - 20
        SP - 20
        ZPS - 10
    CODA:
        - - 50
        C - 50
'''