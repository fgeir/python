the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list.
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "This is a type of fruit: %s" % fruit

#also we can go through mixed lists Too
#notice we have to use %r since we don't know what's in it.
for i in change:
    print "I got: %r" % i

#we can also build lists
elements = []

#then use the range function
for i in range(0, 6):
    print "Adding %d to the list" % i
    #appends is a function that lists understand
    elements.append(i)

#now we can print them out Too
for element in elements:
    print "Now I have this element in my list: %d" % element
