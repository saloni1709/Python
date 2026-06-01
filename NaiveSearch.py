import random
l = []
# 10 random numbers (1 to 50) list mein add karo
for i in range(10):
    l.append(random.randint(1, 50))
l.sort()      # List sort kar lo (optional, bas dekhne ke liye)
print(l)

# User se number input lo
n = int(input("Enter a number: "))

# Naive / Linear Search start
for i in range(len(l)):    # List ke har element ko check karo
    if l[i] == n:          # Agar number mil gaya
        print("Found", l[i])  # Print karo
        break              # Loop stop karo
else:
    # Agar loop poora chal gaya aur number nahi mila
    print("Not Found")