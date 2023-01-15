import unittest
import random
from hashtable import HashTable


class HashTableTest(unittest.TestCase):
    # populate hash_table with random key,value pairs. Return these pairs
    def create_and_set_keys(self, hash_table, item_count):
        if item_count > 2000:
            raise ValueError("item_count too high. Max 2000.")
        keys, items, s = set(), {}, "abcdefgh"
        # populate until item_count reached. "immune" to collaterals
        while len(keys) < item_count:
            keys.add(''.join(random.sample(s, len(s))))
        for key in keys:
            value = random.randint(1, 50)
            items[key] = value
            hash_table.set_value(key, value)
        return items

    def test_init(self):
        test_map = HashTable(0)
        self.assertEqual(test_map._length, 100)
        self.assertEqual(len(test_map._table), 100)
        test_map = HashTable(-500)
        self.assertEqual(test_map._length, 100)
        self.assertEqual(len(test_map._table), 100)
        test_map = HashTable(10)
        self.assertEqual(test_map._length, 10)
        self.assertEqual(len(test_map._table), 10)

    def test_set_and_get_value(self):
        # init and generate data
        test_table = HashTable(1)
        items = self.create_and_set_keys(test_table, 3)
        # test
        for key, value in items.items():
            self.assertEqual(test_table.get_value(key, 0), value)
            with self.assertRaises(KeyError):
                test_table.set_value(key, 55)
        self.assertEqual(test_table.get_value('Tuntematon', -1), -1)

        # init and generate data
        test_table = HashTable(100)
        items = self.create_and_set_keys(test_table, 25)
        # test
        for key, value in items.items():
            self.assertEqual(test_table.get_value(key, 0), value)
            with self.assertRaises(KeyError):
                test_table.set_value(key, 55)
        self.assertEqual(test_table.get_value('Tuntematon', -1), -1)

        # init
        test_table = HashTable(10)
        # test
        self.assertEqual(test_table.get_value('Tuntematon', 0), 0)

    def test_hash_function(self):
        # init
        test_map = HashTable(1)
        str_0, str_1, str_2 = 'moi', 'hei', 'hoi'
        # test
        self.assertEqual(test_map.hash_function(str_0), 0)
        self.assertEqual(test_map.hash_function(str_1), 0)
        self.assertEqual(test_map.hash_function(str_2), 0)

    def test_update_value(self):
        # init
        test_table = HashTable(10)
        items = self.create_and_set_keys(test_table, 7)
        test_table.set_value('Teemu', 22)
        # test
        for key, value in items.items():
            test_table.update_value(key, value+3)
            self.assertEqual(test_table.get_value(key, 0), value+3)
        with self.assertRaises(KeyError):
            test_table.update_value('Tuntematon', 5)
        self.assertEqual(test_table.get_value('Teemu', 0), 22)

    def test_remove_key(self):
        # init
        test_table = HashTable(100)
        items = self.create_and_set_keys(test_table, 53)
        # test
        key = next(iter(items))
        test_table.remove_key(key)
        self.assertEqual(test_table.get_value(key, 0), 0)
        with self.assertRaises(KeyError):
            test_table.remove_key('Tuntematon')

        # init
        test_table = HashTable(1)
        items = self.create_and_set_keys(test_table, 6)
        # test
        key = next(iter(items))
        test_table.remove_key(key)
        self.assertEqual(test_table.get_value(key, 0), 0)
        with self.assertRaises(KeyError):
            test_table.remove_key('Tuntematon')

    def test_is_bucket_increase_recommended(self):
        test_table = HashTable(5)
        self.create_and_set_keys(test_table, 3)
        self.assertFalse(test_table.is_bucket_increase_recommended())
        self.create_and_set_keys(test_table, 3)
        self.assertTrue(test_table.is_bucket_increase_recommended())

    # "private" _variables accessed for the purpose of testing
    def test_increase_buckets(self):
        buckets = [1, 2, 3, 4] + list(range(5, 110+1, 9))
        for init_bucket in buckets:
            test_table = HashTable(init_bucket)
            self.assertEqual(test_table._length, init_bucket)
            items = self.create_and_set_keys(test_table, init_bucket//2 + 1)
            test_table.increase_buckets()
            for key, value in items.items():
                self.assertEqual(test_table.get_value(key, 0), value)
            self.assertEqual(test_table.get_value('Tuntematon', 0), 0)
            self.assertEqual(test_table._length, init_bucket *
                             test_table._increase_buckets_multiplier)


# allows running tests in cmd
if __name__ == "__main__":
    unittest.main(verbosity=2)
