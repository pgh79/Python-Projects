from itertools import product
import sys, cmd, string, pprint, threading, time, datetime, os

class Car():
	cars = []
	def __init__(self, nplate, floor, coord, time, tent, fee, index):
		self.nplate = nplate
		self.floor = floor
		self.coord = coord
		self.time = time
		self.tent = tent
		self.fee = fee
		self.index = index
		
class CarHistory():
	def __init__(self, nplate, tentd, tleft, fee, index):
		self.nplate = nplate
		self.tentd = tentd
		self.tleft = tleft
		self.fee = fee
		self.index = index
		
class CarPayment():
	def __init__(self, nplate, type, number, expiry, csc, index):
		self.nplate = nplate
		self.type = type
		self.number = number
		self.expiry = expiry
		self.csc = csc
		self.index = index
		
class CarPark():
	parked = []
	historylist = []
	payment = []
	def __init__(self):
		groundcoords = list(product(xrange(7), xrange(7)))
		self.ground = [["OO","R","OO","NN","OO","R","OO"],
					["OO","R","OO","NN","OO","R","OO"],
					["OO","R","OO","OO","OO","R","OO"],
					["DL","R","R","R","R","R","DR"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","Ra","OO","R","OO"]]
		self.middle = [["OO","R","OO","Ra","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["R","R","R","R","R","R","R"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","Ra","OO","R","OO"]]
		self.top = [["OO","R","OO","Ra","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["R","R","R","R","R","R","R"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"],
					["OO","R","OO","R","OO","R","OO"]]
		self.currentindex = 0
	
	def spotsFree(self):
		i=0
		for rownum, row in enumerate(self.ground):
			for colnum, value in enumerate(row):
				if value == "OO":
					i+=1
		for rownum, row in enumerate(self.middle):
			for colnum, value in enumerate(row):
				if value == "OO":
					i+=1
		for rownum, row in enumerate(self.top):
			for colnum, value in enumerate(row):
				if value == "OO":
					i+=1
		return i
	
	def printgrid(self):
		print "\n Ground Floor:\n"
		for i in self.ground:
			x = '|'.join(map(str, i))
			print x.replace("DL", "<<").replace("DR",">>").replace("Ra", "^^").replace("R", chr(254) + chr(254))
		print "\nFirst Floor:\n"
		for i in self.middle:
			x = '|'.join(map(str, i))
			print x.replace("DL", "<<").replace("DR",">>").replace("Ra", "^^").replace("R", chr(254) + chr(254))
		print "\nRoof:\n"
		for i in self.top:
			x = '|'.join(map(str, i))
			print x.replace("DL", "<<").replace("DR",">>").replace("Ra", "^^").replace("R", chr(254) + chr(254))
		print "\n"
		print "KEY:"
		print chr(254) + chr(254), "- Road\nOO - Empty Spot\nNumber - ID of car parked in spot\n>>/<< - Entrance/Exits\n^^ - Ramp\nNN - Invalid Slot (not accessible)\n"
	
	def createCar(self, nplate, xtime, floor, rownum, colnum, list):
		coord = (rownum, colnum)
		fee = float(xtime)*0.5
		self.currentindex += 1
		car = Car(nplate, floor, coord, xtime*60, time.time(), fee, self.currentindex)
		carh = CarHistory(nplate, time.ctime(), 0, 0, self.currentindex)
		carp = CarPayment(nplate, "", "", "", "", self.currentindex)
		self.payment += [carp]
		self.parked += [car]
		self.historylist += [carh]
		if self.currentindex < 10:
			list[rownum][colnum] = "0" + str(self.currentindex)
		else:
			list[rownum][colnum] = str(self.currentindex)
		print "Vehicle ID: " + nplate + " parked successfully.\n"
		return
	
	def park(self, nplate, xtime):
		for rownum, row in enumerate(self.ground):
			for colnum, value in enumerate(row):
				if value == "OO":
					self.createCar(nplate, xtime, "Ground ", rownum, colnum, self.ground)
					return
		for rownum, row in enumerate(self.middle):
			for colnum, value in enumerate(row):
				if value == "OO":
					self.createCar(nplate, xtime, "Level 1", rownum, colnum, self.middle)
					return
		for rownum, row in enumerate(self.top):
			for colnum, value in enumerate(row):
				if value == "OO":
					self.createCar(nplate, xtime, "Roof   ", rownum, colnum, self.top)
					return
		print "There are no further parking spots on this level.\n"
		return

			
	def search (self, id, list):
			if len(str(id)) <= 2:
				for z in [z for z,x in enumerate(list) if x.index == int(id)]:
					return list[z]
			else:
				for z in [z for z,x in enumerate(list) if x.nplate == id]:
					return list[z]

		
	def lookup(self, id):
		i = self.search(id, self.parked)
		h = self.search(id, self.historylist)
		print "\nResult Found:"
		print "\nNumber \nPlate: Time: Floor:  Coord: Fee:    Car No.:\n"
		t = time.time()
		nowtime = i.time - (t-i.tent)
		if (nowtime/60)<=0:
			f = (nowtime/60)/(-10)
			f = f*10+i.fee
			h.fee = f
		else:
			f = i.fee
		print str(i.nplate), str('%.2f'%(nowtime/60)), str(i.floor).title(), str(i.coord) + " $" + str('%.2f'%f) + "    " + str(i.index)
		print "\n"
		
	def list(self):
		print "\n"
		print "Number \nPlate: Time: Floor: Coord: Fee:    Car No.:\n"
		for i in self.parked:
			t = time.time()
			nowtime = i.time - (t-i.tent)
			if (nowtime/60)<=0:
				f = (nowtime/60)/(-10)
				f = f*10+i.fee
			else:
				f = i.fee
			print str(i.nplate), str('%.2f'%(nowtime/60)), str(i.floor).title(), str(i.coord) + " $" + str('%.2f'%f) + "    " + str(i.index)
		print "\n"
		
	def leave(self, id, type, number, expiry, csc):
		if id > 0:
			j = self.search(id, self.parked)
			h = self.search(id, self.historylist)
			p = self.search(id, self.payment)
			p.type = type
			p.number = number
			p.expiry = expiry
			p.csc = csc
			try:
				x,y = j.coord
			except AttributeError:
				print "Enter in a valid car ID/number plate!"
				return
			self.ground[x][y] = "OO"
			h.tleft = time.ctime()
			h.fee = j.fee
			self.parked.remove(j)
		else:
			print "Invalid Number Plate/Car ID entered."
	
	def history(self):
		totalpi = 0
		print "\n"
		print "Number \nPlate: Time Entered:            Time Left:               Fee Paid: Car No.:\n"
		for i in self.historylist:
			p = self.search(i.index, self.payment)
			if i.tleft == 0:
				temp = "Car has not left yet.   "
				totalpi += i.fee
				print str(i.nplate), str(i.tentd), str(temp) + " $" + str('%.2f'%i.fee) + "     " + str(i.index)
			else:
				temp = i.tleft
				print str(i.nplate), str(i.tentd), str(temp) + " $" + str('%.2f'%i.fee) + "     " + str(i.index)
				totalpi += i.fee
				if p.type == "credit":
					print "Payment\nType:  Card Number:     Expiry: CSC:"
					print str(p.type).title(), str(p.number), str(p.expiry) + "   " + str(p.csc) + "\n\n"
				else:
					print "Payment Type: " + str(p.type).title() + "\n"
		print "\nTotal Revenue: $" + str('%.2f'%totalpi) + "\n"
		
	def stats(self):
		total=73
		totalr = 0.0
		free = self.spotsFree()
		for i in self.historylist:
			if i.tleft == 0:
				None
			else:
				totalr+=i.fee
		print "Statistics:\n=======================\nTotal Cars Parked: " + str(total-free) + "\nFree Spots: " + str(free) + "\nTotal Revenue: $" + str('%.2f'%totalr) + "\n"
				
			
		
class CLI(cmd.Cmd):
	def __init__(self):
		self.c = CarPark()
		cmd.Cmd.__init__(self)
		self.prompt = "Enter a command: "
		
	def do_map(self, arg):
		self.c.printgrid()
		
	def help_map(self):
		print "\nsyntax: map"
		print "Displays a map of the complex onscreen.\n"
		
	def do_clear(self, arg):
		os.system('cls')
		
	def help_clear(self):
		print "\nsyntax: clear"
		print "Clears the screen on windows.\n"
		
	def do_quit(self, arg):
		sys.exit(1)
		
	def help_quit(self):
		print "syntax: quit"
		print "Quits the program"
		
	def do_park(self, arg):
		try:
			l = arg.split()
			self.c.park(l[0], float(l[1]))
		except IndexError:
			print "Invalid parking entry.  Syntax is: park <number plate> <time paid>"
			
	def help_park(self):
		print "\nsyntax: park <number plate> <time in minutes>"
		print "Adds a new car to the parking complex with so many minutes pre-paid.\nThe system automatically assigns the car a place and a level.\n"
	
	def do_lookup(self, arg):
		l=arg.split()
		l[0] = str(l[0]).upper()
		i = self.c.search(l[0], self.c.parked)
		if i == None:
			print "\nNo valid result found.\n"
		else:
			self.c.lookup(l[0])

	def help_lookup(self):
		print "\nsyntax: lookup <number plate/id>"
		print "Searches the vehicle database to find a certain vehicle parked in the complex.\nDisplays all relevant information on discovery.\n"
		
	def do_list(self, arg):
		self.c.list()
		
	def help_list(self):
		print "\nsyntax: list"
		print "Lists all vehicles currently in the car park and all relevant information.\n"
		
	def do_leave(self, arg):
		l=arg.split()
		self.c.list()
		type = raw_input("Payment Type: [Cash, Cheque or Credit] ")
		type = type.lower()
		if type == "credit":
			number = raw_input("Please enter the card number: ")
			expiry = raw_input("Please enter the expiry: [Format dd/mm] ")
			csc = raw_input("Please enter the security code: ")
			self.c.leave(l[0], type, number, expiry, csc)
		else:
			self.c.leave(l[0], type, "", "", "")
		
	def help_leave(self):
		print "\nsyntax: leave <number plate/id>"
		print "Removes the car from the database, and collects prepaid toll + any fines."
		
	def do_history(self, arg):
		self.c.history()
		
	def do_stats(self, arg):
		self.c.stats()

print "\nWelcome to the Manly Car Park Admin Panel!!!"
print "============================================"
print "\n"
cli = CLI()
#threadconfigure()
cli.cmdloop()
cli.cmdloop()