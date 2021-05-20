import random

a = list(range(100))
#list comprenhesion
b = [i for i in a if a[i]%2 == 0]

ids = [1,2,3,4,5]
people = ["pepe","pepa","popo"]

c = zip(ids,people)

dict ={id:student for id, student in zip(ids,people)}

print(dict)

# set comprenhension remueve tdos los repetidos
repeat = []
for i in range(10):
    a = random.randint(1,4)
    repeat.append(a)
print(repeat)

nonrepeat = {i for i in repeat}

print(nonrepeat)


def binary_search(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1




if __name__ == '__main__':

    data = [random.randint(0, 100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input('What number would you like to find?'))
    found = binary_search(data, target, 0, len(data)-1)
    if found == True:
        print('The number: {} is in the list'. format(target))
    else:
        print('The number: {} is not in the list'.format(target))
