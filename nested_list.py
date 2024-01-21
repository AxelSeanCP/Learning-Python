"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

example:
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
the second lowest is beta and alpha
"""
test_case = [["axel", 35.67], ["meltryllis", 23.54], ["okita", 65.44], ["wakamo", 35.67], ["miyako", 23.54]]

def paling_kecil(x):
    return x[1]

def get_second_lowest():
    second_lowest = [records[0][0]]
    for i in range(1, len(records)):
        if records[i][1] == records[0][1]:
            second_lowest.append(records[i][0]) 
    
    return second_lowest

def bukan_min(x):
    if x[1] == lowest_val:
        return False
    else:
        return True

records = []
for i in range(len(test_case)):
    name = test_case[i][0]
    score = test_case[i][1]
    mylist = [name,score]
    records.append(mylist)

records.sort(key=paling_kecil)

lowest_val = records[0][1]

records = list(filter(bukan_min, records))

result = get_second_lowest()

result.sort()

for name in result:
    print(name)