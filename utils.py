import heapq


class MaxHeapObj(object):
    """
    Overrides the comparison, so you can create a max heap easily
    See https://stackoverflow.com/a/40455775
    """

    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


class MinHeap(object):
    """
    A nice class-based interface to the heapq library
    See https://stackoverflow.com/a/40455775
    """

    def __init__(self):
        self.h = []

    def heappush(self, x):
        heapq.heappush(self.h, x)

    def heappop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)


class MaxHeap(MinHeap):
    """
    A nice class-based interface to create a max heap, using the heapq lib.
    See https://stackoverflow.com/a/40455775
    """

    def heappush(self, x):
        heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self):
        return heapq.heappop(self.h).val

    def __getitem__(self, i):
        return self.h[i].val
