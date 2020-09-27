# Python Data Scieence Bootcamp combined notes

## Day 1
creating environment for Jupyter lab
python -m ipykernel install --user --name=firstEnv

cloning an environment (change the name for example)
conda create --name new_name --clone old_name
conda remove --name old_name --all # or its alias: `conda env remove --name old_name`

#removing unwanted kernels
jupyter kernelspec list
jupyter kernelspec uninstall unwanted-kernel

BASH important commands man (user manual)
man mkdir

redirects
takes the output of a command and "redirects" it to a different location, usually a file

pipes |
redirects the output of one command to another one


grep
searches for patterns

copy line 10-15 to another file 
```
sed -n '10,15p' file1.txt > file2.txt
```
#replace a certain item
```
sed "s/<string to replace>/<string to replace with>/g" <source_file> <target_file>
    used in bash exercise
    sed -i 's/,/;/g' <name of file>
```
#find how many entries "Pierce Brosnan" shops up
grep 'Pierce Brosnan' cast.csv | wc -l

select a specific column |sort| show onnly unique entries | find the desired value | return how many rows
```
cut -d ";" -f 1 cast.csv | sort | uniq -c | grep "Batman" | wc -l
```
#select title column|sort|count unique|sort results by numbers
```
cut -d ";" -f 1 cast.csv | sort | uniq -c | sort -n
```
#2 3 634 468
#3 done, but has to be saved to a different file
#5 58
#6 Batman
#7 sorta confused wrt roles identification in the database.
cut -d ";" -f 4 cast.csv | sort | uniq -d | wc -l gave me 7317 (but some are like Zu Zuniga)
#8 Actor 2407 470
#9 around the world in eighty days with 1298

## Day 2

### Morning lecture
line 15 index vs range focus
list inside tuples can be modified while the tuple itself cannot 

tuple syntax is very helpgul when switching values 

e.g (x,y) = (y,x) 

Dictionary keys must be a data structure that is immutable (e.g a string)
the value has to be mutable

For dictionaries with a list within
```
my_dict['key'][0]
```
Very helpful to obtain the 
```
man #bash
help(dict)
dir(dict) # all the python functionality/methods
```

using the IN operator it will go through the keys.
if you need values you will need to use the .value() method

except Exception as e:

### copies 
What we have used to this point:
```
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
```
Output
```
Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Old List: 140673303268168

New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of New List: 140673303268168
```
old_list and new_list point to the same id hence any changes to any of the aforementioned lists will results in changes in both. Hence new_list is just a pointer to the old_list.

we can create two types of copies:
* shallow copy
* deep copy

But we require the following module and use its associated functions
```
import copy
# consider any object named x
copy.copy(x)
copy.deepcopy(x)
```
#### Shallow copy
A shallow copy creates a new object which stores the reference of the original elements. Therefore a shallow copy doesn't create a copy of nested object, instead it just copies the reference to that nested object

Shallow copy example
```
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
```
Output
```
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```
However, the main difference with between shallow and deepcopy comes with changes to nested object
```
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
```
```
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
```
#### Deep copy
A deep copy created a new object and recursively adds the copes of nested objects present in the original elements.

```
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
```
Output
```
Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

### Collection modules

#### module
A module is nothing but a .py script that cna be called in another .py script
[base modules](https://docs.python.org/3/py-modindex.html) available in python
#### packages
Packages are a collection of related modules stacked together (e.g. Numpy,SciPy)
#### NamedTuple
usually the data stored in tuples can only be accessed through indexes but we can use namedtuple()
```
from collections import namedtuple
fruit = namedtuple('fruit','number variety color')guava = fruit(number=2,variety='HoneyCrisp',color='green')apple = fruit(number=5,variety='Granny Smith',color='red')
```
#### Counter
Counter is a dict subclass which helps to count hashable objects
examples:
* lists (can also use strings)
```
#lists
lst = [5,6,7,1,3,9,9,1,2,5,5,7,7]
c = Counter(lst)
print(c)

