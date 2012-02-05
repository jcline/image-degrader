import os, sys
import Image
import ImageFilter

class Degrader:
	"""A class for degrading images visually"""

	image = None
	degrading = False

	def degrade(self):

		if degrading:
			return
		if image == None:
			return

		degrading = True

		image = image.filter(ImageFilter.BLUR)

		image.save(outresult.img, "JPEG")

		degrading = False
		return

	def loadImage(self, path):

		try:
			image = Image.open(path)
		except IOError:
			print "could not load file"

		return


