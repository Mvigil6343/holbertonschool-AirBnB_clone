<center> <h1>HBNB - The Console</h1> </center>
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.
---
<center><h3>Repository Contents by Project Task</h3> </center>

<p>| Tasks | Files | Description |</p>
<p>| ----- | ----- | ------ |</p>
<p>| 0: Authors/README File | [AUTHORS](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/AUTHORS) | Project authors |</p>
<p>| 1: Pep8 | N/A | All code is pep8 compliant|</p>
<p>| 2: Unit Testing | [/tests](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/tree/main/tests) | All class-defining modules are unittested |</p>
<p>| 3. Make BaseModel | [/models/base_model.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) | Defines a parent class to be inherited by all model classes |</p>
<p>| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|</p>
<p>| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/models/__init__.py)  [/models/base_model.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) | Defines a class to manage persistent file storage system|</p>
<p>| 6. Console 0.0.1 | [console.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |</>
<p>| 7. Console 0.1 | [console.py](https://github.com/Mvigil6343/holbertonschool-AirBnB_clone/blob/main/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |</p>

<center> <h2>General Use</h2> </center>
<p>1. First clone this repository.</p>
<p>2. Once the repository is cloned locate the "console.py" file and run it as follows:</p>
```
<p>/AirBnB_clone$ ./console.py</p>
```
<p>3. When this command is run the following prompt should appear:</p>
```
<p>(hbnb)</p>
```
<p>4. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.</p>
<p>##### Commands</p>
<p>    * create - Creates an instance based on given class</p>
<p>    * destroy - Destroys an object based on class and UUID</p>
   <p> * show - Shows an object based on class and UUID</p>
    <p>* all - Shows all objects the program has access to, or all objects of a given class</p>
    <p>* update - Updates existing attributes an object based on class name and UUID</p>
    <p>* quit - Exits the program (EOF will as well)</p>
<p>##### Alternative Syntax</p>
<p>Users are able to issue a number of console command using an alternative syntax:</p>
 <p>   Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])</p>
<p>Advanced syntax is implemented for the following commands:</p>
  <p>  * all - Shows all objects the program has access to, or all objects of a given class</p>
 <p>   * count - Return number of object instances by class</p>
 <p>   * show - Shows an object based on class and UUID</p>
 <p>  * destroy - Destroys an object based on class and UUID</p>
 <p>   * update - Updates existing attributes an object based on class name and UUID</p>
<br>
<br>
<p><center> <h2>Examples</h2> </center></p>
<p><h3>Primary Command Syntax</h3></p>
<p>###### Example 0: Create an object</p>
<p>Usage: create <class_name></p>
```
<p>(hbnb) create BaseModel</p>
```
```
<p>(hbnb) create BaseModel</p>
<p>3aa5babc-efb6-4041-bfe9-3cc9727588f8</p>
<p>(hbnb)</p>
```
<p>###### Example 1: Show an object</p>
<p>Usage: show <class_name> <_id></p>
```
<p>(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8</p>
<p>[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}</p>
<p>(hbnb)</p>
```
<p>###### Example 2: Destroy an object</p>
<p>Usage: destroy <class_name> <_id></p>
```
<p>(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8</p>
<p>(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8</p>
<p>** no instance found **</p>
<p>(hbnb)</p>
```
<p>###### Example 3: Update an object</p>
<p>Usage: update <class_name> <_id></p>
```
<p>(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"</p>
<p>(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f</p>
<p>[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
<p>'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}</p>
<p>(hbnb)</p>
```
<h3>Alternative Syntax</h3>
<p>###### Example 0: Show all User objects</p>
<p>Usage: <class_name>.all()</p>
```
<p>(hbnb) User.all()</p>
<p>["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', <p>'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]</p>
```
<p>###### Example 1: Destroy a User</p>
<p>Usage: <class_name>.destroy(<_id>)</p>
```
<p>(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")</p>
<p>(hbnb)</p>
<p>hbnb) User.all()</p>
<p>(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]</p>
```
<p>###### Example 2: Update User (by attribute)</p>
<p>Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)</p>
```
<p>(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")</p>
<p>(hbnb)</p>
<p>(hbnb) User.all()</p>
<p>(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]</p>
```
<p>###### Example 3: Update User (by dictionary)</p>
<p>Usage: <class_name>.update(<_id>, <dictionary>)</p>
```
<p>(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})</p>
<p>(hbnb)</p>
<p>(hbnb) User.all()</p>
<p>(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]</p>
```
<br>
<h1>AUTHORS</h1>
<p>Giselle Nieves - Holberton Student - <a href="https://github.com/Gisezegk"> Gise</a></p>
<p>Marcos Vigil - Holberton Student - <a href="https://github.com/Mvigil6343"> Marcos</a></p>
<p>Anit Rodriguez - Holberton Student - <a href="https://github.com/AnitRodriguez"> Anit</a></p>
