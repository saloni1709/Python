Orinum = 12321
num = Orinum
rev = 0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
if Orinum == rev:
    print("Palindrome")
else:
    print("Not Palindrome")