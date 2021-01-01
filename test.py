from keyValueDataStore import KeyValueDataStore

data_store1 = KeyValueDataStore()

data_store1.create("A", '{"abc" : 10}') #Valid JSON
data_store1.create("B", '{"a" : 10, "b" : 20, "c" : 30}') #Valid JSON
data_store1.create("1","Manvi") #Invalid JSON
data_store1.create("C","{}") #Valid JSON
data_store1.create("D","{asdf}") #Invalid JSON
data_store1.create("E",'{ "age":100}') #Valid JSON
data_store1.create("F","{'age':100 }") #Invalid JSON
data_store1.create("G","{\"age\":100 }") #Valid JSON
data_store1.create("H",'{"age":100 }') #Valid JSON
data_store1.create("I",'{"foo":[5,6.8],"foo":"bar"}') #Valid JSON


print(data_store1.read("A")) #Prints the value corresponding to key "A"
print(data_store1.read("I")) #Prints the value corresponding to key "I"
print(data_store1.read("Z")) #Key does not exist

data_store1.view() #View Datastore

data_store1.delete("A") #Deletes key "A"
data_store1.delete("E") #Deletes key "E"
data_store1.delete("Z") #Key does not exist

data_store1.view() #View Datastore


