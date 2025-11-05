# day3 - part2

# Imports
import re

# Main Code
# ---------------------------------------------
nums = []
ans = 0

with open('input.txt', 'r') as file:
    nums += [line.split() for line in file]

# Regex for 'mul(###,###)' or 'do()' or 'don't()'
mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))', str(nums))

do = True
for i in mults:
    if (i[2]=="do()"):
        do = True
        continue
    if (i[3]=="don't()"):
        do = False
        continue
    if (do):
        ans += int(i[0])*int(i[1])

print(ans)
