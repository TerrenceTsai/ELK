def add(numbers, callback):
    results = []
    for i in numbers:
        results.append(callback(i))
    return results

def add2(number):
    return number + 2

def mul2(number):
    return number * 2

print add([1,2,3,4], add2) #=> [3, 4, 5, 6]
print add([1,2,3,4], mul2) #=> [2, 4, 6, 8]