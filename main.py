def north():
	print "You went north!  That's probably fine."
	print "You see an A and a B, and also a button."
	button = False

	while True:
		choice = raw_input("> ")
		if choice == "A" and not button:
			print "consider all of your options my friend."
			print "but not today, for today you die."
			lose()
		elif choice == "B" and not button:
			print "think again you butt"
			lose()
		elif "button" in choice:
			print "climb, every, mountain, push, every, buttoooon"
			button = True
		elif choice == "A" and button:
			win()
		elif choice == "B" and button:
			print "EEEEHHNG!!  WRONG"
			lose()
		else:
			print "yeah, you only have so many options, here."
			print "nice that you think I'm smart enough to come"
			print "up with more stuff, but I haven't."

def south():
	print "again, I question your motives, here."
	print "are you seriously, completely sure right now?"  
	print "I'll even let you back out if you want to.  this room sucks."
	print "you should go north instead."
	choice = raw_input("> ")
	if choice == "north":
		print "oh thank god"
		north()
	else:
		win()

def win():
	print "congratulations butthead!"
	print "you won.  go tell your mother."
	exit(0)

def lose():
	print "you lose.  you see a howling hag:"
	print "SHE'S A WIIIIIITCH"
	print "BOOOOO.  BOOOOOOOO!!"
	exit(0)

def main():
	print "WELCOME TO THE DUNDJEL"
	print "you can go north and south.  maybe other directions?"
	choice = raw_input("> ")
	if choice == "north":
		print "You carry on your dumb way north, dummy"
		north()
	if choice == "south":
		print "god why would you ever go south.  Fine, you go south."
		south()

main()
