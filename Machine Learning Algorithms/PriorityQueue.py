class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(reverse=True)  # Sort in descending order by priority

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            raise IndexError("pop from an empty priority queue")

# Example usage:
priority_queue = PriorityQueue()

priority_queue.push('Task 1', 3)
priority_queue.push('Task 2', 1)
priority_queue.push('Task 3', 2)

while not priority_queue.is_empty():
    (priority, task) = priority_queue.pop()
    print(f"{task}: priority {priority}")
