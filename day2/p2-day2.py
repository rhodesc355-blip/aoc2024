# day2 - part2

# Functions

# Return True if safe, else false
# Not safe if diff between elements is 1 <= diff <= 3
# Only safe if all elements are always increasing or decreasing. Not both
def checkSafe(arr):
    safe = True
    asc = False
    desc = False

    for j in range(0,len(arr)-1):
        x = int(arr[j])
        y = int(arr[j+1])
        
        if (x < y):
            asc = True
        elif (x > y):
            desc = True

        z = x-y
        
        if (abs(z) > 3) or (abs(z) == 0):
            safe = False
            break
        if not (asc^desc): # XOR
            safe = False
            break
    return safe

def dampener(arr):
    safe = False
    for i, _ in enumerate(arr):
        tmpArr = arr[:i] + arr[i+1:]
        safe = checkSafe(tmpArr)
        if safe:
            break
    return safe

# Main Code
# ---------------------------------------------
with open('input.txt', 'r') as file:
    nums = [line.split() for line in file]

ans = []

for line in nums:
    safe = checkSafe(line)
    if not safe:
        safe = dampener(line)
    ans.append(safe)

print("Sum of safe: " + str(sum(ans)))
    
