import csv

def attendees_for_var(filename):
    #opens the file 
    with open(filename, 'r') as csv_file:
        #splits each line in to a string 
        csv_lines = csv_file.read().split('\n')
        #creates a list to store the first name (content in column A) and a list to store the last name (content in column B)
        first_name = []
        last_name = []
        #creates lists to put the cleaned up versions of the first and last name
        new_first_name = []
        new_last_name = []
        #splits each string into lists, so it becomes a list consisting of 2 strings, first and last name
        for index, line in enumerate(csv_lines):
            csv_lines[index] = line.split(",")
        #check and see if the line is blank (out of range error if there are blank lines)
        for line in csv_lines:
            if line[0] != "":
                #appends the first and last name to their respective list
                first_name.append(line[0])
                last_name.append(line[1])
        #cleans up the names (removes beginning and end whitespace --need white space if middle name-- and removes any unnecessary quotation marks)
        #appends cleaned up names to new list
        for first, last in zip(first_name, last_name):
            first = first.replace('"', '').replace("'", "").strip()
            last = last.replace('"', '').replace("'", "").strip()
            new_first_name.append(first)
            new_last_name.append(last)
        #writes the first and last name on each line in to a new text file 
        with open("new.txt", "w") as write_file:
            for first, last in zip(new_first_name, new_last_name):
                write_file.write("{0} {1}\n".format(first, last))
#asks user to input the existing csv file namd and what they'd like the new text file to be name. Puts the inputs into the function
csv_file1 = raw_input("What is your csv file name?")
txt_file1 = raw_input("What do you want the name of your text file to be?")
attendees_for_var(csv_file1, txt_file1)
