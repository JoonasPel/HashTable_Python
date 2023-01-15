# Hash Table Class

This is a Python class that implements a basic hash table data structure. The class has a constructor that takes an optional parameter `length` which is used to initialize the size of the hash table.

## Methods

- `set_value(key, value)`: This method is used to set a value in the hash table. If the key already exists, it will raise a KeyError.
- `get_value(key, default_value)`: This method is used to get a value from the hash table. If the key is not found in the hash table, it will return the `default_value`.
- `update_value(key, new_value)`: This method is used to update a value in the hash table. If the key is not found in the hash table, it will raise a KeyError.
- `remove_key(key)`: This method is used to remove a key-value pair from the hash table. If the key is not found in the hash table, it will raise a KeyError.
- `hash_function(key)`: This method is used to compute the index of the key in the hash table. It uses the built-in Python function `hash()` to generate a hash value for the key and then applies the modulo operator with the length of the hash table to obtain the index.
- `is_bucket_increase_recommended()`: This method is used to check whether the number of items in the hash table is greater than a certain threshold (`_bucket_increase_threshold`) in relation to the number of buckets in the hash table.
- `increase_buckets()`: This method is used to increase the number of buckets in the hash table by a certain multiplier (`_increase_buckets_multiplier`). Existing keys and values will be rehashed so they can still be found.

## Example Usage
```python
hash_table = HashTable()
hash_table.set_value("key1", "value1")
print(hash_table.get_value("key1", "default")) # prints "value1"
hash_table.update_value("key1", "new_value")
print(hash_table.get_value("key1", "default")) # prints "new_value"
hash_table.remove_key("key1")
print(hash_table.get_value("key1", "default")) # prints "default"
```
## Unittests
`test_hashtable.py` includes unittests to test the basic behaviour of the class methods.

#### Note
This is just a basic implementation and it's not suitable for production usage. It's only meant for educational purposes.

