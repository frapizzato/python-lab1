print("Enter a string:")
s = input()
k = len(s)
if (k < 4):
    print()
else:
    print(s[0]+s[1]+s[k-2]+s[k-1])