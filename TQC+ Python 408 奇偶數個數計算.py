odd = 0
even = 0

for i in range(10):
    x = int(input())
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even numbers: {even}\nOdd numbers: {odd}")
