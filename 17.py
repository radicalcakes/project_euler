#count each 999
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousand = len('onethousand')

def calculate_sum(n, l):
	i = 0
	while i < n:
		yield len(l[i])
		print l[i]
		i += 1

def total_calc():
	#right off the bat, we know there are 10 'ten'
	s = 30
	s += len('hundred')*899
	print s
	s += len('and')*890
	print s
	t = sum(calculate_sum(len(tens), tens))
	o = sum(calculate_sum(len(ones), ones))
	teen = sum(calculate_sum(len(teens), teens)) * 10
	o2 = (o + t) * 99
	s += teen
	s += o * 90
	s += o2
	s += thousand
	return s


if __name__=="__main__":
	print total_calc()



