
fname = input("Enter File Name: ")
fh = open("mail.txt", "r")
#count all that has
count = 0
#save the sum of them all
num = 0


for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        #count how many has
        f = line.find(" ")
        #value the number
        p = float(line[f:])
        num += p
        count += 1
print(num/count)
print("done")
