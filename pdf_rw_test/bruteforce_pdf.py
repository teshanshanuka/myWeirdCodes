# Code runcs only on python3
import string
from subprocess import check_call, DEVNULL, CalledProcessError
import sys

alph = string.ascii_lowercase
input_file = 'enc128.1.pdf'
output_file = 'dec_py.pdf'

def fn(depth, wordlist = ['']):
    newlist = []
    print('depth : '+ str(len(wordlist[0])+1))
    print('\tpermutations : ' + str(len(alph)**(len(wordlist[0])+1)))
    for word in wordlist:
        for letter in alph:
            newlist.append(word+letter)
            try:
                check_call(['pdftk', input_file,'input_pw',(word+letter),'output',output_file],stderr=DEVNULL)
                print('Password found! : '+(word+letter))
                print("Unlocked file saved as '"+output_file+"'" )
                return
            except CalledProcessError:
                pass
    if depth == 0:
        print('No luck :(')
        return
    fn(depth-1, newlist)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please specify depth for brute forcing")
    else:
        fn(int(sys.argv[1]))
