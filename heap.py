class Heap:

    def __init__(self) -> None:
        self.heap = []

    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
        
    def heapify_up(self,index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index],self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def heapify_down(self,index):
        
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index],self.heap[largest] = self.heap[largest],self.heap[index]
                index = largest

            else:
                break
    def delete(self):
        
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        del_max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return del_max

    def print_heap(self):
        print(self.heap)
h = Heap()
h.insert(5)
# h.print_heap()
h.insert(4)
# h.print_heap()
h.insert(9)
h.insert(3)
h.print_heap()
h.delete()
h.print_heap()
