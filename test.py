from urlparse import urlparse
import os
import csv


def get_info():
    filename, file_extension = os.path.splitext('https://github.com/abhayraina74/InstaBot')
    p = urlparse(filename)
    q =p.path.split('/')
    print p.path
    print "Username : %s and Reponame : %s " %(q[1], q[2])

get_info()

def in_databse():
    for i in range(0,100):
        with open('Github-Repo.csv', 'rb') as f:
            reader = csv.reader(f, delimiter=';')
            for col in reader:
                print col[i]
in_databse()

# Bhai ab karna yeh hai ki yeh function username,reponame return kar rha hai.
# Chahe url.git hai ya bina .git hai.
# toh yeh database.csv mein write krna hai.
# aur loop chalana hai ki pehle file apne aap github_Repo.csv se url uthaye, username,reponame nikale
# and database.csv mein write krde