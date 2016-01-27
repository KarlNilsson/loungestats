class Match:

	def __init__(self, team_a, team_b, match_id, value_a=0, value_b=0, winner="N/A"):
		self.team_a 	= team_a
		self.team_a 	= team_b
		self.match_id 	= match_id
		self.value_a 	= value_a
		self.value_b 	= value_b
		self.winner		= winner

		if winner != "N/A":
			if winner == team_a:
				self.value_winner = self.value_a
			elif winner == team_b:
				self.value_winner = self.value_b
			else:
				value_winner = -1

	def get_teams():
		return (self.team_a, self.team_b)

	def get_values():
		return (self.value_a, self.value_b)

	def get_winner():
		return self.winner

	def get_winner_value():
		return self.value_winner

	def get_match_id():
		return self.match_id

	def bet(amount, team):
		if team == self.winner:
			return amount * self.value_winner
		elif winner == "N/A":
			return amount
		else:
			return -1*amount