Github-Tracker
==================

Getting Started
---------------
clone our repoitory using the command

```git clone https://github.com/Github-Tracker/Github-Tracker Tracker && cd Tracker```


Usage :
-----------------
Github-tracker is a python based application that uses github API to fetch data and display data like Commits, Lines added or deleted in Graphical format.

1. First enter the username and repository-name of students in database.csv in this format :
  
  ```Username1,Repo-name1```

  ``` Username2,Repo-name2```

2. To fetch/update data, run trackerscript.py :
 (A file with name 'dd-mm-YYYY' will be created with today's data)
 
 ```pyhton trackerscript.py```
 
3. To compare data, run comparator.py and input two dates to compare progress betwen them :

```pyhton comparator.py```

   The format of dates should be this: ```dd-mm-yyyy```

4. After running comparator, you'll get data in ```final.csv``` .


Points to Remember
-----------------------
1. This Script only compares data till the last Sunday.
2. Do not run the script b/w 12:00 am to 5:30 am on Sunday.


Credits
-----------------
* [**Prince Yadav**](https://github.com/Princeyadav05/)
* [**Rohan Khurana**](https://github.com/rk2810/)
* [**Dhananjay Gambhir**](https://github.com/deejay6/)
 

