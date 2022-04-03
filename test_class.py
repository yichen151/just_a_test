class FishModel:
	def __init__(self, num=0):
		self.num = num

	def count(self):
		print(self.num)

fish = FishModel(num=10)
fish.count()
