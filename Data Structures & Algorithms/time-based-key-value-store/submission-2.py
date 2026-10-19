from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.value_map = defaultdict(list)
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append(timestamp)
        self.value_map[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""

        result = ""
        if key in self.time_map:
            timestamps = self.time_map[key]
            n = len(timestamps)
            low = 0
            high = n - 1
            value_list = self.value_map[key]

            while low <= high:
                mid = low + (high - low) // 2
                if timestamp >= timestamps[mid]:
                    result = value_list[mid]
                    low = mid + 1
                else:
                    high = mid - 1
        
        return result


        
