# Dictionaries

band = {"vocals": "Plants", "guitar": "Page"}

band2 = dict(vocals="Plants", guitar="Page")
print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key / value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("drums" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem())  # tuple
print(band)

# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# Copy dictonaries
# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Susweta"
# print(band)

band2 = band.copy()
band2["drums"] = "Susweta"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries

member1 = {"name": "Plants",
           "instrument": "vocals"}

member2 = {"name": "Page",
           "instrument": "guitar"}

band = {"member1": member1,
        "member2": member2}
print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed(the duplicate one will be shown only once)
nums = {1, 2, 3, 2}
print(nums)

# True is a dupe for 1 while false is a dupe for 0
nums = {1, 2, True, 0, 3, False}
print(nums)
# if you use 0 and false both the one which is written first will be considered the second omitted

# Check if a value is in a set
print(2 in nums)
# but you cannot refer to an element in the set with an index position or a key

# Add a new element to set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 9}
nums.update(morenums)
print(nums)

# you can use update with lists,tuples and dictionaries too

# Merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}
mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 6}
one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 6}
one.symmetric_difference_update(two)
print(one)

