import numpy
from csv import reader
from random2 import randint

class Day:
	def __init__(self, date, date_id, tests, positives):
		self.date = date
		self.date_id = int(date_id)
		try:
			self.tests = int(tests)
		except ValueError:
			self.tests = 0
		try:
			self.positives = int(positives)
		except ValueError:
			self.positives = 0
		try:
			self.ratio = self.positives/self.tests
		except ZeroDivisionError:
			self.ratio = 0.0
		self.increase = 0.0

	def __str__(self):
		return f"{self.date} ({self.date_id}):\t{self.tests:5d} Tests\t{self.positives:5d} Positives\t\tRatio: {self.ratio*100:2.2f}%\tIncrease in positives: {self.increase*100:2.2f}%"
	
	def __repr__(self):
		return f"{self.date} ({self.date_id}):\t{self.tests:5d} Tests\t{self.positives:5d} Positives\t\tRatio: {self.ratio*100:2.2f}%\tIncrease in positives: {self.increase*100:2.2f}%"
	
	@classmethod
	def load_from_csv(cls, data):
		# normalize
		data[2] = data[2].replace(".", "")
		data[3] = data[3].replace(".", "")

		if data is not None:
			return Day(date=data[0], date_id=data[1], tests=data[2], positives=data[3])
		else:
			return None

	def calcIncrease(self, yesterday):
		self.increase = self.ratio-yesterday.ratio

def get_index(self):
	return self.date_id

def main():
	with open("coviddaten_2021-03-15.csv", "r", encoding="utf-8") as file:
		data_csv = reader(file, delimiter=";")
		header = []
		days_sum = []
		days = []

		for row_cnt, row in enumerate(data_csv):

			if row_cnt == 0:
				header = row
			if row_cnt == 1:
				days_sum = row
				row[1] = "-1"
			if row_cnt != 0:
				days.append(Day.load_from_csv(row))

		days = sorted(days, key=get_index)

		for d in range(len(days)-1):
			days[d+1].calcIncrease(days[d])
		
		days = sorted(days, key=get_index, reverse=True)

		for d in days:
			print(d)

if __name__ == "__main__":
	main()