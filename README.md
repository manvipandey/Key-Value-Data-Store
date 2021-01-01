# Key Value Data Store

This is a file-based key-value data store that supports the bsaic CRD(create, read and delete) operations.

# Installation

Just include [keyvaluedatastore.py](keyvaluedatastore.py) in your program directory and import it in your program.

# How to use

Firstly, instantiate the class and create an object.

The location of the class can be specified while creating the object. If no location is specified, the program will create the database in the root of your Userprofile folder.

The first operation is `create`. The `create()` function adds a key-value pair to the database. The key should be a string (upto 32 characters) and the value should be a valid json object. If the key already exists or the size of the key is greater than 32 characters, then the program will return an appropriate error response.

The next operation is `read`. This is the most simple operation. The `read()` function returns the value of the key which you pass as an argument. Appropriate error response is returned if the key doesn't exist.

The last operation is `delete`. The `delete()` function checks for the presence of a key in the file and removes it if it is present. If the key doesn't exist, appropriate error response is returned.

A demo of the working of all the functions can be found in the included [test.py](test.py) file.
