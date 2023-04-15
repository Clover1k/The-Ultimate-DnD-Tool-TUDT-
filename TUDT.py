import time
import random
import numpy as np
import pandas as pd

#Begins the code

print('Welcome to TUDT(The Ultimate D&D Tool)! this is three different tools that i have made all in one program! 3 in 1 you could say!')

while True:

    tudtchoose = input('Which Tool? 1.DCRNG(D&D Random Character Generator), 2.DDR(D&D Dice Roller), 3.DSF(D&D Stat Filler) 4.Exit ')

    if tudtchoose == '1':

        print('Hello and welcome to the Character Creator V1.2!')

        while True:

            slctrc = input('What race? 1.Gnome 2.Human 3.Orc 4.Tabaxi 5.Elf 6.Dragonborn: ')
            chrctrnm = input('What is the name of the character to be created? ')
            chrctrbkgrnd = input('What is this character\'s background? ')
            chrctrclss = input('What is the character\'s class? ')

    #Makes the random numbers

            traitnum = random.sample(range(1, 641), 3)
            traitnumf = iter(traitnum)

    #Output

            if slctrc == '1':
                gnomesize = np.random.uniform(3, 3.5)
                gnomeskincol = ['Reddish Tan', 'Brown', 'Grey-ish Tan']
                gnomebeardcol = ['Reddish Tan', 'Brown', 'Grey-ish Tan', 'White']
                gnomebeardcolfinal = random.randint(0, 3)
                gnomeskincolfinal = random.randint(0, 2)
                gnomesizefinal = round(gnomesize, 1)

                traitfr = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfr.iloc[0,0]} & {traitfr.iloc[1,0]} Gnome!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print('Eye Color: Blue')
                print(f'Size: {gnomesizefinal}ft')
                print(f'Skin Color: {gnomeskincol[gnomeskincolfinal]}')
                print(f'Beard color(If you want it to have a beard): {gnomebeardcol[gnomebeardcolfinal]}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break
            elif slctrc == '2':

                humanheight = np.random.uniform(5, 6.6)
                humanskincol = ['Black', 'White', 'Tan-ish', 'Caucasian']
                humanbeardcol = ['White', 'Black', 'Tan', 'Reddish Tan', 'Brown', 'Grey']
                humaneyecol = ['Blue', 'Gold', 'Yellow', 'Green', 'Brown']
                humanheightfinal = round(humanheight, 1)
                humanskincolfinal = random.randint(0, 3)
                humanbeardcolfinal = random.randint(0, 5)
                humaneyecolfinal = random.randint(0, 4)

                traitfrhuman = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfrhuman.iloc[0,0]} & {traitfrhuman.iloc[1,0]} Human!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print(f'Eye Color: {humaneyecol[humaneyecolfinal]}')
                print(f'Size: {humanheightfinal}ft')
                print(f'Skin Color: {humanskincol[humanskincolfinal]}')
                print(f'Beard color(If you want it to have a beard): {humanbeardcol[humanbeardcolfinal]}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break

            elif slctrc == '3':

                orcsize = np.random.uniform(6, 7.1)
                orcskincol = ['Grey', 'Grey-ish Green', 'Green', 'Blue-ish Grey']
                orceyecol = ['Grey', 'Black', 'Grey', 'Black', 'Green']
                orcbeardcol = ['Black', 'Tan', 'Reddish Tan', 'Brown', 'Grey']
                orcskincolfinal = random.randint(0, 3)
                orcbeardcolfinal = random.randint(0, 4)
                orceyecolfinal = random.randint(0, 4)
                orcsizefinal = round(orcsize, 1)

                traitfrorc = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfrorc.iloc[0,0]} & {traitfrorc.iloc[1,0]} Orc!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print(f'Eye Color: {orceyecol[orceyecolfinal]}')
                print(f'Size: {orcsizefinal}ft')
                print(f'Skin Color: {orcskincol[orcskincolfinal]}')
                print(f'Beard color(If you want it to have a beard): {orcbeardcol[orcbeardcolfinal]}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break

            elif slctrc == '4':

                tabaxisize = np.random.uniform(4, 6.9)
                tabaxifurcol = ['Tan', 'Lion-ish', 'Grey', 'Tortoise-Shell', 'Black', 'Orange Tabby', 'Grey Tabby', 'Siamese']
                tabaxieyecol = ['Yellow', 'Green', 'Blue', 'Brown']
                tabaxibeardcol = ['Tan', 'Black', 'Grey', 'Orange']
                tabaxisizefinal = round(tabaxisize, 1)
                tabaxifurcolfinal = random.randint(0, 7)
                tabaxibeardcolfinal = random.randint(0, 3)
                tabaxieyecolfinal = random.randint(0, 3)

                traitfrtabaxi = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfrtabaxi.iloc[0,0]} & {traitfrtabaxi.iloc[1,0]} Tabaxi!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print(f'Eye Color: {tabaxieyecol[tabaxieyecolfinal]}')
                print(f'Size: {tabaxisizefinal}ft')
                print(f'Skin Color: {tabaxifurcol[tabaxifurcolfinal]}')
                print(f'Beard color(If you want it to have a beard): {tabaxibeardcol[tabaxibeardcolfinal]}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break
        
            elif slctrc == '5':
        
                elfheight = np.random.uniform(4, 7.5)
                elfskincol = ['Copper', 'Bronze', 'Bluish', 'White']
                elfeyecol = ['Blue', 'Green', 'Gold']
                elfbeardcol = 'None(Elfs cannot have beards)'
                elfheightfinal = round(elfheight, 1)
                elfskincolfinal = random.randint(0, 3)
                elfeyecolfinal = random.randint(0, 2)

                traitfrelf = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfrelf.iloc[0,0]} & {traitfrelf.iloc[1,0]} Elf!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print(f'Eye Color: {elfeyecol[elfeyecolfinal]}')
                print(f'Size: {elfheightfinal}ft')
                print(f'Skin Color: {elfskincol[elfskincolfinal]}')
                print(f'Beard color(If you want it to have a beard): {elfbeardcol}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break

            elif slctrc == '6':

                dragonbornheight = np.random.uniform(6, 8.1)
                dragonbornskincol = ['Black', 'Blue', 'Bronze', 'Brass', 'Copper', 'Gold', 'Green', 'Red', 'Silver', 'White']
                dragonbornbeardcol = ['Tan', 'Black', 'Grey', 'Orange', 'White']
                dragonborneyecol = ['Red', 'Gold', 'Black']
                dragonbornheightfinal = round(dragonbornheight, 1)
                dragonbornskincolfinal = random.randint(0, 9)
                dragonbornbeardcolfinal = random.randint(0, 4)
                dragonborneyecolfinal = random.randint(0, 2)


                traitfrdrgn = pd.read_csv('psiblprsnaltys - Sheet1.csv', usecols=[0], skiprows=lambda x: x not in traitnum)

                print('Your character is... Drum roll please... Bum Bum Bum!')
                time.sleep(1)
                print(f'{chrctrnm} the {traitfrdrgn.iloc[0,0]} & {traitfrdrgn.iloc[1,0]} Dragonborn!')
                print(f'Class: {chrctrclss}')
                print(f'Background: {chrctrbkgrnd}')
                print('Specifics V')
                print(f'Eye Color: {dragonborneyecol[dragonborneyecolfinal]}')
                print(f'Size: {dragonbornheightfinal}ft')
                print(f'Skin Color: {dragonbornskincol[dragonbornskincolfinal]}')
                print(f'Beard color(If you want it to have a beard): {dragonbornbeardcol[dragonbornbeardcolfinal]}')
                rerun = input('Rerun? Y/N: ')

                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(1)
                    print(' ')
                elif rerun == 'N':
                    print('Thank You for using the Character Creator V1.2 Beta!')
                    break
                else:
                    print('INVALID INPUT')
                    break

            else:
                print('INVALID SELECTION, WHAT YOU SELECTED MAY STILL BE UNDER CONSTRUCTION')

    elif tudtchoose == '2':
        print('Welcome to DnD Dice Roller V1!')
        time.sleep(0.5)

        while True:

            whar = input('What die would you like to roll? 1.3 2.6 3.8 4.10 5.12 6.20 7.100: ')
            if whar == '1':
                rolls = int(input('How many times would you like to roll the d3? '))
                print('Calculating...')
                time.sleep(1)

                for i in range(rolls):
                    roll = random.randint(0, 3)
                    print(roll)
                    i+1

                rerun = input('Rerun? Y/N ')
                if rerun == 'Y':
                    print('Rerunning...')
                    time.sleep(0.5)
                elif rerun == 'N':
                    break

            if whar == '2':

                    rolls = int(input('How many times would you like to roll the d6? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 6)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        break

            if whar == '3':

                    rolls = int(input('How many times would you like to roll the d8? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 8)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        break

            if whar == '4':

                    rolls = int(input('How many times would you like to roll the d10? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 10)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        break

            if whar == '5':

                    rolls = int(input('How many times would you like to roll the d12? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 12)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        break

            if whar == '6':

                    rolls = int(input('How many times would you like to roll the d20? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 20)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        break

            if whar == '7':

                    rolls = int(input('How many times would you like to roll the d100? '))
                    print('Calculating...')
                    time.sleep(1)

                    for i in range(rolls):
                        roll = random.randint(0, 100)
                        print(roll)
                        i+1

                    rerun = input('Rerun? Y/N ')
                    if rerun == 'Y':
                        print('Rerunning...')
                        time.sleep(0.5)
                    elif rerun == 'N':
                        print('Thank you for using the DnD Dice Roller V1!')
                        time.sleep(0.5)
                        break

    elif tudtchoose == '3':
        strnam = 'Str(Strength)'
        dexnam = 'Dex(Dexterity)'
        connam = 'Con(Constitution)'
        intnam = 'Int(Intelligence)'
        wisnam = 'Wis(Wisdom)'
        chanam = 'Cha(Charisma)'

        standarray = [15, 14, 13, 12, 10, 8]

        print('Welcome to DSF(D&D Stat Filler) V1!')

        while True:

            print('Loading...')
            time.sleep(0.5)
            zerolocation = input(f'Where should 15 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if zerolocation == 'Str' or zerolocation == 'str' or zerolocation == 'Strength' or zerolocation == 'strength':
                standarray[0] = 'Str: 15, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif zerolocation == 'Dex' or zerolocation == 'dex' or zerolocation == 'Dexterity' or zerolocation == 'dexterity':
                standarray[0] = 'Dex: 15, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif zerolocation == 'Con' or zerolocation == 'con' or zerolocation == 'Constitution' or zerolocation == 'constitution':
                standarray[0] = 'Con: 15, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif zerolocation == 'Int' or zerolocation == 'int' or zerolocation == 'Intelligence' or zerolocation == 'intelligence':
                standarray[0] = 'Int: 15, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif zerolocation == 'Wis' or zerolocation == 'wis' or zerolocation == 'Wisdom' or zerolocation == 'wisdom':
                standarray[0] = 'Wis: 15, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif zerolocation == 'Cha' or zerolocation == 'cha' or zerolocation == 'Charisma' or zerolocation == 'charisma':
                standarray[0] = 'Cha: 15, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

        #Now 14 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            onelocation = input(f'Where should 14 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if onelocation == 'Str' or onelocation == 'str' or onelocation == 'Strength' or onelocation == 'strength':
                standarray[1] = 'Str: 14, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif onelocation == 'Dex' or onelocation == 'dex' or onelocation == 'Dexterity' or onelocation == 'dexterity':
                standarray[1] = 'Dex: 14, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif onelocation == 'Con' or onelocation == 'con' or onelocation == 'Constitution' or onelocation == 'constitution':
                standarray[1] = 'Con: 14, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif onelocation == 'Int' or onelocation == 'int' or onelocation == 'Intelligence' or onelocation == 'intelligence':
                standarray[1] = 'Int: 14, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif onelocation == 'Wis' or onelocation == 'wis' or onelocation == 'Wisdom' or onelocation == 'wisdom':
                standarray[1] = 'Wis: 14, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif onelocation == 'Cha' or onelocation == 'cha' or onelocation == 'Charisma' or onelocation == 'charisma':
                standarray[1] = 'Cha: 14, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

        #Now 13 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            twolocation = input(f'Where should 13 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if twolocation == 'Str' or twolocation == 'str' or twolocation == 'Strength' or twolocation == 'strength':
                standarray[2] = 'Str: 13, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif twolocation == 'Dex' or twolocation == 'dex' or twolocation == 'Dexterity' or twolocation == 'dexterity':
                standarray[2] = 'Dex: 13, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif twolocation == 'Con' or twolocation == 'con' or twolocation == 'Constitution' or twolocation == 'constitution':
                standarray[2] = 'Con: 13, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif twolocation == 'Int' or twolocation == 'int' or twolocation == 'Intelligence' or twolocation == 'intelligence':
                standarray[2] = 'Int: 13, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif twolocation == 'Wis' or twolocation == 'wis' or twolocation == 'Wisdom' or twolocation == 'wisdom':
                standarray[2] = 'Wis: 13, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif twolocation == 'Cha' or twolocation == 'cha' or twolocation == 'Charisma' or twolocation == twolocation == 'charisma':
                standarray[2] = 'Cha: 13, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

        #Now 12 Location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            threelocation = input(f'Where should 12 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if threelocation == 'Str' or threelocation == 'str' or threelocation == 'Strength' or threelocation == 'strength':
                standarray[3] = 'Str: 12, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif threelocation == 'Dex' or threelocation == 'dex' or threelocation == 'Dexterity' or threelocation == 'dexterity':
                standarray[3] = 'Dex: 12, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif threelocation == 'Con' or threelocation == 'con' or threelocation == 'Constitution' or threelocation == 'constitution':
                standarray[3] = 'Con: 12, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif threelocation == 'Int' or threelocation == 'int' or threelocation == 'Intelligence' or threelocation == 'intelligence':
                standarray[3] = 'Int: 12, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif threelocation == 'Wis' or threelocation == 'wis' or threelocation == 'Wisdom' or threelocation == 'wisdom':
                standarray[3] = 'Wis: 12, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif threelocation == 'Cha' or threelocation == 'cha' or threelocation == 'Charisma' or threelocation == threelocation == 'charisma':
                standarray[3] = 'Cha: 12, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

        # Now 10 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            fourlocation = input(f'Where should 10 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if fourlocation == 'Str' or fourlocation == 'str' or fourlocation == 'Strength' or fourlocation == 'strength':
                standarray[4] = 'Str: 10, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif fourlocation == 'Dex' or fourlocation == 'dex' or fourlocation == 'Dexterity' or fourlocation == 'dexterity':
                standarray[4] = 'Dex: 10, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif fourlocation == 'Con' or fourlocation == 'con' or fourlocation == 'Constitution' or fourlocation == 'constitution':
                standarray[4] = 'Con: 10, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif fourlocation == 'Int' or fourlocation == 'int' or fourlocation == 'Intelligence' or fourlocation == 'intelligence':
                standarray[4] = 'Int: 10, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif fourlocation == 'Wis' or fourlocation == 'wis' or fourlocation == 'Wisdom' or fourlocation == 'wisdom':
                standarray[4] = 'Wis: 10, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif fourlocation == 'Cha' or fourlocation == 'cha' or fourlocation == 'Charisma' or fourlocation == fourlocation == 'charisma':
                standarray[4] = 'Cha: 10, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

        # Now 8 location!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            finallocation = input(f'Where should 8 be? {strnam}, {dexnam}, {connam}, {intnam}, {wisnam}, or {chanam} ')

            if finallocation == 'Str' or finallocation == 'str' or finallocation == 'Strength' or finallocation == 'strength':
                standarray[5] = 'Str: 8, '
                strnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif finallocation == 'Dex' or finallocation == 'dex' or finallocation == 'Dexterity' or finallocation == 'dexterity':
                standarray[5] = 'Dex: 8, '
                dexnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif finallocation == 'Con' or finallocation == 'con' or finallocation == 'Constitution' or finallocation == 'constitution':
                standarray[5] = 'Con: 8, '
                connam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif finallocation == 'Int' or finallocation == 'int' or finallocation == 'Intelligence' or finallocation == 'intelligence':
                standarray[5] = 'Int: 8, '
                intnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif finallocation == 'Wis' or finallocation == 'wis' or finallocation == 'Wisdom' or finallocation == 'wisdom':
                standarray[5] = 'Wis: 8, '
                wisnam = 'UNAVAILABLE(ALREADY CHOSEN)'
            elif finallocation == 'Cha' or finallocation == 'cha' or finallocation == 'Charisma' or finallocation == 'charisma':
                standarray[5] = 'Cha: 8, '
                chanam = 'UNAVAILABLE(ALREADY CHOSEN)'
            else:
                print('INVALID')

            print('Final Stats! V')
            print( )
            print(f'{standarray[0]}{standarray[1]}{standarray[2]}{standarray[3]}{standarray[4]}{standarray[5]}')
            rerun = input('Rerun? Y/N ')
            if rerun == 'Y':
                strnam = 'Str(Strength)'
                dexnam = 'Dex(Dexterity)'
                connam = 'Con(Constitution)'
                intnam = 'Int(Intelligence)'
                wisnam = 'Wis(Wisdom)'
                chanam = 'Cha(Charisma)'
                print( )
            elif rerun == 'N':
                print('Thank you for using DSF V1!')
                break

    elif tudtchoose == '4':
        print('Thank You for using TUDT V1! Have a nice day!')
        break