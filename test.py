import image

d = image.Degrader()
d.loadImage("images/test.png")
print d.degrade()
print "done"

