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
    for i in range(0, x):
        flag = 0
        flag1 = 0
        for j in range(0, z):
            if data1[i][0] == data[j][0] and data1[i][1] == data[j][1]:
                global flag
                flag = 1
                if data1[i][2] == data[j][2]:
                    global flag1
                    flag1 = 1
                    print "For " + data1[i][0] + " and repo : " + data1[i][1] + " with " + data1[i][2] + " changes" \
                                                                                                         " are > "
                    compare_commits = int(data1[i][4]) - int(data[j][4])
                    print "Commit(s) updated = " + str(compare_commits)
                    compare_lines_added = int(data1[i][5]) - int(data[j][5])
                    print "Update on line(s) addition = " + str(compare_lines_added)
                    compare_lines_deleted = int(data1[i][6]) - int(data[j][6])
                    print "Update on line(s) deletion = " + str(compare_lines_deleted)
                    flag = 1
                    break
        if flag == 1 and flag1 == 0:
            print "New Contributor"
            print "For " + data1[i][0] + " and repo : " + data1[i][1] + " with " + data1[i][2] + " changes are > "
            compare_commits = int(data1[i][4]) - int(data[j][4])
            print "Commit(s) updated = " + str(compare_commits)
            compare_lines_added = int(data1[i][5]) - int(data[j][5])
            print "Update on line(s) addition = " + str(compare_lines_added)
            compare_lines_deleted = int(data1[i][6]) - int(data[j][6])
            print "Update on line(s) deletion = " + str(compare_lines_deleted)
        elif flag == 0:
            print "New user!!!"
            print "For " + data1[i][0] + " and repo : " + data1[i][1] + " with " + data1[i][2] + " changes are > "
            compare_commits = int(data1[i][4]) - int(data[j][4])
            print "Commit(s) updated = " + str(compare_commits)
            compare_lines_added = int(data1[i][5]) - int(data[j][5])
            print "Update on line(s) addition = " + str(compare_lines_added)
            compare_lines_deleted = int(data1[i][6]) - int(data[j][6])
            print "Update on line(s) deletion = " + str(compare_lines_deleted)


compare()
