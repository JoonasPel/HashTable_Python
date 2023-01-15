class HashTable:
    def __init__(self, length=100):
        if length <= 0:
            length = 100
        self._length = length
        self._table = [[] for x in range(self._length)]
        # total items in table. Used to "invoke" bucket increase.
        self._items = 0
        # re-hash more buckets when this is reached
        self._bucket_increase_threshold = 0.8
        # new bucket count is old bucket count times this multiplier
        self._increase_buckets_multiplier = 2

    # raises KeyError if key already does exist
    def set_value(self, key, value):
        index = self.hash_function(key)
        values = self._table[index]
        idx = next((idx for idx, value in enumerate(values) if value[0] == key), -1)
        if idx == -1:
            values.append((key, value))
            self._items += 1
        else:
            raise KeyError("Key already exists. Use updateValue() instead.")

    # returns default_value if key not found
    def get_value(self, key, default_value):
        index = self.hash_function(key)
        values = self._table[index]
        value = next((value for value in values if value[0] == key), '')
        return value[1] if value else default_value

    # raises KeyError if key doesn't exist
    def update_value(self, key, new_value):
        index = self.hash_function(key)
        values = self._table[index]
        idx = next((idx for idx, value in enumerate(values) if value[0] == key), -1)
        if idx != -1:
            self._table[index][idx] = (key, new_value)
        else:
            raise KeyError("Key doesn't exist. Can't update.")

    # raises KeyError if key doesn't exist
    def remove_key(self, key):
        index = self.hash_function(key)
        values = self._table[index]
        idx = next((idx for idx, value in enumerate(values) if value[0] == key), -1)
        if idx != -1:
            del values[idx]
            self._items -= 1
        else:
            raise KeyError("Key doesn't exist. Can't remove.")

    def hash_function(self, key) -> int:
        return hash(key) % self._length

    # if there are too many total items in comparison to total buckets, True
    def is_bucket_increase_recommended(self) -> bool:
        return self._items / self._length > self._bucket_increase_threshold

    def increase_buckets(self):
        old_table = self._table
        self._length *= self._increase_buckets_multiplier
        self._table = [[] for x in range(self._length)]
        self._items = 0
        for bucket in old_table:
            for key, value in bucket:
                self.set_value(key, value)