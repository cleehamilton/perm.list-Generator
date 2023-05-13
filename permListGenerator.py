## https://stackoverflow.com/questions/21559039/python-how-to-generate-wordlist-from-given-characters-of-specific-length
## https://docs.python.org/2/library/itertools.html#itertools.product

intro = "(c)2023 kaff1n8t3d\n\
      )  (\n\
     (   ) )\n\
      ) ( (\n\
    _______)_\n\
 .-|-(c)-----|  \n\
( C|  kaff1  |\n\
 '-|  n8t3d  |\n\
   '_________'\n\
    '-------'"

welcomeMsg = "   ______________________________\n\
 / \                             \.\n\
| O |                            |.\n\
 \_ |      Permutation List      |.\n\
    |         Generator          |.\n\
    |          Vs.2.0            |.\n\
    |                            |.\n\
    |    Create a list of all    |.\n\
    |    possible combinations   |.\n\
    |    of a given character    |.\n\
    |    set. Choose how many    |.\n\
    |    place values you want   |.\n\
    |    to have, i.e. every     |.\n\
    |    combination of 4 digits |.\n\
    |    using 0-10. Or Every    |.\n\
    |    combo of 7 to 10 length |.\n\
    |    of letters and symbols  |.\n\
    |    combination.            |.\n\
    |    Creates files in a MAX  |.\n\
    |    length of 900,000 lines.|.\n\
    |    Then Generates an       |.\n\
    |    additional file,        |.\n\
    |    continuing until all    |.\n\
    |    combinations are        |.\n\
    |    generated.              |.\n\
    |                            |.\n\
    |                            |.\n\
    |   _________________________|___\n\
    |  /                            /.\n\
    \_/____________________________/.\n"




import itertools
import os
FilePath = __file__
fPath = FilePath.rstrip(os.path.basename(__file__))
##Default Settings
Defaultchrs = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
#Defaultchrs = "0123456789"#Testing set
fileSize = 900000
min_length, max_length = 6, 6
  
def getOptions():
    chrs = Defaultchrs
    ##Check Settings
    print(f"The Character Set is: {chrs}")
    chrsUpdate = "Y"
    while(chrsUpdate == "Y" or chrsUpdate == "y" or chrsUpdate == "Yes" or chrsUpdate == "YES"): #update Charcterset?
        chrsUpdate = input('\nDo you want to update the Character Set? (Y/N)\n')
        #print(chrsUpdate)
        if chrsUpdate == "N" or chrsUpdate == "n" or chrsUpdate == "No" or chrsUpdate == "NO":
            break
        elif chrsUpdate == "Y" or chrsUpdate == "y" or chrsUpdate == "Yes" or chrsUpdate == "YES" or chrsUpdate == "yes":
            chrs = input('Please enter all the characters you want to iterate through. or (C) to cancel and use the default Characters. \n')
            if chrs == "C":
                print('----Cancelled; Characters set to default.-----\n')
                chrs = Defaultchrs
            break
        else:
            print('Please enter either a capital Y or N. \n')
            chrsUpdate = "Y"

    min_length = int(input('What is the Minimum place values to start with?\n'))
    max_length = int(input('What is the Maximum place values to end with?\n'))
    return min_length, max_length, chrs

def perm(min_length, max_length,fileSize,chrs):
    for n in range(min_length, max_length+1):
        i = 1
        ifile = 1
        for xs in itertools.product(chrs, repeat=n):
            if i > fileSize:
                i = 1
                file1.close()
                ifile += 1
            if i <= fileSize:
                file1 = open(f"{fPath}Perm.list_{str(min_length)}-{str(max_length)}_{str(ifile)}.txt", "a") 
            file1.write(''.join(xs))
            file1.write("\n")
            print(''.join(xs))
            i += 1
    file1.close()
    

if __name__ == "__main__":
    print(intro)
    print(welcomeMsg)
    #::: Do the thing :::
    #Get Options from user
    options = getOptions()
    #run the standard permatation
    perm(options[0],options[1],fileSize,options[2])
    input(f"your file(s) can be found here: {fPath}\n Press any key to exit.")