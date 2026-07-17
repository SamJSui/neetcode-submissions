class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        vt = (value, timestamp)
        if key in self.d:
            self.d[key].append(vt)
        else:
            self.d[key] = [vt]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ''
        for v, t in reversed(self.d[key]):
            if t <= timestamp: return v
        return ''
