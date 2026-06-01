class TimeMap:

    def __init__(self):
        self.ktMap = {}
        self.kvMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ktMap:
            self.ktMap[key].append(timestamp)
        else:
            self.ktMap[key] = [timestamp]

        self.kvMap[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ktMap:
            return ""

        times = self.ktMap[key]
        print(times)

        l = 0
        r = len(times)
        while l < r:
            mid = (r+l)//2

            if times[mid] == timestamp:
                return self.kvMap[(key, timestamp)]
            elif times[mid] < timestamp:
                l = mid+1
            else:
                r = mid

        if times[l-1] < timestamp:
            return self.kvMap[(key, times[l-1])]

        return ""
