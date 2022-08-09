import random

Son = ["s", "z", "sh", "zh"]
App = ["l", "w", "y", "r"]
StpFr = ["p", "b", "t", "d", "k", "g", "m", "n", "ng", "f", "v", "th", "sh", "zh", "s", "z", "h", "c"]
Con = StpFr + App
Vow = ["a", "e", "i", "o", "u", "y"]
Dith = ["ai", "ao", "ay", "oi", "ea", "ua", "ia"]

with open("NameListJasuan.txt", "w") as f:
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
        
        if roll >= 70 and endsWithVowel==False: #-
            name+=''
            deltaWeight+=-5
        elif roll >= 40: #f
            name+=random.choice(StpFr)
        elif roll >= 25: #s
            name+=random.choice(Son)
        elif roll >= 10: #fa
            name+=random.choice(StpFr)
            name+=random.choice(App)
            deltaWeight+=5
        else: #sfa
            name+=random.choice(Son)
            name+=random.choice(StpFr)
            name+=random.choice(App)
            deltaWeight+=10
            
        #VOWEL
        codaRoll = random.randint(1,100) + syllyweight + weight
        roll = random.randint(1,100) + syllyweight + weight
        
        if (roll >= 25 and not codaRoll >= 75) or (roll >= 50): #v
            name+=random.choice(Vow)
        else: #d
            name+=random.choice(Dith)
            deltaWeight+=5
            
        #CODA
        roll = codaRoll
        
        if roll >= 75: #-
            name+=''
            endsWithVowel = True
            deltaWeight+=-15
        elif roll >= 50: #C
            name+=random.choice(Con)
            endsWithVowel = False
        elif roll >= 25: #F
            name+=random.choice(StpFr)
            endsWithVowel = False
        else: #CF
            name+=random.choice(Con)
            name+=random.choice(StpFr)
            endsWithVowel = False
            deltaWeight+=15
    
    print(name)
    weight+=deltaWeight
    #finally, write to file
    with open("NameListJasuan.txt", "a") as f:
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
        
        Zavum Brash Evibshem Poineb Ezhse Icamisu Elinze Finga Sroithus Upazh Bypai Aszav Kizhi Uko Koithia Ozuth Ucith Ethode Unezan Azaysav Bolgoi Apoko Akuacor Ekupo Ashusove Shatab Nathay Thay Fovers Obama Ogro Plakill
Shrumgyi Kuvia Izengozi Bemaizh Fophi Ekopsu Sumu Athea
Tyofim Usiste Thayzoz Fythpil Sayshly Krumef Dloberg Sisao Nozygate Athydakat Upar Azobaythis Oshysbo Syhozh Shushec Dishgay Apitag Sazhikuzh Fella Astauand
'''

