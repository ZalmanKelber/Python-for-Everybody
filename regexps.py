import re

fname = input("Enter file name: ")
handle = open(fname)

sum = 0

for line in handle:
    nums = re.findall("[0-9]+", line)
    for num in nums:
        sum += int(num)

print(sum)
