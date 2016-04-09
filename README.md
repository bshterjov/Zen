INTRODUCTION
    This program schedules meetings in 2 meeting rooms consequentially and provides listing by room and ordered by time.
    Meetings that cannot be fit into the schedule are listed also.
	
USAGE
    The script can be run from an IDE editor or command line, given the meeting requests as a list of stings, such as:
        Scheduler.my_scheduler(inp=['This is the first meeting 25min', 'The second meeting 75min', '75th meeting 115min'])
		
    Or for testing purposes, it can be called with empty argument:
        Scheduler.my_scheduler([])
		   
    Have to bare in mind that the duration of the meetings should always be given in the same format at the end.
	
FURTHER DEVELOPMENT
    The script can be improved by adding functionality to schedule meetings at a given time (provided the time slot is not taken),
    to add more rooms, to handle exceptions and finally to pass successfully employment tests.
		
KNOWN BUGS
    None.
