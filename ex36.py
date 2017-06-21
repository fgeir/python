ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there's not 10 things in that list, lets fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song","Perro","Gato","Orca","Arrachera","Rib-Eye","Balon"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now" % len(stuff)

print stuff
print ' '.join(stuff)
print '#'.join(stuff[3:5])
