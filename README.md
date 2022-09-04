This project consist of to ultimately set up our server a copy of the AirBnB Website (HBnB).
# **0x00. AirBnB clone - The console**
![](images/65f4a1dd9c51265f49d0.png)

The project consist of four segments.
## **Description** 

In this particular project our main focus will be in the first segment, the console.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

It consist of a command interpreter (Cmd) to manage all objects for the AirBnb (HBnb) website. 
Each task is linked and will help you to:

Command interpreter descriptions:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage. 
* create all unittests to validate all our classes and storage engine

• Consist of creating new object like new Place or new User
## **What’s a command interpreter?**
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

• To retrieve an object from a storage ( data base or in a file)
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

• To ensure operations on objects like counting, computer stats, etc… 
## **Resources**
### **Read or watch:**

• To update attributes of an object
* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [uuid module](https://docs.python.org/3.8/library/uuid.html) 
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

• To destroy an object
## **Execution**
Your shell should work like this in interactive mode:

	Environment
$ ./console.py

	Ubuntu 20.04 LTS using python3 (version 3.8.5) will be used to interpret/test the project.
(hbnb) help

	Pycodestyle (version 2.8.*) for styling in the project.
Documented commands (type help <topic>):
========================================
EOF  help  quit

	Usage
(hbnb) 

	It consist of cloning the AirBnB_clone repository by the git commang git clone
(hbnb) 

	Followed by locating the directory by using the cd command cd AirBnB_clone
(hbnb) quit

	The console can be run in both interactive and non-interactive mode 
$

	For interactive mode: ./console and enter any command
But also in non-interactive mode: (like the Shell project in C)

	For non-interactive mode: echo  “<command>” | ./ console.py
$ echo "help" | ./console.py
(hbnb)

	After running one of the above commands this prompt should appear (hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit

	We can interact with the console and these command are used.
(hbnb) 

	create – To create an instance for a given class
$

	EOF and quit – to exit the CONSOLE 
$ cat test_help

	destroy – To  destroy an object for a given class and UUID
help

	show – To show an object based on class and UUID
$

	all – To  show all objects given access by the console or all objects for a particulars class.
$ cat test_help | ./console.py
(hbnb)

	update – To  update instance based on the class name and UUID by adding or updating attributes.
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 

$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![](images/815046647d23428a14ca.png)