# strings
c = Counter('abcacdabcacd')
print(c)
```
```
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})
Counter({'a': 4, 'c': 4, 'b': 2, 'd': 2})
```
* Sentences
```
s = 'the lazy dog jumped over another lazy dog'
words = s.split()
Counter(words)
```

```
Counter({'another': 1, 'dog': 2, 'jumped': 1, 'lazy': 2, 'over': 1, 'the': 1})
```
most_common([n])
```
s = 'the lazy dog jumped over another lazy dog'
words = s.split()
Counter(words).most_common(3)
```
```
[('lazy', 2), ('dog', 2), ('the', 1)]
```

Most common patterns when using the counter() object
```
sum(c.values())                 # total of all counts 
c.clear()                       # reset all counts 
list(c)                         # list unique elements 
set(c)                          # convert to a set 
dict(c)                         # convert to a regular dictionary c.items()                       # convert to a list like (elem, cnt) 
Counter(dict(list_of_pairs))    # convert from a list of(elem, cnt) 
c.most_common()[:-n-1:-1]       # n least common elements 
c += Counter()                  # remove zero and negative counts
```

#### Ordered Dict
a dictionary subclass that remembers ther order in which that keys were first inserted. Can be used with sorting methods to make a sorted dictionary

Sorted by key (alphabeticaly)
```
# let d be any dict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
```
```
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
```
Sorted by value
```
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
```
```
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
```




user1_answer = input("%s, <the message>" % variable)

### datetime
To easily manage use date and time we use the datetime package
```
# import datetime class from datetime module
from datetime import datetime
```

#### strptime() strftime()
strptime() converts a string into a datetime object and strftime() does the reverse

the strings have to be in a specific format and so refer to the [documentation](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

example of its usage
```
my_string = '2019-10-31'

# Create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string, "%Y-%m-%d")

print(my_date)
print('Type: ',type(my_date))
```

Python considers Monday as the first day of the week (index num 0)

[best ressource](https://www.dataquest.io/blog/python-datetime-tutorial/)

To determine the number of days for a given month in python
```
from calendar import monthrange # supports leap years
month = 10
year = 2016
monthrange(year,month)
```

## Day 3
### APIs

stands for Application Programming Interface.
allows 2 computer to communicate with each others 
<img src=https://i.imgur.com/T4CD6mc.png>

a company's API is a dedicated [URLs](https://en.wikipedia.org/wiki/URL) that return pure data response

most APIs require an access token and have a limit to the number of "calls" on a given day or per minutes

* “Application” can refer to many things. Here are some of them in the context of API:

    * A piece of software with a distinct function.
    * The whole server, the whole app, or just a small part of an app.

* Types of APIs
    * SOAP
    * XML-RPC
    * JSON-RPC
    * REST

SOAP APIs
stand for simple object Access Protocol with [ACID](https://en.wikipedia.org/wiki/ACID) compatibility
TL:DR great for critical info and banking

XML-RPC (Extensible markup language – Remote Procedure Calls) is a protocol that uses a specific XML format to transfer data. 

JSON-RPC (JavaScript Object Notation) is a protocol which uses JSON format to transfer data.

REST Representational State Transfer use a data-driven architectural style. REST APIs are based on URIs HTTP protocol.

So why REST is prefered? scalability, security SSL capable, compatibility, data health

REST stands for REpresentational State Transfer.

It means when a RESTful API is called, the server will transfer to the client a representation of the state of the requested resource.

### XML
stands for Extensible Markup Language
currently being replaced by JSON

XML is a markup language like HTML and basically doesn't do anything but wraps the data in tags that are usable for any program to parse through


XML is designed to carry data 
HTML is designed to structure/display data for websites (mostly)

in XML the author must define the tags and document structure. HTML it has already been defined

### JSON
stands for JavaScript Object Notation
language independant like XML

JSON is different to XML as it only has a tag at the beginning of the element (none at the end)

very similar ta python dict
true/false are not capitalized and null is none. if you use the import Json module it will correct them
We can access the data by keys like a dictionary

saving variable (for the session only)
export
```
FOURSQUARE_CLIENT_ID=<your_client_id>
export FOURSQUARE_CLIENT_SECRET=<your_client_secret>
curl -X GET -G "https://api.foursquare.com/v2/venues/explore"  -d client_id=$FOURSQUARE_CLIENT_ID -d client_secret=$FOURSQUARE_CLIENT_SECRET  -d v="20200731"  -d ll="45.6387,-122.6615"  -d query="coffee"  -d limit=1
```
### HTTP requests

HTTP stands for Hypertext Transfer Protocol and is used to structure requests and responses over the internet.  HTTP requires data to be transferred from one point to another over the network.

The transfer of resources happens using TCP (Transmission Control Protocol
[how the internet magic happen](https://www.codecademy.com/articles/http-requests)

## Day 5
### Databases
A relational database is a type of database that organizes data into tables, and links them, based on defined relationships. These relationships enable you to retrieve and combine data from one or more tables with a single query.

Entity: a person,place or thing we want to track in a database.
e.g. James is an entitiy instance(record or row in a table)

Attribute: describes various characteristics about an individual entity
e.g columns in the table

Primary key/identifier: attribute or group attributes that UNIQUELY identifies an instance of the entity

Relationship: describes how one or more entities (tables) interact with each other

Cardinality: the count of instances that are allowed or are necessary between entity relationships (one to one ) (one to many) relationships

Crow's foot notation
e.g. one student can have from 0 to many phone numbers. however one phone number MUST have an associated studentIDkey

reminder the way to create a many to many relationship is through a bridge table. e.g. one student can be enrolled in many courses and one course can have many student enrolled in

subqueries (supa pwoerful as it takes the result of one query and passes it to the next one)
```
SELECT * FROM exercise_logs WHERE type IN (
    SELECT type FROM drs_favorites WHERE reason LIKE "%cardiovascular%");
    -- % is used to find the exact word 
