prefix = "'"
suffix = "',"

with open('source.txt', 'r') as src:
	with open('dest.txt', 'w') as dest:
		for line in src:
			dest.write('%s%s%s\n' % (prefix, line.rstrip('\n'), suffix))