import os, sys
import Image
import ImageFilter

class Degrader:
	"""A class for degrading images visually"""

	image = None

	def degrade(self):

		image = image.filter(ImageFilter.BLUR)

		image.save(outresult.img, "JPEG")

		return

	def loadImage(self, path):

		try:
			image = Image.open(path)
		except IOError:
			print "could not load file"

		return


