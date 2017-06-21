from sys import argv
script, filename = argv

print "We're going to erase %r !" % filename
print "Hit ENTER if you agree."
print "Hit CTRL+C if you don't agree."

raw_input("?")

print "Opening the file"
target = open(filename,'w')

print "Truncating the file. Goodbye"
target.truncate()

print "Now i'm going to ask you for 3 lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Im going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
target.close()
