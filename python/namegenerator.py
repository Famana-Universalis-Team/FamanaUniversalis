import random

Plosives = ['p', 't', 'd', 'b', 'd', 'k', 'g', 'x', 'x']
Liquids = ['m', 'n', 'r', 's', 'z', 'w', 'v', 'f']
Vowels = ['e', 'i', 'o', 'a', 'e', 'i', 'o', 'a', 'ai', 'ei', 'ua', 'ea']

with open("NameListXalian.txt", "w") as f:
    f.write('')
for x in range(0,100):
    #define boolean tags
    endsWithVowel = False
    syllables = 0
    name = ''
    #generate syllabes
    roll = random.randint(1,100)
    print(roll)
    if roll >= 80:
        syllables = 4
    elif roll >= 50:
        syllables = 3
    elif roll >= 5:
        syllables = 2
    else:
        syllables = 1
        
    #now, assemble the word from the syllables
    for syl in range(0,syllables):
        #First, determine syllable structure.
        roll = random.randint(1,100)
        
        if roll >= 75 and endsWithVowel == False:
            structure = 0 #v
        elif roll >= 45:
            structure = 1 #cv
        elif roll >= 30 and endsWithVowel == False:
            structure = 2 #vl
        else:
            structure = 3 #cvl
        
        if structure == 0: #v
            name+=Vowels[random.randint(0,11)]
            endsWithVowel = True
        elif structure == 1: #cv
            if endsWithVowel == False: #then the last syllable ended with a liquid
                name+=Plosives[random.randint(0,8)]
            else:
                roll = random.randint(0,1)
                if roll == 0:
                    name+=Plosives[random.randint(0,8)]
                else:
                    name+=Liquids[random.randint(0,7)]
            name+=Vowels[random.randint(0,11)]
            endsWithVowel = True
        elif structure == 2: #vl
            name+=Vowels[random.randint(0,11)]
            name+=Liquids[random.randint(0,7)]
            endsWithVowel = False
        else: #cvl
            if endsWithVowel == False: #then the last syllable ended with a liquid
                name+=Plosives[random.randint(0,8)]
            else:
                roll = random.randint(0,1)
                if roll == 0:
                    name+=Plosives[random.randint(0,8)]
                else:
                    name+=Liquids[random.randint(0,7)]
            name+=Vowels[random.randint(0,11)]
            name+=Liquids[random.randint(0,7)]
            endsWithVowel = False
    name = name.replace("nm", "n")
    name = name.replace("mn", "n")
    name = name.replace("rr", "l")
    name = name.replace("mm", "m")
    name = name.replace("mr", "l")
    name = name.replace("rm", "l")
    print(name)
    #finally, write to file
    with open("NameListXalian.txt", "a") as f:
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