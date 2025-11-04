# day2 - part2

# Functions
# -----------------------------------------------------------------
def checkSafe(arr):
    """
    Diff = (element - element+1)
    Safe if difference always increases or descreases. Not both
    Also unsafe if 1 <= diff <= 3
    """
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
    """
    Fix an unsafe line by systematically removing 1 element and running checkSafe again
    """
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
    if not safe: # Only run the dampener if we found unsafe line
        safe = dampener(line)
    ans.append(safe)

print("Sum of safe: " + str(sum(ans)))
    
