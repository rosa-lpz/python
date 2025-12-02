https://www.geeksforgeeks.org/python/understanding-python-pickling-example/

## Python Pickle — Python object serialization

Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk. What Pickle does is it “serializes” the object first before writing it to a file. Pickling is a way to convert a Python object (list, dictionary, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another Python script. It provides a facility to convert any Python object to a byte stream. This Byte stream contains all essential information about the object so that it can be reconstructed, or "unpickled" and get back into its original form in any Python. 

# Examples
### ****Pickling without a File****

In this example, we will serialize the dictionary data and store it in a byte stream. Then this data is deserialized using [pickle.loads()](https://www.geeksforgeeks.org/python/how-to-use-pickle-to-save-and-load-variables-in-python/) function back into the original Python object.

```python
import pickle

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
# type(b) gives <class 'bytes'>;
b = pickle.dumps(db)   

# For loading
myEntry = pickle.loads(b)
print(myEntry)
```

Output
```cmd
{'Omkar': {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000},   
'Jagdish': {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}}
```