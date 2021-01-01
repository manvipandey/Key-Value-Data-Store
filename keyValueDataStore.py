import os, json
from datetime import datetime

class KeyValueDataStore:
		
	# Constructor
	def __init__(self):
		name_of_file = input("Enter a file name : ")
		self.file_path= os.path.join(os.environ["USERPROFILE"], name_of_file + ".txt")
		with open(self.file_path, "w") as json_file:
			json_file.write(json.dumps({}, indent = 4))
	
	# To validate if the variable is a JSON object		
	def is_json(self, myjson):
		try:
			json.loads(myjson)
		except ValueError:
			return False
		return True
	
	# Creates a new key-value pair in the datastore
	def create(self, key, value):
		if type(key) != str:
			print("Key must be a string")
		elif len(key) > 32:
			print("Key length should not be more than 32")
		elif not self.is_json(value):
			print("Value must be a valid JSON Object")
		else:
			with open(self.file_path, "r") as json_file:
				datastore_as_dict = json.load(json_file)
			if key in datastore_as_dict:
				print("Key already exists")
			else:
				datastore_as_dict[key] = value
				with open(self.file_path, "w") as json_file:
					json.dump(datastore_as_dict, json_file, indent = 4)
	
	# Deletes the given key-value pair corresponding to the provided key
	def delete(self, key):
		with open(self.file_path, "r") as json_file:
			datastore_as_dict = json.load(json_file)
		if key not in datastore_as_dict:
			print("Key does not exist")
		else:
			del datastore_as_dict[key]
			with open(self.file_path, "w") as json_file:
				json.dump(datastore_as_dict, json_file, indent = 4)
	
	# Returns the JSON object corresponding to the provided key
	def read(self, key):
		with open(self.file_path, "r") as json_file:
			datastore_as_dict = json.load(json_file)
			if key not in datastore_as_dict:
				return "Key does not exist"
			else:
				return json.dumps(datastore_as_dict[key], indent = 4)	
	
	# Prints the current status of the DataStore			
	def view(self):
		with open(self.file_path, "r") as json_file:
			datastore_as_dict = json.load(json_file)
			print(json.dumps(datastore_as_dict, indent=4))
		