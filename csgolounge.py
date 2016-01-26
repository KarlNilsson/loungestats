import json_handler, match_handler, sys


if(__name__ == "__main__"):

	data = json_handler.get_matches()
	stats = json_handler.get_matches_data()
	prompt = '> '
	
	"""
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
	"""
	
	data, stats = match_handler.filter_common_matches(data, stats, False)

	match_handler.print_winner(data[len(data)-12], stats[len(data)-12])


	print data[len(data)-12]
	print stats[len(data)-11]


sys.exit()