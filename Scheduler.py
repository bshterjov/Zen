def my_scheduler(inp=[]):
	"""
	This program schedules meetings in 2 meeting rooms consequentially and provides listing by room and ordered by time.
	Meetings that cannot be fit into the schedule are listed also.
	"""
	import datetime
    # Sorry I could not copy the exact example from HackerRank
	str = ['This is the first meeting 25min',
		   'The second meeting 75min',
		   '75th meeting 115min',
		   'Last of the meetings 50min',
		   '2This is the first meeting 25min',
		   '2The second meeting 75min',
		   '275th meeting 115min',
		   '2Last of the meetings 50min',
		   '3This is the first meeting 25min',
		   '3The second meeting 75min',
		   '375th meeting 115min','375th meeting 115min','Another 375th meeting 115min'
		   ]

    # This is to show that it works when there is no input given, i.e. replaces empty input with above list
	# print(inp)
	if not inp:
		inp=str
	print(inp)
	
	# Break the input to Title (s2) and Duration in minutes (s1)
	combs = []
	for s in inp:
		words = s.split(' ')
		s1 = words[-1]
		s1 = int(s1[:-3])
		s2 = ''
		for s12 in words[:-1]:
			s2 = s2 + s12 + ' '
		mt = (s1,s2)
		combs.append(mt)
	# print(combs)

    # Set the time limits
	t11 = datetime.time(9,0)
	t12 = datetime.time(12,0)
	t13 = datetime.time(13,0)
	t14 = datetime.time(17,0)
	t21 = datetime.time(9,0)
	t22 = datetime.time(12,0)
	t23 = datetime.time(13,0)
	t24 = datetime.time(17,0)

    # Function for adding minutes to a time
	def addm(t,m=0):
		minutes = m + int(datetime.time.strftime(t,'%M'))
		hours = int(datetime.time.strftime(t,'%H'))
		minh = minutes//60 + hours
		minm = minutes%60
		t1 = t.replace(hour=minh, minute= minm)
		return t1

    # Filling meetings in meeting rooms
	meetingRoom1 = []
	meetingRoom2 = []
	for x in combs:
		if addm(t11,x[0]) < t12:
			mr11 = (t11, x[1], x[0])
			t11 = addm(t11,x[0])
			meetingRoom1.append(mr11)
		elif addm(t21,x[0]) < t22:
			mr11 = (t21, x[1], x[0])
			t21 = addm(t21, x[0])
			meetingRoom2.append(mr11)
		elif addm(t13, x[0]) < t14:
			mr11 = (t13, x[1], x[0])
			t13 = addm(t13, x[0])
			meetingRoom1.append(mr11)
		elif addm(t23,x[0]) < t24:
			mr11 = (t23, x[1], x[0])
			t23 = addm(t23, x[0])
			meetingRoom2.append(mr11)
		else:
            # The meetings that would not fit in the schedule for the day will be listed as
			print('There is no available meeting room today for meeting "',x[1],'"')

    # Printing out the output
	print(' ')
	print('Schedule for Meeting Room 1')
	print('Time       Title                          Duration(min)')
	for mr in meetingRoom1:
		print(datetime.time.strftime(mr[0],'%H:%M').ljust(10), mr[1].ljust(30), mr[2])

	print(' ')
	print('Schedule for Meeting Room 2')
	print('Time       Title                          Duration(min)')
	for mr in meetingRoom2:
		print(datetime.time.strftime(mr[0],'%H:%M').ljust(10), mr[1].ljust(30), mr[2])