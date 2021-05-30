numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for num in range(0, len(numbers) - 1):
    if numbers[num] >= numbers[num + 1]:
        continue
    result.append(numbers[num+1])
print(result)