i       = 0
numbers = []

while i < 6:
    print "At the top of the I counter, I is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now:", numbers

    print "At the bottom of the I counter, I is %d" % i
    print "\n"

print "The whole array:"
for num in numbers:
    print num
