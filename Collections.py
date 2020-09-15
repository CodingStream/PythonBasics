# dictionaries, arrays/list (both are same), Tuples

pos = (20, 20, 30) #Tuple, can't add or remove elements

print(pos[0])
print(pos[2])
print(pos)

# you need to have a comma after your last element you are adding to the new tuple
new_pos = pos + (40,) 

print(new_pos)

len(pos)
max(pos)
min(pos)
result = new_pos[0] in pos

print(result)

del new_pos #deletes/removes var from memory


movements = [10, -1, -9, 3, 5]

old_movement = movements[0]

movements[0] = 2


movements.append(3) #adds elements to end of array
movements.remove(3) #removes first occurance of the number 3 from array

print(movements)


#dictionaries


starting_pos = {'p1': 50, 'p2': 20, 'p3':40}

starting_pos['p1']

starting_pos['p4']= 50

print(starting_pos.keys())
print(starting_pos.values())

