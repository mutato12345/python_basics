
string_list = ["apple", "banana", "cherry", "date", "fig"]

int_list = [5, 3, 8, 1, 9, 2]

list = string_list + int_list
print(list)

print(len(string_list[0:5]))

print(len(string_list[ :-1]))

print(len(int_list[0:4]))
          
string_list.append('grape')
print(string_list)

string_list.insert(2, 'orange')
print(string_list)

int_list.extend([10, 11, 12])
print(int_list)

string_list.remove('banana')
print(string_list)

popped = int_list.pop()
print(popped)
print(int_list)

string_list.reverse()
print(string_list)

int_list.sort()
print(int_list)

int_list.sort(reverse = True)
print(int_list)

print(min(int_list))

print(max(int_list))
print(sum(int_list))

print(string_list.index('cherry'))
print('fig' in int_list)

for item in int_list:
    print("current item:", item)
    print(item)

for index, item in enumerate(string_list):
    print(f"index {index}: {item}")


fruits = "apple -banana - cherry - date"
fruit_list = fruits.split()
print(fruit_list)

fruit_tupple = ("mango", "pineapple", "papaya", "guava")
print(fruit_tupple)

for fruit in fruit_tupple:
    print("current fruit:", fruit)
    print(fruit)

print(fruit_tupple[0:-1])

set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}
print(set_1.intersection(set_2))

print(set_1.difference(set_2))

print(set_1.union(set_2))


