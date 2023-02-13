'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

infile = open("employee_data.csv", "r")


# create an empty dictionary
a = 1
employees = {}


# use a loop to iterate through the csv file
reader = csv.reader(infile)
next(reader)

for row in reader:
    i = 0
    fname = row[1]
    lname = row[2]
    salary = row[5]
    department = row[3]
    title = row[4]

    employees["firstname"] = row[1]
    employees["lastname"] = row[2]
    employees["salary"] = row[5]

    # check if the employee fits the search criteria
    if department == "Marketing" and title == "CSR":
        print('Manager Name:', fname, lname, 'Current Salary:', salary)

        employees["firstname"] = row[1]
        employees["lastname"] = row[2]
        employees["salary"] = row[5]
        new_salary = int(salary) * 1.1


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout


employees["firstname"] = row[1]
employees["lastname"] = row[2]
employees["salary"] = new_salary

for employee in employees:

    print('Manager Name:', employees["firstname"],
          employees["lastname "], 'Current Salary:', employees["salary"])
