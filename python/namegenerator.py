import random

Liq = ['m', 'n', 'r', 's', 'z']
ObsVl = ['t', 'p', 'k', 'c']
ObsVd = ['d', 'b', 'g', 'ğ']
vow = ['a', 'e', 'i', 'o', 'u', 'y']
dith = ['ai', 'ei', 'yo', 'yu']

with open("NameListMaxan.txt", "w") as f:
    f.write('')
for x in range(0,100):
    #define boolean tags
    endsWithVowel = False
    voicedEnding = False
    consonantEnding = False
    syllables = 0
    name = ''
    weight = 0
    #generate syllabes
    roll = random.randint(1,100)
    print(roll)
    if roll >= 95:
        syllables = 4
    elif roll >= 75:
        syllables = 3
    elif roll >= 30:
        syllables = 2
    else:
        syllables = 1
        
    #now, assemble the word from the syllables
    for syl in range(0,syllables):
        #First, determine syllable structure.
        roll = random.randint(1,100)
        
        if syllables == 4:
            weight = 40
        elif syllables == 3:
            weight = 15
    
        if roll >= 80 and endsWithVowel == False and syllables != 1:
            structure = 0 #v
            endsWithVowel = True
            weight = 0
        elif roll >= 60-(weight/2) and syllables != 1:
            structure = 1 #cv
            endsWithVowel = True
            weight = 0
        elif roll >= 40-weight and endsWithVowel == False and syllables != 1:
            structure = 2 #vc
            endsWithVowel = False
            weight = 0
        else:
            structure = 3 #cvc
            endsWithVowel = False
            weight = 10
        
        if structure == 0: #v
            roll = random.randint(0,3)
            if roll == 0:
                name+=dith[random.randint(0,3)]
            else:
                name+=vow[random.randint(0,5)]
            voicedEnding = False
            consonantEnding = False
        elif structure == 1: #cv
            roll = random.randint(0,2)
            if roll == 1 and voicedEnding == False and consonantEnding == False:
                name+=ObsVl[random.randint(0,3)]
            elif roll == 2 and consonantEnding == False:
                name+=ObsVd[random.randint(0,3)]
            else:
                name+=Liq[random.randint(0,4)]
            roll = random.randint(0,3)
            if roll == 0:
                name+=dith[random.randint(0,3)]
            else:
                name+=vow[random.randint(0,5)]
            voicedEnding = False
            consonantEnding = False
        elif structure == 2: #vc
            roll = random.randint(0,3)
            if roll == 0:
                name+=dith[random.randint(0,3)]
            else:
                name+=vow[random.randint(0,5)]
            roll = random.randint(0,2)
            if roll == 1:
                name+=ObsVl[random.randint(0,3)]
                voicedEnding = False
                consonantEnding = True
            elif roll == 2:
                name+=ObsVd[random.randint(0,3)]
                voicedEnding = True
                consonantEnding = True
            else:
                name+=Liq[random.randint(0,4)]
                voicedEnding = True
                consonantEnding = False
        else: #cvc
            roll = random.randint(0,2)
            if roll == 1 and voicedEnding == False and consonantEnding == False:
                name+=ObsVl[random.randint(0,3)]
            elif roll == 2 and consonantEnding == False:
                name+=ObsVd[random.randint(0,3)]
            else:
                name+=Liq[random.randint(0,4)]
            name+=vow[random.randint(0,5)]
            roll = random.randint(0,2)
            if roll == 1:
                name+=ObsVl[random.randint(0,3)]
                voicedEnding = False
                consonantEnding = True
            elif roll == 2:
                name+=ObsVd[random.randint(0,3)]
                voicedEnding = True
                consonantEnding = True
            else:
                name+=Liq[random.randint(0,4)]
                voicedEnding = True
                consonantEnding = False
    name = name.replace("nm", "n")
    name = name.replace("mn", "n")
    name = name.replace("rr", "l")
    name = name.replace("mm", "m")
    name = name.replace("mr", "l")
    name = name.replace("rm", "l")
    print(name)
    #finally, write to file
    with open("NameListMaxan.txt", "a") as f:
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