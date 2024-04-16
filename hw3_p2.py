# Team member: Nabanita Gupta

# this programm asks user to input a tweet, and then count the number of words,
#Average number of characters,Number of upper and lower case letters;

   
#this function reverse the input string.
def reverse(x):
    return x[::-1] #slice the string start from the end of string to 0.

# this function counts alphabets, number of digits, number of special characters
def str_statis(y):
    abc= 0
    num= 0
    spe= 0
    y = y.replace(" ", "")
    for i in y:
        if i.isalpha():
            abc += 1
            continue
        elif i.isdigit():
            num += 1
            continue
        else:
            spe += 1
            continue
    return abc,num,spe

def main():
    data = input("Enter a tweet: ")
    lst  = data.split() 
    wd = len(lst)
    re = data.replace(" ", "") #remove whitespaces 
    ch = len(re)
    ave = ch/wd
    up = 0 
    lw = 0 
    for ch in re:
        if ch.isupper():
            up += 1
        elif ch.islower():
            lw += 1
    r = reverse(data)
    abc,num,spe = str_statis(re)
    print("Number of words: ", wd)
    print("Average number of characters: ", ave)
    print("Number of upper case letters: ", up )
    print("Number of lower case letters: ", lw )
    print("you tweet reversed: ", r)
    print("Number of alphabets(a to z, A to Z): ", abc)
    print("Number of digits 0 to 9: ", num)
    print("Number of special characters (such as:# @ &) ", spe)
    return
main()

