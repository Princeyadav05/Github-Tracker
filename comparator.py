import csv
name1 = raw_input("Enter name of older file(compare from) > ")
name2 = raw_input("Enter name of newer file(compare to) >  ")

with open(name1 + '.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
print data
z = len(data)

with open(name2 + '.csv', 'rb') as f:
    read = csv.reader(f)
    data1 = list(read)
print data1
x = len(data1)


def compare():
    for j in range(0, x):
        for i in range(0, x):
            if data1[j][0] == data[i][0] and data1[j][1] == data[i][1] and data1[j][2] == data[i][2]:
                print "For " + data1[i][0] + " and repo : " + data1[i][1] + " with " + data[i][2] + " changes are > "
                compare_commits = int(data1[j][4]) - int(data[i][4])
                print "Commit(s) updated = " + str(compare_commits)
                compare_lines_added = int(data1[j][5]) - int(data[i][5])
                print "Update on line(s) addition = " + str(compare_lines_added)
                compare_lines_deleted = int(data[j][6]) - int(data[i][6])
                print "Update on line(s) deletion = " + str(compare_lines_deleted)
            else:
                print "Nothing to compare for " + data1[i][0] + " with repo : " + data1[i][1] + " in new file !"

compare()
