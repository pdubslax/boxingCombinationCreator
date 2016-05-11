import random
punches = ["straight","hook","uppercut"]

def  generateComboOfLength(length):
	currentPunches = 0
	while currentPunches<length:
		punch = random.choice(punches)
		if (random.random()<=.6):
			# two of the same punch 

			if (bool(random.getrandbits(1))):
				#right hand first
				if punch == "straight":
					print "right cross"
					print "left jab"
				else:
					print "right " + punch
					print "left " + punch
			else:
				#left hand first
				if punch == "straight":
					print "left jab"
					print "right cross"
				else:
					print "left " + punch
					print "right " + punch
			currentPunches += 2
		else:
			if (bool(random.getrandbits(1))):
				# right hand
				if punch == "straight":
					print "right cross"
				else:
					print "right " + punch
			else:
				#left hand
				if punch == "straight":
					print "left jab"
				else:
					print "left " + punch
			currentPunches += 1



def main():
	condition = True
	

	while (condition):
		print 
		print "--------------------------"
		generateComboOfLength(random.randrange(4, 9))
		print
		# print random.randrange(4, 7)
		q = raw_input("Press Enter to generate another round... or q to quit...")
		if str(q)=="q":
			break

    # my code here

if __name__ == "__main__":
	main()