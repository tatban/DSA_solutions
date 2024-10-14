##############################################################################################
##                                                                                          ##
##                                  MAX HEAP IMPLEMENTATION                                 ##
##          Author: Tathagata Bandyopadhyay, Written on: 15.10.2024 01:43 Uhr CEST          ##
##                                                                                          ##
##############################################################################################

class MaxHeap:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.arr = arr.copy()
        self.build_heap()

    def build_heap(self):
        n = len(self.arr)-1
        for i in range(n//2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = self.get_left(i)
        right = self.get_right(i)
        if left <= len(self.arr)-1 and self.arr[left] > self.arr[i]:
            largest = left
        else:
            largest = i
        if right <= len(self.arr)-1 and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != i:
            self.swap(largest, i)
            self.heapify(largest)

    @staticmethod
    def get_parent(i):
        return (i-1) // 2

    @staticmethod
    def get_left(i):
        return 2*i+1

    @staticmethod
    def get_right(i):
        return 2*i+2

    def push(self, key):
        self.arr.append(key)
        current = len(self.arr)-1
        parent = self.get_parent(current)
        while parent >= 0:
            if self.arr[current] > self.arr[parent]:
                self.swap(parent, current)
            current = parent
            parent = self.get_parent(parent)

    def pop(self):
        if self.arr:
            val = self.arr[0]
            n = len(self.arr)
            self.swap(0, n-1)
            self.arr = self.arr[:n-1]
            self.heapify(0)
            return val
        else:
            return None

    def isValidHeap(self):
        n = len(self.arr)
        for i in range(0, (n//2)-1):
            left = self.get_left(i)
            if 0 <= left < n and self.arr[left] > self.arr[i]:
                return False
            right = self.get_right(i)
            if 0 <= right < n and self.arr[right] > self.arr[i]:
                return False
        return True

    def swap(self, i, j):
        tmp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp


def heap_sorted(array, ascending=False):
    mhr = MaxHeap(array)
    arr = []
    while mhr.arr:
        arr.append(mhr.pop())
    if ascending:
        return arr[::-1]
    else:
        return arr


if __name__ == "__main__":
    ara = [1, 3, 2, 28, 12, 4, 55, 7, 9, 16, 14]
    print(f"\n\n########################## Building Heap ##########################\n\n")
    print(ara)
    mh = MaxHeap(ara)
    print(mh.arr)
    print(mh.isValidHeap())
    print(ara)

    print(f"\n\n########################## Popping from Heap ##########################\n\n")
    for _ in range(6):
        print(mh.pop())
        print(mh.arr)
        print(mh.isValidHeap())

    print(f"\n\n########################## Heap Sort ##########################\n\n")
    B = [10, 23, 15, 6, 8, 7, 3, 25]
    print([b for b in heap_sorted(B)])
    print([b for b in heap_sorted(B, ascending=True)])
    print(B)
