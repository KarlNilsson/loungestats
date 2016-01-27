import json_handler, match_handler, stat_analysis, sys


if(__name__ == "__main__"):

	data = json_handler.get_matches()
	stats = json_handler.get_matches_data()
	data, stats = match_handler.filter_common_matches(data, stats)
	matches = match_handler.init_all_matches(data, stats)

	profile = stat_analysis.Stat_analysis()
	profile.init_wallet(1000)
	profile.print_wallet()
	profile.provide_matches(matches)

	balance_stats = []

	
	for j in range(0, 100):
		profile.init_wallet(1000)
		for i in range(0, len(matches)):
			profile.check_balance()
			profile.bet(i, 10, j/100.0)
		balance_stats.append((round(j/100.0, 2), round(profile.get_balance()), profile.get_matches_bet()))

	fo = open("data3.csv", "w")
	fo.write("Upper limit, final value, no bets\n")
	for item in balance_stats:
		fo.write("%0.2f" %item[0] + "," + str(item[1]) + "," + str(item[2]) + "\n")
	

	"""
	for i in range(0, len(matches)):
		profile.check_balance()
		profile.bet(i, 10, 0)
	profile.print_wallet()
	"""


	#profile.print_wallet()
	#profile.print_top_balance()
	#profile.print_bottom_balance()

sys.exit()