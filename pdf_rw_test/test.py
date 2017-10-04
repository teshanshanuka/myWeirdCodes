import os
import string

alph = string.ascii_lowercase

def fn(depth, wordlist):
    newlist = []
    print('depth : '+ str(len(wordlist[0])+1))
    print('\tpermutations : ' + str(len(alph)**(len(wordlist[0])+1)))
    for word in wordlist:
        for letter in alph:
            newlist.append(word+letter)
            if word+letter == 'pp':
                print(word+letter)
                return
    if depth == 0:
        print('No luck :(')
        return
    fn(depth-1, newlist)

fn(2,[''])
