Health = 50
damage = 0
attack = 0
weapon = 0
PU =0
enterD = 0
A = 0
B = 0
C = 0
D = 0
E = 0
Z = 0
H = 0
enterB = 0
Armor = 0
enterC =0
Dust = 0
skeleton = 0
attack502 = 0
attack501 = 0
hallway = 0
chest = 0
GUU = 0
Convo = 0
Convo2 = 0
Convo3 = 0
warlock = 0

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "welcome to the dungeon!"
print "many enter, none leave."
print "you are the bravest adventurer which the king"
print "selected to rescue his daughter from"
print "the clutches of the evil warlock."
print "do you $G(*%# F*&EW E&(**&"
print "~~^&BG(%B(*)D(FV~TJ~~FTH~~~FT~~21~&~%*~^&"
print "**HAHAHAHA**"
print "**I aM ThE wARlOCk Of Brunhild**"
print "**YOu hAVE eNTEred mY dOMAin**"
print "**wElcOME To HeLl**"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "1. Hey you, come back here!"
print "2. (enter the dungeon)"
print "3. (chicken out)"
A = raw_input()
if A == "1":
    print "(you don't hear a response)"
    print "(you decide to enter the dungeon)"
    enterA = 1
if A == "2":
    print 'you enter the scary dungeon'
    enterA = 1
if A == "3":
    print "YoU ARe NoT ALloWEd tO LeaVE!"
    enterA = 1
    
