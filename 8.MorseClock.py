#!/usr/bin/python

def morse(num, mode, num1, num2):
    """ Takes in a number and mode(H,M,S) returns More string """
    #Foramt: .. ....
    s1 = bin(int(str(num)[0]))[2:]
    s2 = bin(int(str(num)[1]))[2:]
    if len(s1) < num1:
         s1 = '0'*(num1-len(s1))+s1
    if len(s2) < num2:
         s2 = '0'*(num2-len(s2))+s2
    ms1 = s1.replace('0','.').replace('1','-')
    ms2 = s2.replace('0','.').replace('1','-')
    return ms1 + " " + ms2

def checkio(time_string):
    """ Takes a normal time string and returns Morse time string """
    time_split = time_string.split(":")
    hours   = time_split[0]
    minutes = time_split[1]
    seconds = time_split[2]
    if len(hours) < 2:
        hours = '0'*(2-len(hours)) + hours
    if len(minutes) < 2:
        minutes = '0'*(2-len(minutes)) + minutes
    if len(seconds) < 2:
        seconds = '0'(2-len(seconds)) + seconds
    return morse(hours,"hours") + " : " + morse(minutes,"minutes") + " : " + morse(seconds,"seconds")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