```
```
SELECT title FROM songs WHERE artist IN (SELECT name FROM artists WHERE genre == 'Pop')
```
When we use "HAVING" we're applying the conditions to the grouped values, not the individual values in the individual rows

SUM,MIN,MAX,AVG

```
-- always group by ... HAVING

SELECT author, SUM(words) as 'total_words' FROM books GROUP BY author HAVING total_words > 1000000;

SELECT author, AVG(words) as 'avg_words' FROM books GROUP BY author HAVING avg_words > 150000
```

[who does what](https://www.khanacademy.org/computing/computer-programming/sql/more-advanced-sql-queries/a/who-issues-sql-queries)
TL:DR DS better be gods at SQL queries

```
SELECT COUNT(*) FROM exercise_logs WHERE
    heart_rate >= ROUND(0.50 * (220-30)) 
    AND  heart_rate <= ROUND(0.90 * (220-30))
```
CASE (similar to IFs)

```
SELECT type, heart_rate,
    CASE 
        WHEN heart_rate > 220-30 THEN "above max"
        WHEN heart_rate > ROUND(0.90 * (220-30)) THEN "above target"
        WHEN heart_rate > ROUND(0.50 * (220-30)) THEN "within target"
        ELSE "below target"
    END as "hr_zone"

    SELECT COUNT(*),
```
before updating data always ALWAYS make sure that you run a SELECT statement of what you are about to do

```
UPDATE users SET deleted = true WHERE id = 1;

SELECT id, deleted FROM users WHERE id = 1;

-- or append (LIMIT 1)
```
[ACID concepts](https://en.wikipedia.org/wiki/ACID)

Whenever we issue a command like CREATE, UPDATE, INSERT, or DELETE, we are automatically starting a transaction. However, if we want, we can also wrap up multiple commands inside a bigger transaction. It may be that we only want an UPDATE to go through if another UPDATE goes through as well
```
BEGIN TRANSACTION;
UPDATE people SET husband = "Winston" WHERE user_id = 1;
UPDATE people SET wife = "Winnefer" WHERE user_id = 2;
COMMIT;
```
If the database is unable to issue both those UPDATE commands for some reason, then it will rollback the transaction and leave the database how it was when it started.

This is very helpful in the event someone is making a change at the same time as we are about to make one which could cause chaos.

granting access privilege
```
GRANT FULL ON TABLE users TO super_admin;
GRANT SELECT ON TABLE users TO analyzing_user;
```

## Wk1

### Panda
A learning investment in PYthon, Panda and  Numpy will yield huge dividend

Most notes are on the notebook
### sql part 2
ODBS: Open Database Connectivity.

JDBC: Java Database Connectivity

Main advantage of JDBC is that the API to access the databse is standard. No need to devellop code for different database

* 1 get a coonection to the database
    * basic synthax: jdbc:<drive protocol>:<drive connection details>
    e.g. jdbc:mysql://localhost:3306/demodb
* 2 create a statement object
    * myConn.createStatement()
* 3 execute SQL query
    * myRs = myStmt.executeQuery("select * from table")
* 4 process the result set
    * while (myRs.next()) { 
        //read data from each rows
    }