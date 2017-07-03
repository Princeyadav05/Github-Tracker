from urlparse import urlparse
import os
import csv
s = []


def get_info(url):
    filename, file_extension = os.path.splitext(url)
    p = urlparse(filename)
    q =p.path.split('/')
    print p.path
    print "Username : %s and Reponame : %s " %(q[1], q[2])
    return q[2]


def in_databse():
    with open('Github-Repo.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for col in reader:
            s.append(col)
        print s
        with open('database.csv', 'wb') as db:
            writer = csv.DictWriter(db , fieldnames=['Username','Repo'] , delimiter=',')
            writer.writeheader()
            for i in range(1, len(s)):
                print s[i][3]
                writer.writerow({'Username': s[i][2],'Repo': get_info(s[i][3])})

in_databse()
# Bhai ab karna yeh hai ki yeh function username,reponame return kar rha hai.
# Chahe url.git hai ya bina .git hai.
# toh yeh database.csv mein write krna hai.
# aur loop chalana hai ki pehle file apne aap github_Repo.csv se url uthaye, username,reponame nikale
# and database.csv mein write krde