import match_handler

class Stat_analysis:

	def __init__(self):
		self.balance = 0
		self.winrate = 0.0
		self.matches_bet = 0
		self.matches = []

	def count_games(self):
		return len(self.matches)

	def init_wallet(self, amount):
		self.balance = amount

	def provide_matches(self, matches):
		self.matches = matches

	def print_wallet(self):
		print 'Current balance: $' + str(self.balance)

	def print_winrate(self):
		print 'hej'

	def print_outoffunds(self, amount):
		print 'Unable to bet $' + str(amont) + '.'
		print_wallet()

	def bet(self, match, amount, strategy = 1):
		if amount > self.balance:
			print_outoffunds(amount)
			return

		pick = ''
		profit = 0
		if strategy == 1:
			if match.get_value()[0] > match.get_value()[1]:
				pick = match.get_teams()[0]
			else:
				pick = match.get_teams()[1]

		if match.get_winner() == pick:
			profit = amount * match.get_winner_value()
		elif winner != "N/A":
			profit = amount * -1

		self.balance += profit