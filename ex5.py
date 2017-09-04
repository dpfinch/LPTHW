my_name = 'Doug P. Finch'
my_age = 27 # In years
my_height = 196 # cm
my_weight = 87 # kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Lets talk about %s." % my_name
print "He's %d inches tall." % (my_height / 2.54)
print "He's %d kg heavy." % my_weight
print "Actually thats not that heavy."
print "He's got %s eyes and %s hair" % (my_eyes,my_hair)
print "His teeth are usually %s depending on coffee" % my_teeth

# Tricky line
print "If I add %d, %d and %d I'd get %d" % (
    my_age, my_height,my_weight,my_age+my_height+my_weight)
