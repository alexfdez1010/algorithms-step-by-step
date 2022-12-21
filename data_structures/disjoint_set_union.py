
class DisjointSetUnion:

    def __init__(self, n: int):
        """
        Initialize a disjoint set union data structure with n elements.
        :param n: number of elements
        """
        self._sets = [i for i in range(n)]
        self._sizes = [1 for i in range(n)]

    def find(self, x: int) -> int:
        """
        Find the representative element of the set containing x.
        :param x: element
        :return: representative element of the set containing x
        """
        if self._sets[x] == x:
            return x

        return self.find(self._sets[x])

    def union(self, x: int, y: int) -> None:
        """
        Merge the sets containing x and y. If x and y are already in the same set, does nothing.
        :param x: element
        :param y: element

        :return: None
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self._sizes[x] < self._sizes[y]:
            self._sets[x] = y
            self._sizes[y] += self._sizes[x]

        else:
            self._sets[y] = x
            self._sizes[x] += self._sizes[y]

    def size(self):
        """
        Return the number of elements in the disjoint set union data structure.

        :return: number of elements
        """
        return len(self._sets)

    @property
    def sets(self):
        """
        Return the sets of the disjoint set union data structure.

        :return: sets
        """
        return self._sets