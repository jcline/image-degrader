import os, sys
import Image
import ImageFilter

class Degrader:
	"""A class for degrading images visually"""

	def __init__(self):
		self.image = None
		self.degrading = False

	def degrade(self):

		if self.degrading:
			return False
		if self.image == None:
			return False

		self.degrading = True

		self.image = self.image.filter(ImageFilter.BLUR)

		self.image.save("outresult.img", "JPEG")

		self.degrading = False
		return True

	def loadImage(self, path):

		try:
			self.image = Image.open(path)
		except IOError:
			print "could not load file"
			print IOError

