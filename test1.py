from string import printable

s = input("please enter input consisting of lowercase latin letters: ")
if s.islower() is False:
    print("please use only lowercase letters")
    quit()
if bool(set(s) - set(printable)) or any(map(str.isdigit, s)) or (" " in s) is True:
    print("please use only lattin letters")
    quit()
if (len(s) >= 1 and len(s) <= 1000) is False:
    print("please enter string in range: 1 to 1000 characters")
    quit()
k = input("how many different letters? ")
try:
    k = int(k)
except:
    print("please enter a number")
    quit()
if (k <= 1 or k >= 26):
    print("there are 26 letters in latin alphabet")
    quit()
if len(s) > 26 or len(s) < k:
    print("not possible")
    quit()
if k <= len(set(s)):
    print("0")
else:
    print(k - len(set(s)))