if enterA == 1:
    print "(while you proceed into the darkness you hear an alarm blare)"
    print "an intruder has entered the dungeon!"
    print "an intruder has entered the dungeon!"
    print "an intruder has entered the dungeon!"
    print "an intruder has entered the dungeon!"
    print "(as you enter the first room you witness multiple weapons scattered)"
    print "(about the room a bow, a sword and a mace)"
    print "(you can only carry one so choose now)"
    B = raw_input()
    if B == "sword":
        weapon = 1
    if B == "mace":
        weapon = 2
    if B == "bow":
        weapon = 3 
    if weapon == 1:
        print "(you grab the sword and enter the hallway)"
        PU = 1
    if weapon == 2:
        print "(you grab the mace and enter the hallway)"
        PU = 1
    if weapon == 3:
        print "(you pick up the bow and enter the hallway)"
        PU = 1
    if PU == 1:
        print "(you enter the hallway and come to a split)"
        print "(Do you choose to go down the left hallway)"
        print "(Or do you choose the right hallway)" 
        C = raw_input()
        if C == "left":
            print "**WRonG HaLLwAy**"
            print "**HaVE A LitTLe FuN**"
            print "(As the warlock makes his statement, a bear)"
            print "(emerges from the darkness.)"
            print "(do you run away from the bear or fight the bear?)" 
            D = raw_input()
            if D == "run":
                print "(you get back to the split but the door is locked)"
                print "(you have no choice but to fight)"
                print "(your only weapon is your sword)"
                print "do you jab or slash the bear?"
                E = raw_input()
            if D == "fight":
             if weapon == 1:
                print "(you choose to fight the bear)"
                print "(your only weapon is your sword)"
                print "do you jab or slash the bear?"
                E = raw_input()
                if E == "jab":
                        print "You jab at the bear with all your might!"
                        print "The bear runs off bleeding back into the darkness"
                        print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                        print "**COnTInuE On yOuR PaTH**"
                        enterB = 1
                if E == "slash":
                        print "You slash at the bear with all your might!"
                        print "The bear runs off bleeding back into the darkness"
                        print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                        print "**COnTInuE On yOuR PaTH**"
                        enterB = 1
             if weapon == 2:
                    print "(you choose to fight the bear)"
                    print "(your only weapon is your mace)"
                    print "(do you club the bear or do you throw the mace)"
                    Z = raw_input()
                    if Z == "club":
                       print "You club the bear with all your might!"
                       print "The bear runs off bleeding back into the darkness"
                       print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                       print "**COnTInuE On yOuR PaTH**" 
                       enterB = 1
                    if Z == "throw":
                       print "You throw your mace at the bear with all your might!"
                       print "The bear runs off bleeding back into the darkness"
                       print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                       print "**COnTInuE On yOuR PaTH**" 
                       enterB = 1

            if weapon == 3:
                    print "(you choose to fight the bear)"
                    print "(your only weapon is your bow)"
                    print "(do you shoot the bear or hit it with your bow)"
                    H = raw_input()
                    if H == "shoot":
                       print "You shoot an arrow at the bear!"
                       print "The bear runs off bleeding back into the darkness"
                       print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                       print "**COnTInuE On yOuR PaTH**"
                       enterB = 1 
                    if H == "hit":
                       print "You hit the bear with your bow with all your might!"
                       print "The bear runs off bleeding back into the darkness"
                       print "**GOoD jOb You HAve DEfeAtEd mY bEaR**"
                       print "**COnTInuE On yOuR PaTH**"
                       enterB = 1 
        if C == "right":
            print "**COnGRAjuLaTioNS yOU HaVE CHoSeN ThE CoRRecT PatH**"
            print "**CoNTinUE**"
            enterB = 1
            if enterB == 1:
                print "(you enter another room with armor scattered about)"
                print "(you see some chainmail, some iron armor and some leather armor)"
                print "(choose some armor to protect your body)"
                Armor = raw_input()
                if Armor == "chainmail":
                    print "(as you pick up the armor it falls apart)" 
                    print "(you hear a banging at the door so you rush out without grabbing any other armor)"
                    enterC = 1
                    if Armor == "iron":
                        print "(you grab the iron aromor but it is welded to the floor)"
                        print "(you hear a banging at the door as it collapses)"
                        print "(you rush out of the room without grabbing any other armor)"
                        enterC = 1
                    if Armor == "leather":
                        print "(your grab the leather armor and it fits perfectly)"
                        print "(you hear a banging at the door and rush out of the room)" 
                        enterC = 2
                    if enterC == 1:
                            print "**I SeE YoU ChoSe mY cUrSEd ARmoR**"
                            print "**GoOd LUck GeTtIng THRouGh ThE ResT Of thE DUnGeOn**"
                            enterD = 1
                    if enterC == 2:
                            print "**GoOd JoB ChOosINg tHe CoRrect ARmOR**"
                            enterD = 1
                    
                    if enterD == 1:
                        print "(you come across some white dust on the ground, do you investigate it or jump over it?)"
                        Dust = raw_input()
                        if Dust == "investigate":
                            skeleton = 1
                        if Dust == "jump":
                            skeleton = 2
                        if skeleton == 1 and weapon == 1:
                                print "(A skeleton rises out of the dust)"
                                print "(you use your sword and prepare to fight)"
                                print "(do you jab or slash?)"
                                attack == raw_input()
                                if attack == "jab":
                                    print "(you jab at the skeleton but your sword goes through the skeleton)"
                                    print "(the skeleton grabs a hold of your neck and strangles you to death)"
                                    print "**Oh POoR BOY YoU HAVE BEeN KILlED**"
                                    print "**LOoKs LiKE THe KING WILl NeVER GEt HIs DAUGHTER BAcK**"
                                    print "The story here ends for you. The End."
                                if attack == "slash":
                                    print "(you slash the skeleton and it crumbles into a pile of bones)"
                                    print "(you walk over the bones as they fall back into dust)"
                                    hallway = 3
                        if skeleton == 1 and weapon == 3:
                                print "(A skeleton rises out of the dust)"
                                print "You back up and draw your bow"
                                print "the skeleton gives you a menacing look"
                                print "do you charge and hit the skeleton with the bow or keep your distance and shoot an arrow?"
                                print "charge or shoot?"
                                attack502 = raw_input()
                                if attack502 == "charge":
                                    print "you charge and slam into the skeleton and it falls apart and crumbles into dust"
                                    hallway = 3
                                if attack502 == "shoot":
                                    print "you shoot an arrow and it soars through the rib cage of the skeleton"
                                    print "the skeleton charges and strangles you to death"
                                    print "**DO YOU ReALLy THiNK You WOULd BE A GoOD ShOT AFtER JuST PIcKInG UP THaT BoW**"
                                    print "**LOoKs LiKE THe KING WILl NeVER GEt HIs DAUGHTER BAcK**"
                                    print "The story here ends for you. The End."
                        if skeleton == 1 and weapon == 2:
                                print "(A skeleton rises out of the dust)"
                                print "(you use your mace and prepare to fight)"
                                print "(do you swing or throw the mace?)"
                                attack501 = raw_input()
                                if attack501 == "swing":
                                    print " You swing your large mace at the skeleton and it smashes through him, crumbling him to dust."
                                    hallway = 3
                                if attack501 == "throw":
                                    print "You manage to throw your mace but you accidentily miss the skeleton."
                                    print "The skeleton charges and strangles you to death."
                                    print "**Oh POoR BOY YoU HAVE BEeN KILlED**"
                                    print "**LOoKs LiKE THe KING WILl NeVER GEt HIs DAUGHTER BAcK**"
                                    print "The story here ends for you. The End."
                        if skeleton == 2:
                            print "(you step over the pile of dust and continue on your path)"
                            print "(skeleton rises up out of the dust behind you but you handle him with ease)"
                            hallway = 4
                        if hallway == 3:
                            print "**CONGraJulAtIOnS You HAve DEfeAtEd THe SKEleTon ThAt gAURds tHE KEy tO My-**"
                            print "**Oh MY I HAvE SaID TO MuCH**"
                            print "**COnTInuE On THe PaTH**"
                            hallway = 4
                        if hallway == 4:
                                print "(as you walk down the hallway you come across a room with a sole chest in the middle of the room)"
                                print "(do you wish to open the chest or exit the room)"
                                chest = raw_input()
                                if chest == "open":
                                    print "(as you go to open the chest a large beast come out of the darkness)"
                                    print "(you pull out your weapon ready to fight)"
                                    if weapon == "1":
                                        print "(do you jab or slash at the large beast?)"
                                        GUU = raw_input()
                                        if GUU == "jab":
                                            print "(as you jab at the beast it shouts out)"
                                            print "NONONONONONO please don't hurt me"
                                            print "1.What! you can talk"
                                            print "2.Shut up let me kill you"
                                            print "3.help me open this chest or I'll kill you"
                                            Convo = raw_input()
                                            if Convo == "1":
                                                print "The warlock put a curse on me"
                                                print "1.What do you mean curse"
                                                print "2.If you help me save the princess i will help you"
                                                print "3.How do I know you aren't lying"
                                                Convo2 = raw_input()
                                                if Convo2 == "1":
                                                    print "I used to be a servant for the warlock" 
                                                    print "but I fell in love with his wife and she the same, so he banished me a dog into the depths of this cavern."
                                                if Convo2 == "2":
                                                    print "Alright, Alright, I'll help you"
                                                if Convo2 == "3":
                                                    print "I would help you if I could but this chest is for the key holder only."
                                                    print "   "
                                                    print "1.I thought the skeleton out there gaurded the key where is it?"
                                                    print "2.Your large enough, just squash it"
                                                    print "3.Fine then help me find it"
                                                    Convo3 = raw_input() 
                                                    if Convo3 == "1":
                                                        print "What you defeated the skeleton, oh! Key holder open the chest"
                                                        print "(as you go to open the chest you hear the warlock)"
                                                        print "**no please don't oPen that chest**"
                                                        print "**it conTains my soul and if open I shall die**"
                                                        print "1.then tell me why I can't open it"
                                                        print "2.then why don't you come and fight me"
                                                        F = raw_input()
                                                        if F == "1":
                                                            print "**because Then you will never get your princess back**"
                                                            print "Well then come get us!!!"
                                                            warlock = 1
                                                        if F == "2":
                                                            print "**I'm no wArlock"
                                                            warlock = 1
                                                        if warlock  == "1":
                                                            print"(an old man enters the room)"
                                                            print "**Here I am not a warlock nor Supreme ruleR of the kingdom**"
                                                            print "**No NO I WoN't TeLL TheM WHo You ARe, No PleASe!"
                                                            print "(The old man fell to the ground, dead)"
                                                            print "(As soon as the Warlock dies a door opens, It's The Princess)"
                                                            print "Congrajulations You Have Won"
                                                            print "Thanks For Playing"
                                                    if Convo3 == "2":
                                                        print "I'm sorry I can't do that"
                                                        print "The only way to open it is to kill the skeleton"
                                                        print "('but I did kill the skeleton')"
                                                        print "What you defeated the skeleton, oh! Key holder open the chest"
                                                        print "(as you go to open the chest you hear the warlock)"
                                                        print "**no please don't oPen that chest**"
                                                        print "**it conTains my soul and if open I shall die**"
                                                        print "1.then tell me why I can't open it"
                                                        print "2.then why don't you come and fight me"
                                                        F = raw_input()
                                                        if F == "1":
                                                            print "**because Then you will never get your princess back**"
                                                            print "Well then come get us!!!"
                                                            warlock = 1
                                                        if F == "2":
                                                            print "**I'm no wArlock"
                                                            warlock = 1
                                                        if warlock  == "1":
                                                            print"(an old man enters the room)"
                                                            print "**Here I am not a warlock nor Supreme ruleR of the kingdom**"
                                                            print "**No NO I WoN't TeLL TheM WHo You ARe, No PleASe!"
                                                            print "(The old man fell to the ground, dead)"
                                                            print "(As soon as the Warlock dies a door opens, It's The Princess)"
                                                            print "Congrajulations You Have Won"
                                                            print "Thanks For Playing"
                                                    if Convo3 == "3":
                                                         print "I'm sorry I can't do that"
                                                         print "The only way to open it is to kill the skeleton"
                                                         print "('but I did kill the skeleton')"
                                                         print "What you defeated the skeleton, oh! Key holder open the chest"
                                                         print "(as you go to open the chest you hear the warlock)"
                                                         print "**no please don't oPen that chest**"
                                                         print "**it conTains my soul and if open I shall die**"
                                                         print "1.then tell me why I can't open it"
                                                         print "2.then why don't you come and fight me"
                                                         F = raw_input()
                                                         if F == "1":
                                                            print "**because Then you will never get your princess back**"
                                                            print "Well then come get us!!!"
                                                            warlock = 1
                                                         if F == "2":
                                                            print "**I'm no wArlock"
                                                            warlock = 1
                                                         if warlock  == "1":
                                                            print"(an old man enters the room)"
                                                            print "**Here I am not a warlock nor Supreme ruleR of the kingdom**"
                                                            print "**No NO I WoN't TeLL TheM WHo You ARe, No PleASe!"
                                                            print "(The old man fell to the ground, dead)"
                                                            print "(As soon as the Warlock dies a door opens, It's The Princess)"
                                                            print "Congrajulations You Have Won"
                                                            print "Thanks For Playing"
                                            if Convo == "2":
                                                print "I'm Sorry but You Leave Me No Choice"
                                                print "**Oh POoR BOY YoU HAVE BEeN KILlED**"
                                                print "**LOoKs LiKE THe KING WILl NeVER GEt HIs DAUGHTER BAcK**"
                                                print "The story here ends for you. The End."
                                            if Convo == "3":
                                                 print "I'm sorry I can't do that"
                                                 print "The only way to open it is to kill the skeleton"
                                                 print "('but I did kill the skeleton')"
                                                 print "What you defeated the skeleton, oh! Key holder open the chest"
                                                 print "(as you go to open the chest you hear the warlock)"
                                                 print "**no please don't oPen that chest**"
                                                 print "**it conTains my soul and if open I shall die**"
                                                 print "1.then tell me why I can't open it"            
                                                 print "2.then why don't you come and fight me"
                                                 F = raw_input()
                                                 if F == "1":
                                                            print "**because Then you will never get your princess back**"
                                                            print "Well then come get us!!!"
                                                            warlock = 1
                                                 if F == "2":
                                                            print "**I'm no wArlock"
                                                            warlock = 1
                                                 if warlock  == "1":
                                                            print"(an old man enters the room)"
                                                            print "**Here I am not a warlock nor Supreme ruleR of the kingdom**"
                                                            print "**No NO I WoN't TeLL TheM WHo You ARe, No PleASe!"
                                                            print "(The old man fell to the ground, dead)"
                                                            print "(As soon as the Warlock dies a door opens, It's The Princess)"
                                                            print "Congrajulations You Have Won"
                                                            print "Thanks For Playing" 