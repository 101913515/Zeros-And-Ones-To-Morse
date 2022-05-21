#intended for personal/project use

#Ones and Zeros are used to create "morse code" to represent the dots and dashes of actual morse code

#The Ones represent the clicks while the Zeros repersents time between them where 0 would equal one second
#Hence: 3 zeros would seperate letters and 7 zeros would seperate words

#in that case 10111 would equal a dot dash and that would be "A"

#try creating a morse code number out of zeros and ones!
def Zeros_and_Ones_to_letters(dotsanddashes):
    # What this function does is that it takes a bunch of 0s and 1s that mimic dots and dashes and
    # converts them into letters and words

    # converts binary into Strings
    morse = str(dotsanddashes)

    # necessary varaibles
    x = 0
    m = 0
    mo = 0
    mw = 0
    morsetrans = ""
    morsevalue = None

    # Word Splitter(Uses the dots to split the numbers by spaces)
    morsesplitwords = morse.split("0000000")
    morsewordlen = len(morsesplitwords)

    # How we store the words/numbers
    morseword = list(range(9999999))

    # Execution Loop
    for i in range(morsewordlen):

        morsewords = morsesplitwords[mw]
        morsesplit = morsewords.split("000")
        morselen = len(morsesplit)
        x = 0

        for i in range(morselen):

            morse = morsesplit[x]
            morselength = len(morse)

            #Binary Tree that translated all the 0s and 1s into letters
            if morse[0] == "1":
                if morselength == 1:
                    morsevalue = ("E")
                if morselength == 3:
                    if morse[2] == "1" and morse[1] == "0":
                        morsevalue = ("I")
                    if morse[2] == "1" and morse[1] == "1":
                        morsevalue = ("T")
                if morselength == 5:
                    if morse[4] == "1" and morse[3] == "0" and morse[1] == "0":
                        morsevalue = ("S")
                    if morse[2] == "1" and morse[1] == "0" and morse[3] == "1" and morse[4] == "1":
                        morsevalue = ("A")
                    if morse[2] == "1" and morse[1] == "1" and morse[3] == "0" and morse[4] == "1":
                        morsevalue = ("N")
                if morselength == 7:
                    if morse[6] == "1" and morse[5] == "0" and morse[3] == "0" and morse[1] == "0":
                        morsevalue = ("H")
                    if morse[4] == "1" and morse[3] == "0" and morse[5] == "1" and morse[6] == "1" and morse[1] == "0":
                        morsevalue = ("U")
                    if morse[4] == "1" and morse[3] == "1" and morse[5] == "0" and morse[6] == "1":
                        morsevalue = ("R")
                    if morse[4] == "1" and morse[5] == "1" and morse[6] == "1" and morse[1] == "1":
                        morsevalue = ("M")
                    if morse[6] == "1" and morse[5] == "0" and morse[3] == "0" and morse[1] == "1":
                        morsevalue = ("D")
                if morselength == 9:
                    if morse[8] == "1" and morse[7] == "0" and morse[5] == "0" and morse[3] == "0" and morse[1] == "0":
                        morsevalue = ("5")
                    if morse[6] == "1" and morse[5] == "0" and morse[7] == "1" and morse[8] == "1" and morse[
                        3] == "0" and morse[1] == "0":
                        morsevalue = ("V")
                    if morse[6] == "1" and morse[5] == "1" and morse[7] == "0" and morse[8] == "1" and morse[1] == "0":
                        morsevalue = ("F")
                    if morse[6] == "1" and morse[5] == "0" and morse[7] == "0" and morse[8] == "1" and morse[3] == "1":
                        morsevalue = ("L")
                    if morse[6] == "1" and morse[5] == "0" and morse[7] == "1" and morse[8] == "1" and morse[3] == "1":
                        morsevalue = ("W")
                    if morse[6] == "1" and morse[5] == "1" and morse[7] == "0" and morse[8] == "1" and morse[1] == "1":
                        morsevalue = ("G")
                    if morse[8] == "1" and morse[7] == "0" and morse[5] == "0" and morse[3] == "0" and morse[1] == "1":
                        morsevalue = ("B")
                    if morse[6] == "1" and morse[5] == "0" and morse[7] == "1" and morse[8] == "1" and morse[
                        3] == "0" and morse[1] == "1":
                        morsevalue = ("K")
                if morselength == 11:
                    if morse[8] == "1" and morse[9] == "1" and morse[10] == "1" and morse[1] == "0":
                        morsevalue = ("4")
                    if morse[8] == "1" and morse[9] == "0" and morse[10] == "1" and morse[1] == "0" and morse[7] == "1":
                        morsevalue = ("P")
                    if morse[8] == "1" and morse[9] == "0" and morse[10] == "1" and morse[1] == "0" and morse[7] == "0":
                        morsevalue = ("&")
                    if morse[8] == "1" and morse[9] == "1" and morse[10] == "1" and morse[1] == "1" and morse[5] == "1":
                        morsevalue = ("O")
                    if morse[8] == "1" and morse[9] == "0" and morse[10] == "1" and morse[1] == "1" and morse[5] == "1":
                        morsevalue = ("Z")
                    if morse[8] == "1" and morse[9] == "0" and morse[10] == "1" and morse[1] == "1" and morse[
                        5] == "0" and morse[7] == "0":
                        morsevalue = ("6")
                    if morse[8] == "1" and morse[9] == "1" and morse[10] == "1" and morse[1] == "1" and morse[5] == "0":
                        morsevalue = ("X")
                    if morse[8] == "1" and morse[9] == "0" and morse[10] == "1" and morse[1] == "1" and morse[
                        5] == "0" and morse[7] == "1":
                        morsevalue = ("C")
                if morselength == 13:
                    if morse[10] == "1" and morse[11] == "1" and morse[12] == "1" and morse[3] == "0" and morse[
                        1] == "0":
                        morsevalue = ("3")
                    if morse[10] == "1" and morse[11] == "0" and morse[12] == "1" and morse[1] == "0":
                        morsevalue = ("+")
                    if morse[10] == "1" and morse[11] == "1" and morse[12] == "1" and morse[3] == "1":
                        morsevalue = ("J")
                    if morse[10] == "1" and morse[11] == "1" and morse[12] == "1" and morse[3] == "0" and morse[
                        1] == "1" and morse[5] == "1":
                        morsevalue = ("Q")
                    if morse[10] == "1" and morse[11] == "0" and morse[12] == "1" and morse[1] == "1" and morse[
                        9] == "0":
                        morsevalue = ("7")
                    if morse[10] == "1" and morse[11] == "1" and morse[12] == "1" and morse[3] == "0" and morse[
                        1] == "1" and morse[5] == "0" and morse[7] == "0":
                        morsevalue = ("=")
                    if morse[10] == "1" and morse[11] == "0" and morse[12] == "1" and morse[1] == "1":
                        morsevalue = ("/")
                    if morse[10] == "1" and morse[11] == "1" and morse[12] == "1" and morse[3] == "0" and morse[
                        1] == "1" and morse[5] == "0" and morse[7] == "1":
                        morsevalue = ("Y")
                if morselength == 15:
                    if morse[12] == "1" and morse[13] == "1" and morse[14] == "1" and morse[1] == "0":
                        morsevalue = ("2")
                    if morse[12] == "1" and morse[13] == "0" and morse[14] == "1" and morse[1] == "1" and morse[
                        5] == "1":
                        morsevalue = ("8")
                    if morse[12] == "1" and morse[13] == "0" and morse[14] == "1" and morse[1] == "0" and morse[
                        3] == "0":
                        morsevalue = ("?")
                    if morse[12] == "1" and morse[13] == "0" and morse[14] == "1" and morse[1] == "0" and morse[
                        3] == "1":
                        morsevalue = ('"')
                    if morse[12] == "1" and morse[13] == "0" and morse[14] == "1" and morse[1] == "1" and morse[
                        5] == "0":
                        morsevalue = ("(")
                    if morse[12] == "1" and morse[13] == "1" and morse[14] == "1" and morse[1] == "1":
                        morsevalue = ("-")
                if morselength == 17:
                    if morse[14] == "1" and morse[15] == "1" and morse[16] == "1" and morse[7] == "1" and morse[
                        3] == "1":
                        morsevalue = ("1")
                    if morse[14] == "1" and morse[15] == "0" and morse[16] == "1" and morse[13] == "1" and morse[
                        5] == "1":
                        morsevalue = ("9")
                    if morse[14] == "1" and morse[15] == "0" and morse[16] == "1" and morse[13] == "1" and morse[
                        5] == "0" and morse[1] == "1":
                        morsevalue = (";")
                    if morse[14] == "1" and morse[15] == "0" and morse[16] == "1" and morse[13] == "0":
                        morsevalue = (":")
                    if morse[14] == "1" and morse[15] == "1" and morse[16] == "1" and morse[7] == "0" and morse[
                        3] == "1":
                        morsevalue = (".")
                    if morse[14] == "1" and morse[15] == "1" and morse[16] == "1" and morse[7] == "0" and morse[
                        3] == "0":
                        morsevalue = ("_")
                    if morse[14] == "1" and morse[15] == "1" and morse[16] == "1" and morse[7] == "1" and morse[
                        3] == "0":
                        morsevalue = ("$")
                    if morse[14] == "1" and morse[15] == "0" and morse[16] == "1" and morse[13] == "1" and morse[
                        5] == "0" and morse[1] == "0":
                        morsevalue = ("@")
                if morselength == 19:
                    if morse[16] == "1" and morse[17] == "1" and morse[18] == "1" and morse[9] == "1":
                        morsevalue = ("0")
                    if morse[16] == "1" and morse[17] == "1" and morse[18] == "1" and morse[9] == "0" and morse[
                        5] == "1":
                        morsevalue = (",")
                    if morse[16] == "1" and morse[17] == "0" and morse[18] == "1" and morse[9] == "0":
                        morsevalue = ("'")
                    if morse[16] == "1" and morse[17] == "1" and morse[18] == "1" and morse[9] == "0" and morse[
                        5] == "0" and morse[11] == "0":
                        morsevalue = ("!")
                    if morse[16] == "1" and morse[17] == "1" and morse[18] == "1" and morse[9] == "0" and morse[
                        5] == "0" and morse[11] == "1":
                        morsevalue = (")")

            #proceeds to the next letter
            if morsevalue != None:
                morseword[m] = morsevalue
                m += 1
                morse = morsesplit[x]
                if m >= 1:
                    x += 1
                morselength = len(morse)
                morsevalue = None
        #proceeds to the next word
        if len(morsesplitwords) > 1:
            morseword[m] = " "
            m += 1
            mw += 1

    # Takes the stored information and puts them into a varaible to be returned
    for i in range(m):
        morsetrans += str(morseword[mo])
        mo += 1

    return (morsetrans)