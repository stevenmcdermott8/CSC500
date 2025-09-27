'''
Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
 Write a Python program to solve the general version of the above problem. Ask the user 
 for the time now (in hours) and then ask for the number of hours to wait for the alarm. 
 Your program should output what the time will be on a 24-hour clock when the 
 alarm goes off.
 '''

 # define function to gather current hour and handle errors
def get_current_hour():
    ''' surround with try/except to catch invalid input and prevent application
    from crashing, put inside a loop to allow running function until valid input is given'''
    while True:
        ## begin try block to handle potential exception
        try:
            ## set current hour to calculate from
            current_hour = int(input('Enter current hour (0-23) for 24 hour clock, eg 13 = 1pm: '))
            ## validate that the hour entered is a valid hour
            if 0 <= current_hour <= 23:
                ## if valid, return the value the user entered, cast as an integer
                return current_hour
            else:
                ## inform user if we need value between 0 and 23 only
                print("Hour must be between 0 and 23.")
        except ValueError:
            ## inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter a valid integer.")
    
 # define function to gather hours to wait and handle errors
def get_hours_to_wait():
    ''' surround with try/except to catch invalid input and prevent application
    from crashing, put inside a loop to allow running function until valid input is given'''
   
    while True:
        ## begin try block to handle potential exception
        try:
            ## set current hour to calculate from
            hours_to_wait = int(input('Enter total hours to wait: '))
            if hours_to_wait > 0:
                ## if valid, return the value the user entered, cast as an integer
                return hours_to_wait
            else:
                ## inform user if we need value between 0 and 23 only
                print("Hour must be greater than 0")
        except ValueError:
            ## inform user if we specifically get invalid input for the expected input type
            print("Invalid input. Please enter valid integers only.")

def main():
    # get the current hour from the user
    current_hour = get_current_hour()

    # get the time to wait from the user
    hours_to_wait = get_hours_to_wait()
    
    ## calculate the total hours by adding current hour to hours to wait
    total_hours = current_hour + hours_to_wait
    
    ## get the total days to wait if number is over 24
    ## set defaul value of 0 to avoid errors later
    alarm_days = 0
    if (total_hours >= 24):
        ## get total days, rounded down to whole days using //
        ## the remainder is gathered later
        alarm_days = total_hours // 24

    ## get the total hours to add to the alarm
    next_alarm_hour = total_hours % 24

    ## extra credit, get the 12 hour clock time.
    next_12_hour_clock_time = next_alarm_hour
    if (next_alarm_hour > 12):
        ## subtract 12 if number is greated than 12
        next_12_hour_clock_time = next_12_hour_clock_time - 12
    
    ## based on the alarm hour, determine if this is an am or pm hour
    am_or_pm = 'pm' if next_alarm_hour >= 12 else 'am'

    ## print the time in 24 and 12 hour clock formats
    print('\n24 hour clock time {}:00'.format(next_alarm_hour))
    print('12 hour clock time {}:00 {}'.format(next_12_hour_clock_time, am_or_pm))

    ## print the days to wait plus the hour the alarm will go off
    print('\nOn a 24 hour clock, the alarm will go off in {} day(s) at {}'.format(alarm_days, next_alarm_hour))
    print('On a 12 hour clock, The alarm will go off in {} days(s) as {} {}'.format(alarm_days, next_12_hour_clock_time, am_or_pm))

## main function to run program
if __name__ == "__main__":
    main()