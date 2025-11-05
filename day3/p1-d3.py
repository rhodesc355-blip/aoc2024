# day3 - part1

# Import
import re

# Main Code
# ---------------------------------------------
nums = []
ans = 0

with open('input.txt', 'r') as file:
    nums += [line.split() for line in file]

# Regex for 'mul(###,###)'
mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', str(nums))

for i in mults:
    ans += int(i[0])*int(i[1])

print(ans)
