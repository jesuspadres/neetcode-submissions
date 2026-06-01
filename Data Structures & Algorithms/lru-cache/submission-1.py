class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.usedKeys = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usedKeys.remove(key)
            self.usedKeys.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.usedKeys) == self.capacity and key not in self.cache:
            del self.cache[self.usedKeys.pop(0)]
        elif key in self.cache:
            self.usedKeys.remove(key)
        self.cache[key] = value
        self.usedKeys.append(key)

