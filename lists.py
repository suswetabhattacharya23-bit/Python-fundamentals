users = ['Susweta', 'Graham', 'Mica']

data = ['Susweta', 19, True]

emptylist = []

print("Susweta" in emptylist)

print(users[0])
print(users[-1])
print(users.index('Graham'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))
users.append('Messi')
print(users)

users += ['Hannah']
print(users)

users.extend(['Ken', 'Barbie'])
print(users)
# users.extend(data)
# print(users)
users.insert(0, 'Stella')
print(users)

users[1:1] = ['William', 'Augustus']
print(users)
users[1:3] = ['Hazel', 'Gratel']
print(users)
users.remove('Gratel')
print(users)
print(users.pop())
print(users)
del users[0]
print(users)
# del data  #doesn't work cause it will be non existent so nothing to print
data.clear()
print(data)

users[1:2] = ['susweta']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [23, 5, 70, 56, 47]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# Direct printing sorted value without changing original value
print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples
mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 8, 2, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)
print(anothertuple.count(2))

 

# Daily Log: 8
