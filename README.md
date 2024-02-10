# AirBnB Clone Project
 the AirBnB_clone project, a vital component of the software engineering curriculum at Holberton School. This project serves as a comprehensive learning opportunity, delving into fundamental concepts of advanced programming.

 The primary objective of this project is to construct a simplified version of the AirBnB website, with the initial step being the development of a console or command-line interpreter. This console plays a crucial role in managing website objects, facilitating tasks such as creation, retrieval, manipulation, and deletion.

 The project adopts an object-oriented approach, where classes represent various entities, including BaseModel, User, State, City, Amenity, Place, and Review. It's worth noting that all classes inherit from the BaseModel class.

 The console operates on specific commands, allowing users to execute operations such as object creation, display, modification, and deletion. Furthermore, the project incorporates a basic file storage system utilizing the FileStorage class for serialization and deserialization of instances.

 Written in Python, the project is interpreted and tested on Ubuntu 14.04 LTS using Python3.

# Description of the command interpreter:
 The console functions as the chief interpreter within our AirBnB clone venture, entrusted with the supervision of object handling. Its capabilities extend across a broad spectrum of tasks, ranging from object inception, retrieval from various data sources, manipulation, attribute adjustments, elimination, and beyond.

## How to start it:
 navigate in the directory and enter this command: ./console.py
## How to use it:
 our console can do this things:
 - `create <Class_Name>`: Creates a new instance of BaseModel, saves it (to the JSON file) an
 prints the id. Ex: $ create BaseModel

 - `show <Class_Name> <id>` Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234

 - `destroy <Class_Name> <id>` Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

 - `all <Class_Name>` Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all

 - `update <class name> <id> <attribute name> "<attribute value>"` Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

 - `<Class_Name>.all()` Prints all string representation of all instances based class name Ex: $ User.all()
 - `<class name>.count()` Print the number of instance for class name Ex: $User.count()

 - `<class name>.show(<id>)` Prints the string representation retrieve an instance based on its ID Ex: User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")

 - `<class name>.destroy(<id>)` Destroy an instance based on his ID Ex: User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")

 - `<class name>.update(<id>, <attribute name>, <attribute value>)` Update an instance based on his ID Ex: User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")

## Examples
![Examples](https://github.com/islamhasib953/AirBnB_clone/blob/main/Screenshot%20from%202024-02-10%2020-46-59.png)
