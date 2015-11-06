ten_things = "Apples Orange Crows Telephone Light Sugar"

print "What there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Firsbee","Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:#当stuff中的元素不等于10执行
    next_one = more_stuff.pop()
    print "Adding:",next_one
    stuff.append(next_one)
    print "There are %d items now."% len(stuff)

print "There we go:", stuff

print "Let's do somethings with stuff."

print stuff[1]
print stuff[-1]# whoa! fancy
print stuff.pop()
print ''.join(stuff)# what? cool!
print '#'.join(stuff[3:5])# super stellar!
