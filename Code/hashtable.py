#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Why and under what conditions? loops through both buckets and bucket items and is calculated by b * n/b"""
        # Collect all keys in each bucket
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Why and under what conditions?loops through both buckets and bucket items and is calculated by b * n/b"""
        all_values = []

        for bucket in self.buckets:  # Loop through all buckets
            for key, value in bucket.items():
                all_values.append(value)
        return all_values  # Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Why and under what conditions?loops through both buckets and bucket items and is calculated by b * n/b"""
        count = 0

        for bucket in self.buckets: # Loop through all buckets
            for item in bucket.items():
                count += 1  # Count number of key-value entries in each bucket
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n/b or l) Why and under what conditions? only traverses one bucket after going through the constant time processes"""
        bucket_index = self._bucket_index(key)  # Find bucket where given key belongs
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda item: item[0] == key)

        if item != None: # Check if key-value entry exists in bucket
            return True
        else:
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(n/b or l) Why and under what conditions?only traverses one bucket after going through the constant time processes"""
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key)  # TODO: Find bucket where given key belongs
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda item: item[0] == key) # TODO: Check if key-value entry exists in bucket

        if self.contains(key):
            return item[1]  # TODO: If found, return value associated with given key
        else:
            raise KeyError(f'Key not found: {key}')  # TODO: Otherwise, raise error to tell user get failed


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(n/b or l) Why and under what conditions?only traverses one bucket after going through the constant time processes"""
        bucket_index = self._bucket_index(key)  # TODO: Find bucket where given key belongs
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda item: item[0] == key)  # TODO: Check if key-value entry exists in bucket

        if item is not None:
            bucket.replace(item, (key, value)) # TODO: If found, update value associated with given key
            return
        else:
            bucket.append((key, value)) # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n/b or l) Why and under what conditions? only traverses one bucket after going through the constant time processes"""
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_index = self._bucket_index(key) # TODO: Find bucket where given key belongs
        bucket = self.buckets[bucket_index]
        item = bucket.find(lambda item: item[0] == key)  # TODO: Check if key-value entry exists in bucket

        if item is not None:
            bucket.delete(item)  # TODO: If found, delete entry associated with given key

            return
        else:
            raise KeyError(f'Key not found: {key}')  # TODO: Otherwise, raise error to tell user delete failed


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
