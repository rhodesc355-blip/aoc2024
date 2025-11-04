with open('input.txt', 'r') as file:
    input_lines = [line.split() for line in file]

arr1 = []
arr2 = []
ans = []

for i in input_lines:
    j, k = [int(x) for x in i]
    arr1.append(j)
    arr2.append(k)

arr1.sort()
arr2.sort()

for i in arr1:
    x = arr2.count(i)
    ans.append((i*x))

print(sum(ans))
