def make_nums(total, increment):
	numbers = []
	for i in range(0, total, increment):
		numbers.append(i)
	print numbers
	
make_nums(100,10)


"""Previously:

	i = 0
	numbers = []
	while i < total:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i+=increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num
"""