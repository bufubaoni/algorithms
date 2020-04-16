class LRUCache(object):

    def __init__(self, capacity):
        “””
        :type capacity: int
        “””
        self.capacity = capacity
        self.keys = []
        self.data = {}


    def get(self, key):
        “””
        :type key: int
        :rtype: int
        “””
        if key in self.keys:
            self.update_key(key)
        return self.data.get(key, -1)


    def put(self, key, value):
        “””
        :type key: int
        :type value: int
        :rtype: None
        “””
        self.update_key(key)
        if len(self.keys) > self.capacity:
            drop_key = self.keys.pop(0)
            self.data.pop(drop_key)
            self.data[key] = value
        else:
            self.data[key] = value

    def update_key(self, key):
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)