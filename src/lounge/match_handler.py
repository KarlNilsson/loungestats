import match

def get_value(stats_member):
	a = (float)(stats_member['a'])
	b = (float)(stats_member['b'])

	a_percentage = a/(a+b)
	b_percentage = b/(a+b)
	a_value = round((1.0/a_percentage)-1, 2)
	b_value = round((1.0/b_percentage)-1, 2)

	return (a_value, b_value)

def get_match_info(data_member):
	team_a 			= data_member['a']
	team_b 			= data_member['b']
	match_id 		= data_member['match']
	winning_team 	= data_member['winner']
	if winning_team in ['a', 'b']:
		winner = data_member[winning_team]
	else:
		winner = "N/A"

	return (team_a, team_b, winner, match_id)

def print_winner(data_member, stats_member):
	a_value, b_value = get_value(stats_member)
	team_a, team_b, winning_team, match_id = get_match_info(data_member)
	print (team_a + ": " + (str)(a_value) + " for 1\n")
	print (team_b + ": " + (str)(b_value) + " for 1\n")
	print ('\n\nWINNER:\t'),
	print winning_team
	print '\n\n'

def remove_closed_games(data, stats):
	i = 0
	while (i < len(data)):
		member = data[i]
		if (member['winner'] not in (['a', 'b'])) or ((int)(member['closed']) == 0):
			data.pop(i)
			i-=1
		i += 1

def get_common_matches(data, stats):
	data_matches = []
	stats_matches = []
	for member in data:
		data_matches.append(member['match'])
	for member in stats:
		stats_matches.append(member['match'])

	common_matches = (set(data_matches) & set(stats_matches))
	common_matches = sorted(common_matches, key=lambda x: (int)(x))
	return common_matches

def filter_common_matches(data, stats, remove_closed=True):
	if remove_closed:
		remove_closed_games(data, stats)

	common_matches = get_common_matches(data, stats)
	data_copy = list(data)
	stats_copy = list(stats)
	new_data = []
	new_stats = []

	for i in range(len(common_matches)):
		found = False
		while len(data_copy) > 0:
			member = data_copy[0]
			if member['match'] == common_matches[i]:
				new_data.append(member)
				found = True
			data_copy.pop(0)
			if found:
				break

		found = False
		while len(stats_copy) > 0:
			member = stats_copy[0]
			if member['match'] == common_matches[i]:
				new_stats.append(member)
				found = True
			stats_copy.pop(0)
			if found:
				break

	return new_data, new_stats

def init_all_matches(data, stats):
	matches = []
	for i in range (len(data)):

		match_info = get_match_info(data[i])
		values = get_value(stats[i])

		game = match.Match(match_info[0], match_info[1], match_info[3], values[0], values[1], match_info[2])
		matches.append(game)

	return matches