log_file = open("um-server-01.txt")  # this line opens files and puts it in variable


def sales_reports(log_file):   # defining a function by naming it and telling us the input required
    '''
    reads files and prints sales from Monday only.
    '''


    for line in log_file:   # for loop, looks at each line in the file
        line = line.rstrip() # apply rstrip method, which gets rid of spaces at the end of a line
        day = line[0:3]  # putting the first three characters of a line in a variable -= assigning
        if day == "Mon":  # if the day variable is monday do something
            print(line)   #the something is print the log line :)


sales_reports(log_file) # run the function that I just defined thaaanks
