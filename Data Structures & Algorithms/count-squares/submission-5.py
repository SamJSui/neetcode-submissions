class CountSquares:

    def __init__(self):
        self.points = []
        self.cnter = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points.append(point)
        self.cnter[point] = self.cnter.get(point, 0)+1

    def count(self, point: List[int]) -> int:
        ret = 0
        visited = set()
        point = tuple(point)
        for p in self.points:
            dx, dy = p[0]-point[0], p[1]-point[1]
            if abs(dx) != abs(dy) or p in visited or p == point: continue

            x, y = point[0]+dx, point[1]+dy
            cornx, corny = (x, point[1]), (point[0], y)
            # print(p, point, cornx, corny, dx, dy)
            if p in self.cnter and cornx in self.cnter and corny in self.cnter:
                print(p, point, self.cnter[p], self.cnter[cornx], self.cnter[corny])
                ret += self.cnter[corny] * self.cnter[cornx] * self.cnter[p]
            visited.add(p)
        return ret
