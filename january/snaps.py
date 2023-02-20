from collections import defaultdict
class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(defaultdict)
        self.snap_cnt = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[self.snap_cnt][index] = val

    def snap(self) -> int:
        self.snap_cnt += 1
        return self.snap_cnt - 1

    def get(self, index: int, snap_id: int) -> int:
        cur = snap_id
        while cur > 0 and index not in self.snaps[cur]:
            cur -= 1
        if index in self.snaps[cur]:
            return self.snaps[cur][index]
        return 0

obj = SnapshotArray(1)
obj.set(0,4)
obj.set(0,16)
obj.set(0,13)
print(obj.snap())
print(obj.get(0,0))
print(obj.snap())
print(obj.snap())

# [[1],[0,4],[0,16],[0,13],[],[0,0],[]]