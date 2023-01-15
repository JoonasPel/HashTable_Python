from hashtable import HashTable
import time
import random


def populate(hash_table, count):
    s, i = "abcdefghijklm", 1
    while i < count:
        try:
            key = ''.join(random.sample(s, len(s)))
            value = random.randint(1,50)
            hash_table.set_value(key, value)
            i += 1
        except KeyError:
            pass

# asymptotic performance testing
if __name__ == "__main__":
    hash_table = HashTable(10*1000*1000)
    print("populating...")
    populate(hash_table, 5*1000*1000)
    print("populating done")
    hash_table.set_value("Joonas", 13)

    # time to find value by key
    REPEAT_SEARCH = 100*1000
    t0 = time.time_ns()
    for i in range(0, REPEAT_SEARCH):
        temp = hash_table.get_value("Joonas", 0)

    time_per_search = (time.time_ns() - t0) / 1000 / REPEAT_SEARCH
    print(f"elapsed time(µs) for one search: {round(time_per_search, 2)}µs")
