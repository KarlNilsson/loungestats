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

	for i in range(0, len(matches)):
		profile.check_balance()
		profile.bet(i, 10)

	profile.print_wallet()
	profile.print_top_balance()
	profile.print_bottom_balance()



	
	"""
	prompt = '> '

	while(True):
		print "Enter the match you would like to watch"
		try:
			match_id = (int)(raw_input(prompt))
		except ValueError:
			sys.exit()
		if (match_id < len(data_stats)):
			data_member = data[match_id]
			stats_member = stats[match_id]
			get_value(data_member, stats_member)
		else:
			print "Non-existing match id, try again\n"
	
	

	print
	match_handler.print_winner(data[len(data)-14], stats[len(data)-14])


	print data[len(data)-14]
	print stats[len(data)-14]
	print 'Data length: ' + str(stat_analysis.count_games(data))
	"""


sys.exit()