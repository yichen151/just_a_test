class FishModel:
	def __init__(self, num):
		self.num = num * 5

	def count(self):
		print(self.num)

class HotFishModel(FishModel):
	def __init__(self, num):
		FishModel.__init__(self, num)
		self.hot = True

	def change_status(self):
		if self.hot is True:
			self.hot = False
		else:
			self.hot = True

	def is_hot(self):
		if self.hot is True:
			print('Yes')
		else:
			print('No')

class FreshFishModel(FishModel):
	def __init__(self, num):
		FishModel.__init__(self, num)
		self.fresh = True
		
	def change_status(self):
		if self.fresh is True:
			self.fresh = False
		else:
			self.fresh = True
			
	def is_fresh(self):
		if self.fresh is True:
			print('Yes')
		else:
			print('No')
			
if __name__ == '__main__':
	fish = FishModel(num=10)
	fish.count()

	hot_fish = HotFishModel(num=20)
	hot_fish.count()
	hot_fish.is_hot()
	hot_fish.change_status()
	hot_fish.is_hot()
