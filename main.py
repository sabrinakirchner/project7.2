# Use the file name mbox-short.txt as the file name

fname = input("Enter File Name: ")
fh = open("mail.txt", "r")
num = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        f = line.rstrip()
        start = f.rfind("0")
        total = float(f[start:])
        num += total
        count += 1
        p = num/count
        print (p)
print("done")








