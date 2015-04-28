import csv

def attendees_for_var(csv_file, txt_file):
    with open(csv_file, 'r') as csv_file:
        csv_lines = csv_file.read().split('\n')
        first_name = []
        last_name = []
        company_name = []
        new_first_name = []
        new_last_name = []
        new_company_name = []
        for index, line in enumerate(csv_lines):
            csv_lines[index] = line.split(",")
        for line in csv_lines:
            if line[0] != "":
                first_name.append(line[0])
                last_name.append(line[1])
                company_name.append(line[2])
        for first, last, company in zip(first_name, last_name, company_name):
            first = first.replace('"', '').replace("'", "").strip()
            last = last.replace('"', '').replace("'", "").strip()
            company = company.replace('"', '').replace("'", "").strip()
            new_first_name.append(first)
            new_last_name.append(last)
            new_company_name.append(company)
        with open(txt_file, "w") as write_file:
            for first, last, company in zip(new_first_name, new_last_name, company_name):
                write_file.write("{0} {1}, {2}\n".format(first, last, company))
                
answer = raw_input("Is first name in the first column, last name in the second column and company in the third column? Type Y for Yes and N for No >>>")
if answer == "Y" or answer == "y":
    csv_file1 = raw_input("What is your csv file name? >>>")
    csv_file1 = csv_file1.strip()
    txt_file1 = raw_input("What do you want the name of your text file to be? >>>")
    txt_file1 = txt_file1.strip()
    attendees_for_var(csv_file1, txt_file1)
elif answer == "N" or answer == "n":
    print "Please put list of first names in the first column and list of last names in the second column. When you are finished, run the program again."
else:
    print "I'm not sure what you mean. Please re-start the program and try again."
