import match_handler

class Stat_analysis:

	def __init__(self):
		self.balance = 0.0
		self.winrate = 0.0
		self.matches_bet = 0
		self.matches = []
		self.top_balance = 0.0
		self.bottom_balance = 0.0

	def count_games(self):
		return len(self.matches)

	def init_wallet(self, amount):
		self.balance = amount
		self.top_balance = amount
		self.bottom_balance = amount
		self.matches_bet = 0

	def check_balance(self):
		if self.balance > self.top_balance:
			self.top_balance = self.balance
		if self.balance < self.bottom_balance:
			self.bottom_balance = self.balance

	def get_balance(self):
		return self.balance

	def get_matches_bet(self):
		return self.matches_bet

	def print_top_balance(self):
		print 'Highest balance so far: $' + str(self.top_balance)

	def print_bottom_balance(self):
		print 'Lowest balance so far: $' + str(self.bottom_balance)

	def provide_matches(self, matches):
		self.matches = matches

	def print_wallet(self):
		print 'Current balance: $' + str(self.balance)

	def print_winrate(self):
		print 'hej'

	def print_outoffunds(self, amount):
		print 'Unable to bet $' + str(amount)
		self.print_wallet()

	def bet(self, match_pos, amount, minimum, strategy = 1):
		match = self.matches[match_pos]
		#if amount > self.balance:
		#	self.print_outoffunds(amount)
		#	return

		pick = ''
		profit = 0
		if strategy == 1:
			if match.get_values()[0] < match.get_values()[1]:
				pick = match.get_teams()[0]
			else:
				pick = match.get_teams()[1]

		if match.get_values()[0] < minimum:
			return
		elif match.get_values()[1] < minimum:
			return

		if match.get_winner() == pick:
			profit = amount * match.get_winner_value()
		elif match.get_winner() != "N/A":
			profit = amount * -1

		self.balance += profit
		self.matches_bet += 1