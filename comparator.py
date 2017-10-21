import csv

name1 = raw_input("Enter name of older file(compare from) > ")
name2 = raw_input("Enter name of newer file(compare to) >  ")

with open(name1 + '.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
# print data
z = len(data)

with open(name2 + '.csv', 'rb') as f:
    read = csv.reader(f)
    data1 = list(read)
# print data1
x = len(data1)

#using git APIs
def compare():
    with open("final.csv",'wb') as final:
        writer = csv.DictWriter(final , fieldnames=['Name', 'Repo', 'Contributor', 'Commits(s) Updated', 'Update on line(s) addition',
                                                    'Update on line(s) deletion'], delimiter=',')
        writer.writeheader()
        for i in range(1, x):
            for j in range(1, z):
                if data1[i][0] == data[j][0] and data1[i][1] == data[j][1]:
                    global flag
                    flag = 1
                    if data1[i][2] == data[j][2]:
                        global flag1
                        flag1 = 1

                        compare_commits = int(data1[i][4]) - int(data[j][4])

                        compare_lines_added = int(data1[i][5]) - int(data[j][5])

                        compare_lines_deleted = int(data1[i][6]) - int(data[j][6])

                        writer.writerow({'Name': data1[i][0], 'Repo': data1[i][1], 'Contributor': data1[i][2],
                                         'Commits(s) Updated': str(compare_commits), 'Update on line(s) addition':
                                             str(compare_lines_added), 'Update on line(s) deletion': str(compare_lines_deleted)})
                        break
            if flag == 1 and flag1 == 0:
                compare_commits = int(data1[i][4]) - int(data[j][4])

                compare_lines_added = int(data1[i][5]) - int(data[j][5])

                compare_lines_deleted = int(data1[i][6]) - int(data[j][6])

                writer.writerow({'Name': data1[i][0], 'Repo': data1[i][1], 'Contributor': data1[i][2],
                                 'Commits(s) Updated': str(compare_commits), 'Update on line(s) addition':
                                     str(compare_lines_added), 'Update on line(s) deletion': str(compare_lines_deleted)})
            elif flag == 0:
                print "New user!!!"

compare()
