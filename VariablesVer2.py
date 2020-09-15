# This class will show using operators with variables, only the common opertors
#not all for now

person_name = 'Mike' #assignment

speed = 31.2
distance = 30

speed = distance

alive = False

is_alive = not alive # the not operator inverses the boolean value in alive

print('is_alive = ' + str(is_alive))

# adition

time = speed + distance

time = speed - distance #subtrac

time = speed * distance # multiplication

time = speed/speed # division

speed = time/distance
print(speed)

#modulus - returns remainder of a divsion (what's left)

time = 6 % 4
print(time)

# floor operator that discards the reminder after performing devision

time = 4//3
print(time)
# exponent operator

time = 2**3


time += distance # equivalent time = time + distance, also there is /= *= and -=

full_name = person_name + 'Andriod'


#condition ==   !=  <   <=   >=   >

result = full_name == person_name

print(result)

result =  time >= distance

print(result)

result = time < distance

print(result) # last note, be careful with indentation 
